from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

cart_api = Blueprint("cart_api", __name__)

cart_car = db.Table("cart_car",
    db.Column("cart_id", db.Integer, db.ForeignKey("cart.id")),
    db.Column("car_id", db.Integer, db.ForeignKey("carro.id")),
    db.Column("qtd", db.Integer)
)

cart_moto = db.Table("cart_moto",
    db.Column("cart_id", db.Integer, db.ForeignKey("cart.id")),
    db.Column("moto_id", db.Integer, db.ForeignKey("moto.id")),
    db.Column("qtd", db.Integer)
)

class Cart(BaseModel):
    __tablename__ = "cart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantidade_itens = db.Column(db.Integer)
    carrinho_vazio = db.Column(db.Boolean, default=True)

    following_carro = db.relationship("Carro", secondary=cart_car, backref="f_carro")
    following_moto = db.relationship("Moto", secondary=cart_moto, backref="f_moto")
    
    user_id = db.Column(db.ForeignKey("user.id"))




