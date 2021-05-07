from main import *

"_____________________UPDATE_____________________"

def alter_diretor(set_chave, set_value,where_coluna, where_value): #rodando
    update("diretores", set_chave, set_value, where_coluna, where_value)

# alter_diretor(["id"], [33],"id", 11)

def alter_genero(set_chave, set_value,where_coluna, where_value): #rodando
    update("generos", set_chave, set_value, where_coluna, where_value)

#alter_genero(["id"], [115], "id", 20)

def alter_filme(set_chave, set_value,where_coluna, where_value): #rodando
    update("filmes", set_chave, set_value, where_coluna, where_value)

#alter_filme(["titulo"], ["Carros"], "id", 24)

def alter_usuario(set_chave, set_value,where_coluna, where_value): #rodando
    update("usuarios", set_chave, set_value, where_coluna, where_value)

#alter_usuario(["nome_completo"], ["Caio Espíndola Gonçalves Silva"], "CPF", "42885196831")

"_____________________INSERT_____________________"

def insert_diretor(id_, nome_):
    insert("diretores", ["id", "nome_completo"], [id_, nome_]) #rodando

def insert_genero(id_, nome_):
    insert("generos", ["id", "nome"], [id_, nome_]) #rodando

def insert_filme(id_, titulo_, ano_, classif_, preco_, dir_id, gen_id): #rodando
    insert\
    (
        "filmes",
        ["id", "titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
        [id_, titulo_, ano_, classif_, preco_, dir_id, gen_id]
    )

def insert_usuario(id_, nome_comp, cpf_):
    insert("usuarios", ["id", "nome_completo", "CPF"], [id_, nome_comp, cpf_]) #rodando


"_____________________DELETE_____________________"

def delete_diretor(where_column, where_value):
    delete("diretores", where_column, where_value)

#delete_diretor("id", 35)

def delete_genero(where_column, where_value):
    delete("generos", where_column, where_value)

def delete_filmes(where_column, where_value):
    delete("filmes", where_column, where_value)

def delete_usuario(where_column, where_value):
    delete("usuarios", where_column, where_value)

"_____________________SELECT_____________________"

