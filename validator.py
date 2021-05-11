def valid_director(nome_completo):

    if len(nome_completo) == 0:
        return False

    return True

def valid_user(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False

    if len(CPF) != 14:
        return False

    return True

def valid_genre(nome):
    if len(nome) == 0:
        return False

    return True

def valid_movie(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    if ano == 0:
        return False
    if len(classificacao) == 0:
        return False
    if len(preco) == 0:
        return False
    if len(diretores_id) == 0:
        return False
    if len(generos_id) == 0:
        return False

    return True

def valid_rent(data_inicio, data_fim, filmes_id, id_usuario):
    if data_inicio == 0:
        return False
    if data_fim == 0:
        return False
    if filmes_id == 0:
        return False
    if id_usuario == 0:
        return False

    return True

def valid_payment(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    if len(tipo) == 0:
        return False
    if len(status) == 0:
        return False
    if codigo_pagamento == 0:
        return False
    if valor == 0:
        return False
    if data == 0:
        return False
    if locacoes_id == 0:
        return False

    return True