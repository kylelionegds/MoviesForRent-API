from flask import Flask, jsonify, request
from main import select
from models import *
from serializers import *
from validator import *

app = Flask (__name__)

@app.route("/diretores", methods=["GET"])
def show_directors():
    return jsonify(select_diretor("ing"))

@app.route("/diretores", methods=["POST"])
def create_director():
    director = director_from_web(**request.json)
    if valid_director(**director):
        insert_diretor(**director)
        created_director = get_director(director["nome_completo"])
        return jsonify(director_from_db(created_director))
    else:
        jsonify({"erro": "diretor inválido!"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)