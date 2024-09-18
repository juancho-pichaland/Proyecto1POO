from flask import Flask, render_template, request, redirect, url_for
from models import Usuario, Receta, Planificacion, ListaCompras, Inventario
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/planificador", methods=["GET", "POST"])
def planificador():
    if request.method == "POST":
        
        pass
    return render_template("planificador.html", planificaciones=obtener_planificaciones())

@app.route("/lista_compras", methods=["GET", "POST"])
def lista_compras():
    if request.method == "POST":
        
        pass
    return render_template("lista_compras.html", listas=obtener_listas_compras())

@app.route("/inventario", methods=["GET", "POST"])
def inventario():
    if request.method == "POST":
        
        pass
    return render_template("inventario.html", inventarios=obtener_inventarios())

if __name__ == "__main__":
    app.run(debug=True)
