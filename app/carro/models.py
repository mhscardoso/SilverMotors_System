from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

carro_api = Blueprint("carro_api", __name__)

class Carro(BaseModel):
    __tablename__ = "carro"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    placa = db.Column(db.String(7))
    modelo = db.Column(db.String(15))
    cor = db.Column(db.String(15))
    ano = db.Column(db.String(4))
    preco = db.Column(db.Float)

    def json(self):
        return {
            "placa": self.placa,
            "modelo": self.modelo,
            "cor": self.cor,
            "ano": self.ano,
            "preco": self.preco
        }
