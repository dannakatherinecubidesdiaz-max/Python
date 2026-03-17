from flask import Flask, request, jsonify, Response

app = Flask(__name__)
usuarios_db: list[dict]= []

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario()->tuple[Response, int]:
    #1. Extraemos el Paiload del body de la peticiòn HTTP
    datos_entrantes: dict = request.get_json()

    #2.Resiliencia: Validaciòn del contrado de datos
    if not datos_entrantes or "nombre" not in datos_entrantes:
        return jsonify({"error":"Falta el campo requerido 'nombre'"}), 400 #400
    
    #3.Procesamiento y guardado
    nuevo_usuario = {
        "id": len(usuarios_db) + 1,
        "nombre": datos_entrantes["nombre"],
        "rol":datos_entrantes.get("rol", "Usuario Estàndar")
    }
    usuarios_db.append(nuevo_usuario)

    #4.Retorno de confirmaciòn con còdigo 201(Created)
    return jsonify({"mensaje": "Usuario creado", "data": nuevo_usuario}), 201

if __name__=='__main__':
    app.run(debug=True)