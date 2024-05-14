from app import db

class Modulo(db.Model):
    __tablename__ = "modulo"
    id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    nome = db.Column(db.String(200))