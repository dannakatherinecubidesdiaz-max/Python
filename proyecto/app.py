import os
from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
# Importamos la base de datos y las rutas
from models import db
from routes import api_bp

# 1. Cargar variables de entorno (.env)
load_dotenv()

# 2. Instanciar el Orquestador Central (App)
app = Flask(__name__)

# 3. Configuración de la App
# Usamos valores por defecto si no existen en el .env
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///defo')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'clave-insegura')

# 4. Ensamblar e Inicializar (Paso solicitado)
db.init_app(app)           # Ensambla el proyecto con el ORM
migrate = Migrate(app, db) # Motor de migraciones
jwt = JWTManager(app)      # Inicializa el motor de seguridad JWT

# 5. Registrar el Blueprint
# Esto conecta las rutas definidas en 'routes' con el prefijo /api
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == '__main__':
    # El archivo app.py arranca el servidor
    puerto = int(os.getenv('PORT', 5000))
    
    # Nota: getenv devuelve un string, por eso comparamos con 'true'
    modo_debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(port=puerto, debug=modo_debug)
