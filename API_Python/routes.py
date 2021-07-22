from flask import Flask

app = Flask("Youtube")

# primeira rota


@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"Olá": "mundo"}


@app.route("/checa/id", methods=["POST"])
def cadastraUsuario():

    return{"id": 0}

app.run()
