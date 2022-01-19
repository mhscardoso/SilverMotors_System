from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

user_api = Blueprint("user_api", __name__)

class User(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    cpf = db.Column(db.String(14))
    email = db.Column(db.String(30))
    telefone = db.Column(db.String(11))
    nascimento = db.Column(db.DateTime)

    user_cart = db.relationship("Cart", backref="user", uselist=False)
    user_cupom = db.relationship("Cupom", backref="user")

    def json(self):
        return {
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "nascimento": self.nascimento
        }

