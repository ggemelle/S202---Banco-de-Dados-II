from pymongo import MongoClient
from database import Database

class MotoristaDAO:
    def __init__(self, database: str, collection: str):
        self.db = Database(database, collection)

    def create_motorista(self, motorista):
        try:
            res = self.db.collection.insert_one(motorista)
            print(f"Motorista created: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista(self, filter=None):
        try:
            res = self.db.collection.find_one(filter)
            print(f"Motorista found: {res}")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, filter, upvalues):
        try:
            res = self.db.collection.update_one(filter, {"$set": upvalues})
            print(f"Motorista updated: {res.modified_count} document(s) modified")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, filter):
        try:
            res = self.db.collection.delete_one(filter)
            print(f"Motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None