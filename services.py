from main import app, request

from schema import *

@app.route("/", methods="GET")
def inicio_indice():
    pass

@app.route("/usuarios/login", methods="GET")
def usuarios_login():
    pass

@app.route("/usuarios/sair", methods="GET")
def usuarios_sair():
    pass

@app.route("/usuarios/cadastrar", methods="GET")
def usuarios_cadastrar():
    pass

@app.route("/admin/usuarios/cancelar", methods="GET")
def usuarios_cancelar():
    pass

@app.route("/minicurso", methods="GET")
def minicurso_indice():
    pass

@app.route("/admin/minicurso/cadastrar", methods="GET")
def minicurso_cadastrar():
    pass

@app.route("/minicurso/inscrever", methods="GET")
def minicurso_inscrever():
    pass
