from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.pedidos.models import Pedido
from blueprintapp.clientes.models import Cliente
from blueprintapp.productos.models import Producto

bp_pedidos = Blueprint("bp_pedidos", __name__, template_folder="templates")

@bp_pedidos.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template("pedidos/index.html", pedidos=pedidos)

@bp_pedidos.route("/create", methods=["GET", "POST"])
def create():
    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == "POST":
        pedido = Pedido(
            fecha=request.form["fecha"],
            monto=request.form["monto"],
            cliente_id=request.form["cliente_id"],
            producto_id=request.form["producto_id"]
        )
        db.session.add(pedido)
        db.session.commit()
        return redirect(url_for("bp_pedidos.index"))

    return render_template("pedidos/create.html", clientes=clientes, productos=productos)

@bp_pedidos.route("/delete/<int:id>")
def delete(id):
    pedido = Pedido.query.get_or_404(id)
    db.session.delete(pedido)
    db.session.commit()
    return redirect(url_for("bp_pedidos.index"))