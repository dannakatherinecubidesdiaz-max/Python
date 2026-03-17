#1. Importamos la Clase principal del framework
from flask import Flask

#2. INSTANCIACIòN: Creamos el objeto servidor.
#__name__le dice a Flask dònde buscar los archivos internos del proyecto.
app = Flask(__name__)

#ENRUTAMIENTO: El decorador @ mapea una URL de red con una funciòn en RAM.
app.route('/',methods=['GET']) 
def home() ->str:
    """Funciòn que se ejecuta cuando el cliente hace GET a la raìz del sitio."""
    return"<h1> Sistema de Control Agroindustrial Activo<h1>"

#4. EJECUCIÒN DEL BUCLE DE ESCUCHA
if __name__=='__main__':
 #host='0.0.0.0' expone el servidor a todas las interfaces de tu red local
 # port= 5000 es el puerto TCP asignado. debug=True reinicia el server si hay
 app.run(host='0.0.0.0', port=5000, debug=True) 