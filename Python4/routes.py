#Archivo: routes.py
from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, Usuario

#Blueprint: Un mini-orquestador para agrupar rutas y exportarlas a app.py
api_bp = Blueprint('api',__name__)

@api_bp.route('/usuarios/registrar', methods=['POST'])
def registrar_usuario() -> tuple[Response, int]:
    try: 
        payload = request.get_json()

        #1. Hashing Criptogràfico en RAM
        clave_segura = generate_password_hash(payload['password'])

        #2. [INSTANCIACIÒN]: Objeto en RAM
        nuevo_user = Usuario(
            username=payload['username'],
            password_hash=clave_segura,
            rol=payload.get('rol', 'Operario')
        )
        #3. [ABSTRACCIÒN TRANSACCIONAL]: Guardamos en disco 
        db.session.add(nuevo_user)
        db.session.commit() #Consolidaciòn atòmica

        return jsonify({"mensaje": "Exito", "data": nuevo_user.serializar()}), 200 
    
    except Exception as e:
        db.session.rollback() #Revierte la RAM si hubo un fallo (ej: username du)
        return jsonify({"error": "Fallo de integridad", "detalle": str(e)}), 400
    
@api_bp.route('/usuarios', methods=['GET'])
def listar_usuarios() -> tuple[Response, int]:
        #Paginacion: Protege la RAM para no cargar i millon de registros de golpe
        pagina = request.args.get('page', 1, type=int)
        paginacion = Usuario.query.paginate(page=pagina, per_page=10, error_out=False)

        resultado = [u.serializar() for u in paginacion.items]

        return jsonify({
            "pagina_actual": paginacion.page,
            "total_paginas": paginacion.pages,
            "usuarios": resultado
        }), 200
    
#Agregar en routes.py
@api_bp.route('/login', methods=['POST'])
def login() -> tuple[Response, int]:
    payload = request.get_json()

    # 1. Buscamos al usuario en el disco
    usuario = Usuario.query.filter_by(username=payload.get('username')).first()

    # 2. Validacion de hashes (Compara texto plano vs hash almacenado)
    if usuario and check_password_hash(usuario.password_hash, payload.get('password')):
        # 3. Generamos Token inyectando la identidad (Rol)
        identidad ={"username": usuario.username, "rol": usuario.rol}
        token_acceso = create_access_token(identity=identidad)

        return jsonify({"mensaje": "Login exitoso", "token": token_acceso}), 200
    
    return jsonify({"error": "Creedenciales invalidàs"}), 401
# Agregar en routes.py
@api_bp.route('/inventario/critico', methods=['POST'])
@jwt_required() # BARRERA 1: Bloquea peticiones no autenticadas (Sin Token)
def modificar_inventario() -> tuple[Response, int]:
     # Extraemos el diccionario de identidad inyectando en el Token 
     usuario_actual = get_jwt_identity()

     # BARRERA 2: Control de Acceso Basado en Roles (RBAC)
     if usuario_actual.get("rol") != "Admin":
          return jsonify({"error": "Forbidden: Requiere privilegios de Administrador"})
     
     return jsonify({
          "mensaje": "Acceso concedido al servidor.",
          "operador": usuario_actual["username"]
     }), 200