from app import db
class Administrador(db.Model):
    __tablename__ = "administrador"
    id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    nome = db.Column(db.String(200))
    cpf = db.Column(db.String(11))
    senha = db.Column(db.String(60))
    email = db.Column(db.String(60))
    