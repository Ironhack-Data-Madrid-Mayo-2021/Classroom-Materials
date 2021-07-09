from config.configuration import engine
import pandas as pd


def mensajepersonaje(person):
    query = f""" SELECT character_name, dialogue
FROM frases
WHERE character_name = "{person}"

"""
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient="records")