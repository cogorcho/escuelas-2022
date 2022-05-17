from flask import Flask, Response
from flask_csp.csp import csp_header
from flask_cors import CORS
import utils.mongodb as mdb
import json
import utils.mongodb.datos as datos


app = Flask(__name__)
CORS(app)

@app.route('/')
@csp_header({'default-src':"'none'",'script-src':"'self'"})
def index():
    data = json.dumps(mdb.Provincias, ensure_ascii=False).encode("utf8")
    #return Response(data,  mimetype='application/json')
    return data

@app.route('/ambitos')
def ambitos():
    return Response(json.dumps(mdb.Ambitos, ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/sectores')
def sectores():
    return Response(json.dumps(mdb.Sectores, ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/pcias')
def pcias():
    return Response(json.dumps(mdb.Pcias, ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/provincias')
def provincias():
    return Response(json.dumps(mdb.getProvinciasFull(), ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/munisxprov/<id>')
def munisxprov(id):
    return Response(json.dumps(datos.getMunicipiosProvincia(id), ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/buscamuni/<token>')
def buscamuni(token):
    return Response(json.dumps(datos.searchMuni(token), ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/localidadesxprovincia/<id>')
def buscalocas(id):
    return Response(json.dumps(datos.getLocalidadesProvincia(id), ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/departamentosxprovincia/<id>')
def buscadeptos(id):
    return Response(json.dumps(datos.getDepartamentosxProvincia(id), ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/escuelas/<provid>')
def datosxprovincia(provid):
        return Response(json.dumps(datos.getEscuelasPorProvincias(provid), ensure_ascii=False).encode("utf8"),  mimetype='application/json')

@app.route('/escuelasxlocalidad/<codigo>')
def escuelasxlocalidad(codigo):
        return Response(json.dumps(datos.getEscuelasPorLocalidad(codigo), ensure_ascii=False).encode("utf8"),  mimetype='application/json')


@app.route('/escuela/<CUE>')
def escuela(CUE):
        esc = datos.getEscuela(CUE)
        esc['tiposeducacion'] = datos.getTiposEducacion(CUE)
        esc['niveles'] = datos.getNiveles(esc['tiposeducacion'])
        return Response(json.dumps(esc, ensure_ascii=False).encode("utf8"),  mimetype='application/json')
        
#fetch('http://localhost:5000/provincias', {mode: "no-cors"}).then(response => response.json()).then(data => console.log(data)).catch(rejected => {console.log(rejected);});