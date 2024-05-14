from app import db

class Conteudo(db.Model):
    __tablename__ = "conteudo"
    id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    mapamental = db.Column(db.text)
    videoaula = db.Column(db.text)
    textos = db.Column(db.text)
    livrospdf = db.Column(db.text)
    resumos = db.Column(db.text)