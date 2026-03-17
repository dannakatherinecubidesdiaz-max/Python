import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# ___CAPA DE LÓGICA DE NEGOCIO  ___
class Producto:
    def __init__(self, id_: int, nombre: str, precio: float, stock: int):
        self.__id = id_
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Métodos de acceso (encapsulaciòn)
    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio,
            "stock": self.__stock
        }

    def actualizar_stock(self, cantidad: int):
        self.__stock += cantidad

# Gestor único de productos en memoria
class InventarioProductos:
    def __init__(self):
        self._productos: list[Producto] = []

    def agregar_producto(self, nombre: str, precio: float, stock: int) -> Producto:
        nuevo = Producto(len(self._productos) + 1, nombre, precio, stock)
        self._productos.append(nuevo)
        return nuevo

    def obtener_todos(self) -> list[dict]:
        return [p.to_dict() for p in self._productos]

gestor = InventarioProductos()

# ___CAPA DE TRANSPORTE (Controladores / Flask)___
@app.route('/api/productos', methods=['GET'])
def listar_productos() -> tuple[Response, int]:
    datos = gestor.obtener_todos()
    return jsonify({"total": len(datos), "productos": datos}), 200

@app.route('/api/productos', methods=['POST'])
def crear_producto() -> tuple[Response, int]:
    try:
        payload = request.get_json()
        nuevo = gestor.agregar_producto(payload["nombre"], payload["precio"], payload["stock"])
        return jsonify({"mensaje": "Producto creado", "data": nuevo.to_dict()}), 201
    except KeyError:
        return jsonify({"error": "JSON inválido, faltan campos"}), 400

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT", 5000)), debug=os.getenv("FLASK_DEBUG") == "1")