from flask import Blueprint, render_template, request, redirect, url_for
from blueprintapp.app import db
from blueprintapp.productos.models import Producto

bp_productos = Blueprint("bp_productos", __name__, template_folder="templates")

@bp_productos.route("/")
def index():
    productos = Producto.query.all()
    return render_template("productos/index.html", productos=productos)

@bp_productos.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        producto = Producto(
            nombre=request.form["nombre"],
            precio=request.form["precio"],
            stock=request.form["stock"]
        )
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for("bp_productos.index"))

    return render_template("productos/create.html")

@bp_productos.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    producto = Producto.query.get_or_404(id)

    if request.method == "POST":
        producto.nombre = request.form["nombre"]
        producto.precio = request.form["precio"]
        producto.stock = request.form["stock"]
        db.session.commit()
        return redirect(url_for("bp_productos.index"))

    return render_template("productos/edit.html", producto=producto)

@bp_productos.route("/delete/<int:id>")
def delete(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for("bp_productos.index"))