import os


import os
import dotenv
import sqlalchemy as alch

dotenv.load_dotenv()

passw = os.getenv("pass_sql")
print(passw)
dbName="HP"

#me conecto con la base de datos 
connectionData=f"mysql+pymysql://root:admin@localhost/{dbName}"
engine = alch.create_engine(connectionData)