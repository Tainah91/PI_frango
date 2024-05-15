from app import db

class Pagamento(db.Model):
    __tablename__ = "pagamento"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    boleto = db.Column(db.String(200))
    pix = db.Column (db.String(200))