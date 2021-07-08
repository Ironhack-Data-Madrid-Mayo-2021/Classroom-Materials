import collections
import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

dburl = os.getenv("URL")


print(dburl)
if not dburl:
    raise ValueError ("no tienes URL de mongodb")



# CONEXIÓN CON LA COLECCIÓN
client = MongoClient(dburl)
db = client.get_database()
collection = db["frases"]