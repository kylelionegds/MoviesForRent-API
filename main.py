from mysql.connector import connect, Error

config_db = {
        "host":"localhost",
        "user":"root",
        "password":"root",
        "database":"locadora-teste",
    }

params = None

def query (sql, params = None):
    with connect(**config_db) as conn:
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            return cursor.fetchall()


def execute(sql, params = None):
    with connect(**config_db) as conn:
        with conn.cursor(dictionary=True) as cursor:
            cursor.execute(sql, params)
            conn.commit()
            return cursor.lastrowid

def delete(table_name, coluna, valor):
    execute(f"DELETE FROM {table_name} WHERE {coluna} = %s", (valor,))

def update(tabela, nome_chave, valor_chave, colunas, valores):
    sets = [f"{coluna} = %s" for coluna in colunas]
    return execute(f"""UPDATE {tabela} SET {",".join(sets)} WHERE {nome_chave} = %s""", valores + [valor_chave])

def select(table_name, chave=1, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM {table_name} WHERE {chave} = %s LIMIT {limit} offset {offset}""", (valor_chave, )) #verificar sintaxe no format

def select_like(table_name, chave=1, valor_chave=1, limit=100, offset=0):
    return query(f"""SELECT * FROM {table_name} WHERE {chave} LIKE %s LIMIT {limit} offset {offset}""", (f"%{valor_chave}%",))

def get_data(table_name, where_key, where_value):
    return query(f"""select * from {table_name} where {where_key} = %s""", (where_value,))

def insert(table_name, colunas, valores):
    return execute(f"""INSERT INTO {table_name} ({', '.join(colunas)}) values ({', '.join(['%s' for valor in valores])})""", valores)

#def create(nome_tabela, colunas):
    #list_tableColumns = []
    #for coluna, valor in colunas.items():
        #list_tableColumns.append(f"{coluna} {valor}")

    #sql_columns = ",".join(list_tableColumns)
    #execute(f"""CREATE TABLE {nome_tabela}
    #        (id int unsigned primary key not null auto_increment, {sql_columns})""")

#def add_column(nome_tabela, nome_coluna):
    #execute(f"alter table {nome_tabela} add column {nome_coluna} varchar(255)")