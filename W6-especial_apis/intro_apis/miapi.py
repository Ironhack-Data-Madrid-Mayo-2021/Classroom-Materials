from flask import Flask
from tools.paraeldado import eldado 
import tools.datos as dat



app = Flask(__name__)


@app.route("/")
def index():
    return "Hola mundo"


@app.route("/datos")
def datos():
    return dat.datos_pepe()



@app.route("/dado")
def dado():
    return eldado()












app.run("0.0.0.0",5000, debug=True)
 