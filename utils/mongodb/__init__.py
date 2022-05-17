import pymongo
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
DB = client['Escuelas']
collection = DB['Escuelas']

def getProvincias():
    result = collection.distinct('Jurisdicción')
    return result

def getAmbitos():
    result = collection.distinct("Ámbito")
    return result

def getSectores():
    result = collection.distinct('Sector')
    return result

def getProvinciasFull():
    collection = DB['Provincias']
    projection = {"_id": 0}
    result = list(collection.find({}, projection).sort('nombre', pymongo.ASCENDING))
    return result

def getProvinciaFull(id):
    collection = DB['Provincias']
    projection = {"_id": 0}
    result = list(collection.find({'id': id},projection))
    return result

Provincias = getProvinciasFull()
Pcias = getProvincias()
Ambitos = getAmbitos()
Sectores = getSectores()