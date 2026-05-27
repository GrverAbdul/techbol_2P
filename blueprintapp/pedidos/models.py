# modelo pedido
from blueprintapp.app import db
class Pedido(db.Model):
    __tablename__ = "pedidos"

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    # clave foranea a producto
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"))
    # clave foranea a cliente
    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"))
    # relacion con producto
    producto = db.relationship(
        "Producto",
        back_populates="pedidos"
    )
    # relacion con cliente
    cliente = db.relationship(
        "Cliente",
        back_populates="pedidos"
    )