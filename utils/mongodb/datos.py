from . import *
import re

Niveles = [
    {'Común' : 'NivelesComun'},
    {'Adultos':'NivelesAdultos'},
    {'Artística':'NivelesArtistica'},
    {'Especial':'NivelesEspecial'},
    {'Hospitalaria Domiciliaria':'NivelesHospitalaria'},
    {'Intercultural Bilingüe':'NivelesIntercultural'},
    {'Contexto de Encierro':'NivelesEncierro'}
]

"""
FUNCIONES:
    getDataProvinciaPorId(id):
    getDataProvinciaPorNombre(nombre):
    getMunicipiosProvincia(id):
    searchMuni(token):
    getEscuelasPorProvincias(jurisdiccion):
    getLocalidadesProvincia(id):
    getEscuela(CUE):
    getTiposEducacion(CUE):
    getNiveles(tipos):
    getDepartamentosxProvincia(id):
"""

def getDataProvinciaPorId(id):
    collection = DB['Provincias']
    query = {'id': id }
    result = list(collection.find(query,{'_id':0}))[0]
    return result

def getDataProvinciaPorNombre(nombre):
    collection = DB['Provincias']
    query = {'nombre': nombre }
    result = list(collection.find(query,{}))[0]
    return result

def getMunicipiosProvincia(id):
    collection = DB['Municipios']
    query = {'provincia.id': id }
    filter = { '_id':0, 'provincia.nombre': 1, 'nombre':1, 'centroide': 1}
    result = list(collection.find(query,filter).sort("nombre", pymongo.ASCENDING))
    return result

def searchMuni(token):
    collection = DB['Municipios']
    regx = re.compile(f"^{token}", re.IGNORECASE)
    query = {'nombre': regx}
    filter = {'_id':0, 'nombre': 1, 'provincia.nombre': 1, 'centroide':1}
    result = list(collection.find(query,filter).sort("nombre", pymongo.ASCENDING))
    return result

def getEscuelasPorProvincias(jurisdiccion):
    collection = DB['Escuelas']
    query = {'Jurisdicción': jurisdiccion}
    return list(collection.find(query,{'_id':0}).sort('nombre', pymongo.ASCENDING))

def getEscuelasPorLocalidad(codigo_localidad):
    collection = DB['Escuelas']
    query = {'Código localidad': codigo_localidad}
    return list(collection.find(query,{'_id':0}).sort('nombre', pymongo.ASCENDING))

def getLocalidadesProvincia(id):
    collection = DB['Localidades']
    query = {'provincia.id': id }
    filter = { '_id':0, 'provincia.nombre': 1, 'nombre':1, 'id': 1, 'centroide': 1}
    result = list(collection.find(query,filter).sort("nombre", pymongo.ASCENDING))
    return result

def getEscuela(CUE):
    collection = DB['Escuelas']
    query = {'CUE Anexo': CUE}
    return list(collection.find(query,{'_id':0}).sort('nombre', pymongo.ASCENDING))[0]

def getTiposEducacion(CUE):
    collection = DB['TiposEducacion']
    query = {'CUE Anexo': CUE}
    return list(collection.find(query,{'_id':0}).sort('nombre', pymongo.ASCENDING))[0]

def getNiveles(tipos):
    print('tipos',tipos)
    CUE = tipos['CUE Anexo']
    niveles = {}
    for k in tipos.keys():
        if k == 'CUE Anexo':
            continue
        if tipos[k] == 'SI':
            nivel = [ item for item in Niveles if k in item][0]
            collection = DB[nivel[k]]
            niveles[k] = list(collection.find({'CUE Anexo': CUE},{'_id':0}))
    return niveles

def getDepartamentosxProvincia(id):
    collection = DB['Departamentos']
    query = {'provincia.id': id }
    filter = { '_id':0, 'provincia.nombre': 1, 'nombre':1, 'centroide': 1}
    result = list(collection.find(query,filter).sort("nombre", pymongo.ASCENDING))
    return result