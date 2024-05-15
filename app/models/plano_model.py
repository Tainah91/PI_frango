from app import db

class Plano(db.Model):
    __tablename__ = "plano"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(200))