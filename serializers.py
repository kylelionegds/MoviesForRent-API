from datetime import timedelta, datetime

def director_from_web(**kwargs):
    return {
                "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
           }

def director_from_db(args):
    return {
                "id": args["id"],
                "nome_completo": args["nome_completo"],
           }

def name_diretor_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else "",

def genre_from_web(**kwargs):
    return {
                "nome": kwargs["nome"] if "nome" in kwargs else "",
           }

def name_genre_from_web(**kwargs):
    return kwargs["nome"] if "nome" in kwargs else "",

def genre_from_db(args):
    return {
                "id": args["id"],
                "nome": args["nome"],
           }

def movie_from_web(**kwargs):
    return {
                "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
                "ano": kwargs["ano"] if "ano" in kwargs else "",
                "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
                "preco": kwargs["preco"] if "preco" in kwargs else "",
                "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
                "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else "",
           }

def movie_from_db(args):
    return{
                "id": args["id"],
                "titulo": args["titulo"],
                "ano": args["ano"],
                "classificacao": args["classificacao"],
                "preco": str(args["preco"]),
                "diretores_id": args["diretores_id"],
                "generos_id": args["generos_id"],
          }

def title_movie_from_web(**kwargs):
    return kwargs["titulo"] if "titulo" in kwargs else ""

def user_from_web(**kwargs):
    return {
                "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
           }

def user_from_db(args):
    return {
                "id": args["id"],
                "nome_completo": args["nome_completo"],
                "CPF": args["CPF"],
           }

def name_user_from_web(**kwargs):
    return kwargs["nome_completo"] if "nome_completo" in kwargs else ""

def rent_from_web(**kwargs):
    return {
                "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
                "id_usuario": kwargs["id_usuario"] if "id_usuario" in kwargs else "",
           }

def rent_from_db(rent, data_inicio, data_fim):
    return {
                "id": rent["id"],
                "data_inicio": datetime.date(data_inicio).strftime("%d %B, %Y"),
                "data_fim": datetime.date(data_fim).strftime("%d %B, %Y"),
                "filmes_id": rent["filmes_id"],
                "id_usuario": rent["id_usuario"],

           }

def id_rent_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""

def payment_from_web(**kwargs):
    return{
                "tipo": kwargs["tipo"] if "tipo" in kwargs else "",
          }

def payment_from_db(pagamento, data):
    return {
                "id": pagamento["id"],
                "tipo": pagamento["tipo"],
                "status": pagamento["status"],
                "codigo_pagamento": pagamento["codigo_pagamento"],
                "valor": str(pagamento["valor"]),
                "data": datetime.date(data).strftime("%d %B, %Y"),
                "locacoes_id": pagamento["locacoes_id"],

           }
def id_payment_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""