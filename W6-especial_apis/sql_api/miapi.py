from flask import Flask, request
from flask import jsonify
from pandas.core.accessor import DirNamesMixin

# Importamos nuestros módulos de funciones
import tools.getdata as get 
import tools.postdata as pos

app = Flask(__name__)



@app.route("/")
def index():
    return "Hola mundo"


@app.route("/frases/<name>")
def frasespersonaje(name):
    print(name)
    frases = get.mensajepersonaje(name)
    return jsonify(frases)



@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    escena = request.form.get("scene")
    person = request.form.get("character_name")
    frase = request.form.get("dialogue")
    pos.metemensaje(escena,person, frase)
    return "Se ha insertado correctamente"











app.run()