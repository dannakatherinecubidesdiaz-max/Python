  #Agregar en routes.py
@api_bp.route('/login', methods=['POST'])
def login() -> tuple[Response, int]:
    payload = request.get_json()

    # 1. Buscamos al usuario en el disco
    usuario = Usuario.query.filter_by(username=payload.get('username')).first()

    # 2. Validacion de hashes (Compara texto plano vs hash almacenado)
    if usuario and check_password_hash(usuario.password_hash, payload.get('password')):
        # 3. Generamos Token inyectando la identidad (Rol)
        identidad ={"username": usuario.username,
                    "rol": usuario.rol
                    }
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

# Archivo: routes.py
from flask import Blueprint, request, jsonify, Response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# Importamos Producto (asumiendo que está definido en models.py)
from models import db, Usuario, Producto 

api_bp = Blueprint('api', __name__)

@api_bp.route('/usuarios/registrar', methods=['POST'])
def registrar_usuario() -> tuple[Response, int]:
    try: 
        payload = request.get_json()
        # 1. Hashing Criptográfico
        clave_segura = generate_password_hash(payload['password'])

        nuevo_user = Usuario(
            username=payload['username'],
            password_hash=clave_segura,
            rol=payload.get('rol', 'Operario')
        )
        
        db.session.add(nuevo_user)
        db.session.commit() 

        return jsonify({"mensaje": "Usuario registrado con éxito", "data": nuevo_user.serializar()}), 201 
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Fallo de integridad o datos faltantes", "detalle": str(e)}), 400

@api_bp.route('/login', methods=['POST'])
def login() -> tuple[Response, int]:
    payload = request.get_json()
    usuario = Usuario.query.filter_by(username=payload.get('username')).first()

    # Validamos que el usuario exista y que el password coincida con el hash
    if usuario and check_password_hash(usuario.password_hash, payload.get('password')):
        # Inyectamos el 'rol' en la identidad del token
        identidad = {"username": usuario.username, "rol": usuario.rol}
        token_acceso = create_access_token(identity=identidad)

        return jsonify({"mensaje": "Login exitoso", "token": token_acceso}), 200
    
    return jsonify({"error": "Credenciales inválidas"}), 401

# --- NUEVA RUTA SOLICITADA EN LA IMAGEN ---
@api_bp.route('/productos', methods=['POST'])
@jwt_required() # BARRERA 1: Requiere Token válido
def crear_producto() -> tuple[Response, int]:
    # Extraemos la identidad (diccionario con username y rol)
    usuario_actual = get_jwt_identity()

    # BARRERA 2: Control de Acceso (RBAC) - Solo Admin
    if usuario_actual.get("rol") != "Admin":
        return jsonify({"error": "Forbidden: Se requieren privilegios de Administrador"}), 403
    
    try:
        payload = request.get_json()
        nuevo_producto = Producto(
            nombre=payload['nombre'],
            precio=payload['precio'],
            stock=payload.get('stock', 0)
        )
        
        db.session.add(nuevo_producto)
        db.session.commit()

        return jsonify({
            "mensaje": "Producto creado con éxito",
            "producto": nuevo_producto.serializar(),
            "creado_por": usuario_actual["username"]
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Error al crear producto", "detalle": str(e)}), 400

# Ruta adicional de ejemplo para listar usuarios
@api_bp.route('/usuarios', methods=['GET'])
def listar_usuarios() -> tuple[Response, int]:
    pagina = request.args.get('page', 1, type=int)
    paginacion = Usuario.query.paginate(page=pagina, per_page=10, error_out=False)
    resultado = [u.serializar() for u in paginacion.items]

    return jsonify({
        "pagina_actual": paginacion.page,
        "total_paginas": paginacion.pages,
        "usuarios": resultado
    }), 200
