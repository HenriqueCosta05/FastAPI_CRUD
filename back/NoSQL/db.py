from pymongo import MongoClient

#Setup inicial do MongoDB
connection_string = "mongodb://development:password@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["fastapiCrud"]
collection = db_connection.get_collection("CRUD")


