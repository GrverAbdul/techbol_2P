#importando el app.py
from blueprintapp.app import create_app

#para crear la aplicacion con todas las carecteristicas que se hizo en app.py
flask_app = create_app()

if __name__ == "__main__":
    #ejecutar
    flask_app.run(debug=True)