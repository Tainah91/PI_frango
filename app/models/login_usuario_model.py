from app import db

class LogUsuario(db.Model):
    __tablename__ = "log_usuario"
    id = db.Column(db.Integer, primary_key= True,autoincrement=True)
    nome = db.Column(db.String(200),unique=True)
    datadenascimento = db.Column(db.Date)
    cpf = db.Column(db.String(11))
    email = db.Column(db.String(60))
    senha = db.Column(bd.String(60))
    fk_tipo_id = db.Column(db.Integer,db.ForeignKey('tipo.id'))
