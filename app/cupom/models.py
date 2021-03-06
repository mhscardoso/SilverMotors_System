from app.extensions import db
from app.models import BaseModel
from flask import Blueprint

cupom_api = Blueprint("cupom_api", __name__)

class Cupom(BaseModel):
    __tablename__ = "cupom"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    desconto = db.Column(db.Float)
    codigo = db.Column(db.String(10))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
