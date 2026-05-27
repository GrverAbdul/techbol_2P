# modelo producto
from blueprintapp.app import db

class Producto(db.Model):

    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    # relacion uno a muchos con pedidos
    pedidos = db.relationship("Pedido",back_populates="producto",cascade="all, delete")