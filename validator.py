def valid_director(nome_completo):

    if len(nome_completo) == 0:
        return False

    return True

def valid_user(nome_completo):
    if len(nome_completo) == 0:
        return False

    return True

def valid_genre(nome):
    if len(nome) == 0:
        return False

    return True

def valid_movie(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if len(titulo) == 0:
        return False
    if len(str(ano)) == 0:
        return False
    if len(str(classificacao)) == 0:
        return False
    if len(str(preco)) == 0:
        return False
    if len(str(diretores_id)) == 0:
        return False
    if len(str(generos_id)) == 0:
        return False

    return True

def valid_rent(data_inicio, data_fim, filmes_id, id_usuario):
    if len(str(data_inicio)) == 0:
        return False
    if len(str(data_fim)) == 0:
        return False
    if len(str(filmes_id)) == 0:
        return False
    if len(str(id_usuario)) == 0:
        return False

    return True

def valid_payment(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    if len(tipo) == 0:
        return False
    if len(status) == 0:
        return False
    if len(str(codigo_pagamento)) == 0:
        return False
    if len(str(valor)) == 0:
        return False
    if len(str(data)) == 0:
        return False
    if len(str(locacoes_id)) == 0:
        return False

    return True