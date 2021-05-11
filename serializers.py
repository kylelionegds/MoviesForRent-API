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
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
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
        "data_inicio": kwargs["data_inicio"] if "data_inicio" in kwargs else "",
        "data_fim": kwargs["data_fim"] if "data_fim" in kwargs else "",
        "filmes_id": kwargs["filmes_id"] if "filmes_id" in kwargs else "",
        "id_usuario": kwargs["id_usuario"] if "id_usuario" in kwargs else "",
    }

def rent_from_db(args):
    return {
        "id": args["id"],
        "data_inicio": args["data_inicio"],
        "data_fim": args["data_fim"],
        "filmes_id": args["filmes_id"],
        "id_usuario": args["id_usuario"],

    }

def id_rent_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""

def payment_from_web(**kwargs):
    return{
        "tipo": kwargs["tipo"] if "tipo" in kwargs else "",
        "status": kwargs["status"] if "status" in kwargs else "",
        "codigo_pagamento": kwargs["codigo_pagamento"] if "codigo_pagamento" in kwargs else "",
        "valor": kwargs["valor"] if "valor" in kwargs else "",
        "data": kwargs["data"] if "data" in kwargs else "",
        "locacoes_id": kwargs["locacoes_id"] if "locacoes_id" in kwargs else "",
    }

def payment_from_db(args):
    return {
        "id": args["id"],
        "tipo": args["tipo"],
        "status": args["status"],
        "codigo_pagamento": args["codigo_pagamento"],
        "valor": str(args["valor"]),
        "data": args["data"],
        "locacoes_id": args["locacoes_id"],

    }
def id_payment_from_web(**kwargs):
    return kwargs["id"] if "id" in kwargs else ""