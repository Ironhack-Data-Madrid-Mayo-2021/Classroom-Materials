from config.configuration import collection

def insertamensaje(escena, personaje,frase):
    dic_insertar = {"scene": escena,
    "character_name": personaje,
    "dialogue": frase
    }
    collection.insert_one(dic_insertar)


#Esta función es como la anterior pero ya recibe un diccionario
def insertamensaje2(diccionario):
    """
    Función que inserta un documento en la base de datos
    """
    collection.insert_one(diccionario)
    return f"Se han introducido los siguientes datos {diccionario}"