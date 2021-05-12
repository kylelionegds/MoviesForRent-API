from flask import Flask, jsonify, request
from main import select_specific_rent, query
from models import *
from serializers import *
from validator import *
from datetime import datetime, timedelta
import uuid, random

app = Flask (__name__)


@app.route("/diretores/all", methods=["GET"])
def show_directors():
    return jsonify(select_director(""))

@app.route("/diretores/find", methods=["GET"])
def find_diretor():
    director = name_diretor_from_web(**request.args)
    directors = select_director(director)
    dir_from_db = [director_from_db(diretor) for diretor in directors]
    return jsonify(dir_from_db)

@app.route("/diretores", methods=["POST"])
def insrt_director():
    director = director_from_web(**request.json)
    if valid_director(**director):
        id_dir = insert_director(**director)
        created_director = get_director(id_dir)
        return jsonify(director_from_db(created_director))
    else:
        return jsonify({"erro": "diretor inválido!"})

@app.route("/diretores/alter/<int:id>", methods=["PATCH", "PUT"])
def alt_diretor(id):
    director = director_from_web(**request.json)
    if valid_director(**director):
        alter_director(id, **director)
        updated_director = get_director(id)
        return jsonify(director_from_db(updated_director))
    else:
        return jsonify({"erro":"diretor inválido!"})

@app.route("/diretores/clear/<int:id>", methods=["DELETE"])
def clear_diretores(id):
    try:
        delete_director(id)
        return "", 204
    except:
        return jsonify({"erro":"não é possivel excluir este diretor!"})

@app.route("/filmes", methods=["POST"])
def insrt_movie():
    movie = movie_from_web(**request.json)
    if valid_movie(**movie):
        id_movie = insert_movie(**movie)
        created_movie = get_movie(id_movie)
        return movie_from_db(created_movie)
    else:
        return jsonify({"erro":"filme inválido!"})

@app.route("/filmes/find", methods=["GET"])
def find_movies():
    movie_title = title_movie_from_web(**request.args)
    movies = select_movie(movie_title)
    filmes_from_db = [movie_from_db(movie) for movie in movies]
    return jsonify(filmes_from_db)

@app.route("/filmes/alter/<int:id>",methods=["PATCH", "PUT"])
def alt_movie(id):
    movie = movie_from_web(**request.json)
    if valid_movie(**movie):
        alter_movie(id, **movie)
        updated_movie = get_movie(id)
        return jsonify(movie_from_db(updated_movie))
    else:
        return jsonify({"erro":"filme inválido!"})

@app.route("/filmes/clear/<int:id>", methods=["DELETE"])
def clear_movie(id):
    try:
        delete_movie(id)
        return "", 204
    except:
        return jsonify({"erro":"não é possivel excluir esse filme!"})

@app.route("/generos", methods=["POST"])
def insrt_genre():
    genre = genre_from_web(**request.json)
    if valid_genre(**genre):
        id_genre = insert_genre(**genre)
        created_genre = get_genre(id_genre)
        return genre_from_db(created_genre)
    else:
        return jsonify({"erro": "genero inválido!"})

@app.route("/generos/find", methods=["GET"])
def find_genres():
    name_genre = name_genre_from_web(**request.args)
    generos = select_genre(name_genre)
    gen_from_db = [genre_from_db(genero) for genero in generos]
    return jsonify(gen_from_db)

@app.route("/generos/alter/<int:id>", methods=["PATCH", "PUT"])
def alt_genre(id):
    genre = genre_from_web(**request.json)
    if valid_genre(**genre):
        alter_genre(id, **genre)
        updated_genre = get_genre(id)
        return jsonify(genre_from_db(updated_genre))
    else:
        return jsonify({"erro":"genero inválido!"})

@app.route("/generos/clear/<int:id>", methods=["DELETE"])
def clear_genre(id):
    try:
        delete_genre(id)
        return "", 204
    except:
        return jsonify({"erro":"não é possivel excluir este gênero!"})

@app.route("/usuarios", methods=["POST"])
def insrt_user():
    user = user_from_web(**request.json)
    if valid_user(**user):
        id_user = insert_user(**user)
        created_user = get_user(id_user)
        return jsonify(user_from_db(created_user))
    else:
        return jsonify({"erro":"usuário inválido!"})

@app.route("/usuarios/find", methods=["GET"])
def find_user():
    f_name = name_user_from_web(**request.args)
    users = select_user(f_name)
    usrs_from_db = [user_from_db(user) for user in users]
    return jsonify(usrs_from_db)

@app.route("/usuarios/alter/<int:id>", methods=["PATCH", "PUT"])
def alt_user(id):
    user = user_from_web(**request.json)
    if valid_user(**user):
        alter_user(id, **user)
        updated_user = get_user(id)
        return jsonify(user_from_db(updated_user))
    else:
        return jsonify({"erro":"usuário inválido!"})

@app.route("/usuarios/clear/<int:id>", methods=["DELETE"])
def clear_user(id):
    try:
        delete_user(id)
        return "", 204
    except:
        return jsonify({"erro": "não é possível excluir este usuário!"})

@app.route("/locacoes", methods=["POST"])
def insrt_rent():
    rent = rent_from_web(**request.json['locacao'])
    pay_type = payment_from_web(**request.json['pagamento'])
    if valid_payment(**pay_type) and valid_rent(**rent):
        current_date = datetime.now()
        end_date = (current_date + timedelta(hours=48))
        id_rent = insert_rent(current_date, end_date, **rent)
        created_rent = get_rent(id_rent)
        status_options = ["aprovado", "em analise", "reprovado"]
        status = random.choice(status_options)
        payment_cod = str(uuid.uuid4())
        value = get_movie(rent["filmes_id"])["preco"]
        date = datetime.now()
        rent_id = select_specific_rent(rent["usuarios_id"])["id"]
        payment_id = insert_payment(pay_type["tipo"], status, payment_cod, value, date, rent_id)
        created_payment = get_payment(payment_id)
        return jsonify({"pagamento": payment_from_db(created_payment, date), "locação": rent_from_db(created_rent, current_date, end_date)})
    else:
        return jsonify({"erro": "não foi possível realizar locação!"})

@app.route("/locacoes/find", methods=["GET"])
def find_rent():
    rent_id = id_rent_from_web(**request.args)
    rents = select_rent(rent_id)
    rnts_from_db = [rent_from_db(id) for id in rents]
    return jsonify(rnts_from_db)

@app.route("/locacoes/filme/<int:id>", methods=["GET"])
def check_movie_rent_by_id(id):
    return jsonify(query(f"""SELECT locacoes.id, filmes.titulo, usuarios.nome_completo, data_inicio,
                         pagamento.status FROM locacoes
                         INNER JOIN filmes ON filmes.id = locacoes.filmes_id AND filmes_id = %s
                         INNER JOIN usuarios ON usuarios.id = locacoes.usuarios_id
                         INNER JOIN pagamento ON locacoes.id = pagamento.locacoes_id""", [id,]))

@app.route("/locacoes/alter/<int:id>", methods=["PATCH", "PUT"])
def alt_rent(id):
    rent = rent_from_web(**request.json)
    if valid_rent(**rent):
        alter_rent(id, **rent)
        updated_rent = get_rent(id)
        return jsonify(rent_from_db(updated_rent))
    else:
        return jsonify({"erro":"locação inválida!"})

@app.route("/locacoes/clear/<int:id>", methods=["DELETE"])
def clear_rent(id):
    try:
        delete_rent(id)
        return "", 204
    except:
        return jsonify({"erro":"impossível deletar esta locação!"})


@app.route("/pagamentos", methods=["POST"])
def insrt_payment():
    pymt = payment_from_web(**request.json)
    if valid_payment(**pymt):
        id_pay = insert_payment(**pymt)
        created_payment = get_payment(id_pay)
        return payment_from_db(created_payment)
    else:
        return jsonify({"erro":"pagamento inválido!"})

@app.route("/pagamentos/find", methods=["GET"])
def find_payment():
    payment_id = id_payment_from_web(**request.args)
    payments = select_payment(payment_id)
    pymts_from_db = [payment_from_db(id) for id in payments]
    return jsonify(pymts_from_db)

@app.route("/pagamentos/alter/<int:id>", methods=["PATCH", "PUT"])
def alt_payment(id):
    pymt = payment_from_web(**request.json)
    if valid_payment(**pymt):
        alter_payment(id, **pymt)
        updated_payment = get_payment(id)
        return jsonify(payment_from_db(updated_payment))
    else:
        return jsonify({"erro":"pagamento inválido!"})

@app.route("/pagamentos/clear/<int:id>", methods=["DELETE"])
def clear_payment(id):
    try:
        delete_payment(id)
        return "", 204
    except:
        return jsonify({"erro":"impossivel deletar esse pagamento!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)