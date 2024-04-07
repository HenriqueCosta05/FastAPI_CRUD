from bson.objectid import ObjectId
from typing import Dict, List
from datetime import timedelta
from models import Item
from NoSQL.connect_db import connection

# Inicializando a conexão com o MongoDB.
db = connection

#Método para criar um item no MongoDB (Create).
def create_item(item: Item) -> Dict:
    item_dict = item.dict()
    result = db["CRUD"].insert_one(item_dict)
    return {"_id": str(result.inserted_id)}

#Método para ler todos os itens do MongoDB (Read).
def get_all_items() -> List[Dict]:
    items = db["CRUD"].find()
    return [{**item, "_id": str(item["_id"])} for item in items]

#Método para atualizar um item no MongoDB (Update).
def update_item(id: str, item: Item) -> Dict:
    item_dict = item.dict()
    result = db["CRUD"].update_one({"_id": ObjectId(id)}, {"$set": item_dict})
    return {"modified_count": result.modified_count}

#Método para deletar um item no MongoDB (Delete).
def delete_item(id: str) -> Dict:
    result = db["CRUD"].delete_one({"_id": ObjectId(id)})
    return {"deleted_item": result.deleted_count}
    