#Archivo: app.py
import os
from flask import Flask
from dotenv import load_dotenv
#1. Cargamos el archivo .env a la memoria del Sistema Operativo
load_dotenv()

#2. [INSTANCIACION]: Creamos el Orquestador Central
app = Flask(__name__)

#3. [ENCAPSULAMIENTO DE CONFIGURACIÒN]: Guardamos los secretos dentro de 'app'
#Si la variable no existe en el .env, usamos un valor fallback por seguridad.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI','sqlite:///defo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'clave-insegura')

#Agregar en app.py (Seccion de acoplamiento)
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

#[ACOPLAMIENTO]: Le pasamos el orquestador 'app' al ORM y utilidades
db.init_app(app)
migrate = Migrate(app, db)  #Motor de migraciones
jwt = JWTManager(app)       #Motor de seguridad JWT

#(En las siguientes fases conectaremos la Base de Datos y la Seguridad aqui)

if __name__=='__main__':
    #El archivo app.py es el ùnico que arranca el servidor 
    puerto = int(os.getenv('PORT', 5000))
    modo_debug = os.getenv('FLASK_DEBUG')== True
    app.run(port=puerto, debug=modo_debug)
    
from routes import api_bp

app.register_blueprint(api_bp, url_prefix='/api')