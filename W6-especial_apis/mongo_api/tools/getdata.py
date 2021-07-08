from config.configuration import db, collection


def frases_personaje():
    query = {"character_name": "Minerva McGonagall"}
    frases =  list(collection.find(query, {"_id": 0}))
    return frases


def mensajes(nombre):
    query = {"character_name": f"{nombre}"}
    frases =  list(collection.find(query, {"_id": 0}))
    return frases


def personajes_all():
    query = list(collection.distinct("character_name"))
    return query


def frases_all():
    query = list(collection.find({}, {"_id":0}))
    return query