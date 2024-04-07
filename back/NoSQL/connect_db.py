from .db import MongoDBConnection

#Inicializando a conexão com o MongoDB.
db_connection = MongoDBConnection()
db_connection.connect_to_database()
connection = db_connection.get_db_connection()
print(connection)