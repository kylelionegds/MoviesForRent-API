from flask import Flask, jsonify, request
from main import query, execute
from models import *
from serializers import *

app = Flask (__name__)

@app.route("/create-director", methods=["POST"])
def cria_diretor():
    pass



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)