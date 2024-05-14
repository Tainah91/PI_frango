from app import db

class Tipo(db.Model):
    __tablename__ = "tipo"
    id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    nome = db.Column(db.String(60))
    