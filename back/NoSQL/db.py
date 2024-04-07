from pymongo import MongoClient

#Setup inicial de conexão com o MongoDB.

mongo_db_connection_info = {
    "HOST": "localhost",
    "PORT": "27017",
    "USER": "development",
    "PASSWORD": "password",
    "DB_NAME": "fastapiCrud"
}

class MongoDBConnection: 
    def __init__(self) -> None:
        self.__connection_string = 'mongodb://{}:{}@{}:{}/?authSource=admin'.format(
            mongo_db_connection_info["USER"],
            mongo_db_connection_info["PASSWORD"],
            mongo_db_connection_info["HOST"],
            mongo_db_connection_info["PORT"]
        )
        self.__database_name = mongo_db_connection_info["DB_NAME"]
        #Inicializando conexão com o MongoDB como vazia e depois substituíndo pelo client.
        self.__client = None
        self.__db_connection = None
        
    def connect_to_database(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]
        
    #Retornando a conexão com o MongoDB.
    def get_db_connection(self):
        return self.__db_connection
        
    #Retornando o client do MongoDB.
    def get_db_client(self):
        return self.__client