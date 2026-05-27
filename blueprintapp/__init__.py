# blueprintapp/app.py
# fabrica de aplicaciones flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# instancia global de la base de datos
db = SQLAlchemy()

# manejador de migraciones
migrate = Migrate()

def create_app():

    # crear aplicacion flask
    app = Flask(__name__, template_folder='templates')

    # configuracion sqlite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv_ventas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # iniciar extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # importar blueprints (desde sus rutas)
    from blueprintapp.clientes.routes import bp_clientes
    from blueprintapp.productos.routes import bp_productos
    from blueprintapp.pedidos.routes import bp_pedidos

    # registrar blueprints con prefijos
    app.register_blueprint(bp_clientes, url_prefix="/clientes")
    app.register_blueprint(bp_productos, url_prefix="/productos")
    app.register_blueprint(bp_pedidos, url_prefix="/pedidos")

    return app