from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    def __init__(self, username=None, password=None):
        self.client = MongoClient('mongodb://%s:%s@localhost:54276/?authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    #create
    def create(self, data):
        if data is not None:
            data_create = self.database.animals.insert(data)
            return data_create
        else:
            raise Exception("Nothing to save, parameter empty.")

    #read
    def read(self, data):
        if data is not None:
            data_read = self.database.animals.find(data,{"_id":False})
            return data_read
        else: 
            raise Exception("Nothing to save, parameter empty.")
        
    
    #update 
    def update(self, query, data):
        if data is not None:
            data_update = self.database.animals.update_one(query, data)
            return data_update
        else:
            raise Exception("Nothing to save, parameter empty.")
            
        
    
    
    #delete
    def delete(self, data):
        if data is not None:
            data_delete = self.database.animals.delete_one(data)
            return data_delete
        else:
            raise Exception("Nothing to save, parameter empty.")
    
    
            

