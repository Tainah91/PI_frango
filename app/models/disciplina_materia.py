from app import db

class Disciplina_Materia(db.Model):
    __tablename__ = "Disciplina_Materia"
    id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    nome = db.Column (db.String(200))