from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.clientes.models import Cliente

# blueprint de clientes
bp_clientes = Blueprint("bp_clientes", __name__, template_folder="templates")

# listar clientes
@bp_clientes.route("/")
def index():
    clientes = Cliente.query.all()
    return render_template("clientes/index.html", clientes=clientes)

# crear cliente
@bp_clientes.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        cliente = Cliente(
            nombre=request.form["nombre"],
            telefono=request.form["telefono"]
        )
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for("bp_clientes.index"))

    return render_template("clientes/create.html")

# editar cliente
@bp_clientes.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    cliente = Cliente.query.get_or_404(id)

    if request.method == "POST":
        cliente.nombre = request.form["nombre"]
        cliente.telefono = request.form["telefono"]
        db.session.commit()
        return redirect(url_for("bp_clientes.index"))

    return render_template("clientes/edit.html", cliente=cliente)

# eliminar cliente
@bp_clientes.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for("bp_clientes.index"))