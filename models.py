from main import select, select_like, update, delete, insert

"_____________________UPDATE_____________________"

#def alter_director(set_chave, set_value, where_coluna, where_value):
#    update("diretores", set_chave, set_value, where_coluna, where_value)

def alter_director(id_diretor, nome_completo):
    update("diretores", "id", id_diretor, ["nome_completo"], [nome_completo,])

def alter_genre(id_genre, nome): #rodando
    update("generos", "id", id_genre, ["nome"], [nome,])

def alter_movie(id_movie, titulo): #rodando
    update("filmes", id_movie, ["id"], [titulo,])

def alter_user(id_user, nome_completo): #rodando
    update("usuarios", id_user, ["id"], ["nome_completo"], [nome_completo,])

def alter_rent(id, data_inicio, data_fim, filmes_id, id_usuario):
    update("locacoes", "id", id, ["id", "data_inicio", "data_fim", "filmes_id", "id_usuario"],
           [id, data_inicio, data_fim, filmes_id, id_usuario,])

def alter_payment(id, tipo, status, codigo_pagamento, valor, data, locacoes_id):
    update("pagamentos", "id", id, ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
           [tipo, status, codigo_pagamento, valor, data, locacoes_id,])

"_____________________INSERT_____________________"

def insert_director(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo]) #rodando

def insert_genre(nome):
    return insert("generos", ["nome",], [nome,]) #rodando

def insert_movie(id, titulo, ano, classificacao, preco, diretores_id, generos_id): #rodando
    return insert("filmes", ["id", "titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"], [id, titulo, ano, classificacao, preco, diretores_id, generos_id,])

def insert_user(id, nome_completo, CPF):
    return insert("usuarios", ["id", "nome_completo", "CPF"], [id, nome_completo, CPF]) #rodando

def insert_rent(data_inicio, data_fim, filmes_id, id_usuario):
    return insert("locacoes", ["data_inicio", "data_fim", "filmes_id", "id_usuario"],
                  [data_inicio, data_fim, filmes_id, id_usuario])

def insert_payment(tipo, status, codigo_pagamento, valor, data, locacoes_id):
    return insert("pagamentos", ["tipo", "status", "codigo_pagamento", "valor", "data", "locacoes_id"],
                  [tipo, status, codigo_pagamento, valor, data, locacoes_id])

"_____________________DELETE_____________________"

def delete_director(key_value): #rodando
    delete("diretores", "id", key_value)

#delete_diretor("id", 35)

def delete_genre(key_value):
    delete("generos", "id", key_value)

def delete_movie(key_value):
    delete("filmes", "id", key_value)

def delete_user(key_value):
    delete("usuarios", "id", key_value)

def delete_rent(key_value):
    delete("locacoes", "id", key_value)

def delete_payment(key_value):
    delete("pagamentos", "id", key_value)

"_____________________SELECT_____________________"

def select_director(key_value): #rodando
    return select("diretores", "id", key_value)

def select_genre(key_value): #rodando
    return select_like("genero", "nome", key_value)

def select_movie(key_value): #rodando
    return select_like("filmes", "titulo", key_value)

def select_user(key_value): #rodando
    return select_like("usuarios", "nome_completo", key_value)

def select_rent(key_value): #rodando
    return select_like("locacoes", "id", key_value)

def select_payment(key_value): #rodando
    return select_like("pagamentos", "id", key_value)

#select_diretor(1, 1, 100, 0)

"_____________________GET_____________________"

def get_director(id_director):
    return select("diretores", "id", id_director)[0]

def get_movie(id_movie):
    return select("filmes", "id", id_movie)[0]

def get_genre(id_genre):
    return select("generos", "id", id_genre)[0]

def get_user(id_user):
    return select("usuarios", "id", id_user)[0]

def get_rent(id_rent):
    return select("locacoes", "id", id_rent)[0]

def get_payment(id_payment):
    return select("pagamentos", "id", id_payment)[0]


