# pip install flask
from flask import Flask, request
from flask import jsonify
# pip install markdown 
import markdown.extensions.fenced_code

# IMPORTAMOS LOS MÓDULOS DE FUNCIONES PROPIOS
import tools.getdata as get
import tools.postdata as pos



app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extensions = ["fenced_code"]
    )
    return md_template




@app.route("/frases")
def frases():
    frases = get.frases_personaje()
    return jsonify(frases)


@app.route("/frases_todas")
def frases_todas():
    frases = get.frases_all()
    return jsonify(frases)

@app.route("/personajes")
def personajes():
    personajes = get.personajes_all()
    return jsonify(personajes)


@app.route("/frases/<name>")
def frasespersonaje(name):
    frases = get.mensajes(name)
    return jsonify(frases)

# VAMOS A UTILIZAR REQUEST.FORM.GET PARA RECIBIR PARÁMETROS
# REALIZAREMOS ENDPOINTS DE TIPO POST


@app.route("/nuevafrase", methods=["POST"])
def insertamensaje():
    escena = request.form.get("scene")
    personaje = request.form.get("character_name")
    frase = request.form.get("dialogue")
    pos.insertamensaje (escena,personaje,frase)
    return "Se ha insetado el mensaje en la base de datos"



#Endpoint anterior refactorizado
@app.route("/nuevafrase2", methods=["POST"])
def nuevafrase_2():
    diccionario =  {"scene": request.form.get("escena"),
    "character_name": request.form.get("nombre"),
    "dialogue": request.form.get("diálogo")
    }
    respuesta = pos.insertamensaje2(diccionario)
    return respuesta










app.run("0.0.0.0", 5000, debug=True)