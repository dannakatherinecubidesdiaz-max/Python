#Archivo: models.py
from flask_sqlalchemy import SQLAlchemy
#Instanciamos la herramienta vacia. Se acoplara a 'app' màs adelante.
db=SQLAlchemy()

#[HERENCIA]: La clase 'Usuario' hereda todo el poder de 'db.Model'
class Usuario(db.Model):
    __tablename__= 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)

    #[ENCAPSULAMIENTO]: Nunca guardamos el password real, solo su representaciòn
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.String(20), default='Operario')

    #[POLIMORFISMO]: Metodo propio para transformar el objeto a JSON 
    def serializar(self)->dict:
        return{
            "id": self.id,
            "username": self.username,
            "rol": self.rol
        }
    