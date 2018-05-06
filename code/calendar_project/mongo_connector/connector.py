import pymongo
import logging


class Connector:
    # TODO poner configuración de la conexión a mongo
    db = pymongo.MongoClient()['calendar_db']
    logging.basicConfig(filename="./logs/info.log", level=logging.INFO)

    @staticmethod
    def add_document(collection, document):
        return Connector.db[collection].insert(document)

    @staticmethod
    def find_document(collection, query):
        return Connector.db[collection].find_one(query)

    @staticmethod
    def delete_document(collection, document_id):
        return Connector.db[collection].update_one({id: document_id}, {"deleted": True})

    @staticmethod
    def update_document(collection, document_id, new_values):
        return Connector.db[collection].update_one({id: document_id}, new_values)
