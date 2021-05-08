def director_from_web(**kwargs):
    return\
        {
            "id": kwargs["id"] if kwargs["id"] else "",
            "nome_completo": kwargs["nome_completo"] if kwargs["nome_completo"] else "",
        }

def director_from_db(*args):
    return\
        {
            "id": args[0],
            "nome_completo": args[1]
        }