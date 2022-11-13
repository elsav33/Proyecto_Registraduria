from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPartidos import ControladorPartidos
from Controladores.ControladorMesas import ControladorMesas
from Controladores.ControladorCandidatos import ControladorCandidatos
from Controladores.ControladorResultados import ControladorResultados
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://elsav:MisionTIC2022@cluster0.0dpgjmb.mongodb.net/bd_registro_web?retryWrites=true&w=majority")
db = client.test

print(db)

baseDatos = client['bd_registro_web']
print(baseDatos.list_collection_names())

app = Flask(__name__)
cors = CORS(app)

miControladorPartidos = ControladorPartidos()
miControladorMesas = ControladorMesas()
miControladorCandidatos = ControladorCandidatos()
miControladorResultados = ControladorResultados()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json['mensaje'] = "Servidor corriendo correctamente..."
    return jsonify(json)


# Aquí los partidos

@app.route("/partidos", methods=['POST'])
def CrearPartido():
    datos = request.get_json()
    respuesta = miControladorPartidos.crear(datos)
    return jsonify(respuesta)


@app.route("/partidos", methods=['GET'])
def MostrarPartidos():
    respuesta = miControladorPartidos.consultarPartidos()
    return jsonify(respuesta)


@app.route("/partidos/<string:id>", methods=['GET'])
def MostrarPartido(id):
    respuesta = miControladorPartidos.consultaPartido(id)
    return jsonify(respuesta)


@app.route("/partidos/<string:id>", methods=['PUT'])
def ActualizarPartido(id):
    datos = request.get_json()
    respuesta = miControladorPartidos.actualizar(id, datos)
    return jsonify(respuesta)


@app.route("/partidos/<string:id>", methods=['DELETE'])
def EliminarPartido(id):
    respuesta = miControladorPartidos.eliminar(id)
    return jsonify(respuesta)


# Aquí las mesas

@app.route("/mesas", methods=['POST'])
def CrearMesa():
    datos = request.get_json()
    respuesta = miControladorMesas.crear(datos)
    return jsonify(respuesta)


@app.route("/mesas", methods=['GET'])
def MostrarMesas():
    respuesta = miControladorMesas.consultarMesas()
    return jsonify(respuesta)


@app.route("/mesas/<string:id>", methods=['GET'])
def MostrarMesa(id):
    respuesta = miControladorMesas.consultaMesa(id)
    return jsonify(respuesta)


@app.route("/mesas/<string:id>", methods=['PUT'])
def ActualizarMesa(id):
    datos = request.get_json()
    respuesta = miControladorMesas.actualizar(id, datos)
    return jsonify(respuesta)


@app.route("/mesas/<string:id>", methods=['DELETE'])
def EliminarMesa(id):
    respuesta = miControladorMesas.eliminar(id)
    return jsonify(respuesta)


# Aquí los Candidatos

@app.route("/candidatos", methods=['POST'])
def CrearCandidato():
    datos = request.get_json()
    respuesta = miControladorCandidatos.crear(datos)
    return jsonify(respuesta)


@app.route("/candidatos", methods=['GET'])
def MostrarCandidatos():
    respuesta = miControladorCandidatos.consultarCandidatos()
    return jsonify(respuesta)


@app.route("/candidatos/<string:id>", methods=['GET'])
def MostrarCandidato(id):
    respuesta = miControladorCandidatos.consultaCandidato(id)
    return jsonify(respuesta)


@app.route("/candidatos/<string:id>", methods=['PUT'])
def ActualizarCandidato(id):
    datos = request.get_json()
    respuesta = miControladorCandidatos.actualizar(id, datos)
    return jsonify(respuesta)


@app.route("/candidatos/<string:id>", methods=['DELETE'])
def EliminarCandidato(id):
    respuesta = miControladorCandidatos.eliminar(id)
    return jsonify(respuesta)


# Relacion Partido y Candidato --- ya no se va a usar porque se creó la referencia manualmente
"""@app.route("/candidatos/<string:id>/partidos/<string:id_partido>", methods=['PUT'])
def asignaPartido(id, id_partido):
    respuesta = miControladorCandidatos.asignaPartido(id, id_partido)
    return jsonify(respuesta)"""


# Aquí los Resultados

@app.route("/resultados/candidatos/<string:id_candidato>/mesas/<string:id_mesa>/partidos/<string:id_partido>",
           methods=['POST'])
def CrearResultado(id_candidato, id_mesa, id_partido):
    datos = request.get_json()
    respuesta = miControladorResultados.crear(datos, id_candidato, id_mesa, id_partido)
    return jsonify(respuesta)


@app.route("/resultados", methods=['GET'])
def MostrarResultados():
    respuesta = miControladorResultados.consultarResultados()
    return jsonify(respuesta)


@app.route("/resultados/<string:id>", methods=['GET'])
def MostrarResultado(id):
    respuesta = miControladorResultados.consultaResultado(id)
    return jsonify(respuesta)


@app.route(
    "/resultados/<string:id>/candidatos/<string:id_candidato>/mesas/<string:id_mesa>/partidos/<string:id_partido>",
    methods=['PUT'])
def ActualizarResultado(id, id_candidato, id_mesa, id_partido):
    datos = request.get_json()
    respuesta = miControladorResultados.actualizar(id, datos, id_candidato, id_mesa, id_partido)
    return jsonify(respuesta)


@app.route("/resultados/<string:id>", methods=['DELETE'])
def EliminarResultado(id):
    respuesta = miControladorResultados.eliminar(id)
    return jsonify(respuesta)


# Aquí los Reportes

@app.route("/resultados/resultadosCandidatos", methods=['GET'])
def resultadosCandidatos():
    respuesta = miControladorResultados.ReporteCandidatos()
    return jsonify(respuesta)


@app.route("/resultados/resultadosCandidatosMesa/<string:id_mesa>", methods=['GET'])
def resultadosCandidatosMesa(id_mesa):
    respuesta = miControladorResultados.ReporteCandidatosMesa(id_mesa)
    return jsonify(respuesta)


@app.route("/resultados/resultadosPartidos", methods=['GET'])
def resultadosPartidos():
    respuesta = miControladorResultados.ReportePartidos()
    return jsonify(respuesta)


@app.route("/resultados/resultadosPartidosMesa/<string:id_mesa>", methods=['GET'])
def resultadosPartidosMesa(id_mesa):
    respuesta = miControladorResultados.ReportePartidosMesa(id_mesa)
    return jsonify(respuesta)


@app.route("/resultados/resultadosMesas", methods=['GET'])
def resultadosMesas():
    respuesta = miControladorResultados.ReporteMesas()
    return jsonify(respuesta)


@app.route("/resultados/resultadosCongreso", methods=['GET'])
def resultadosCongreso():
    respuesta = miControladorResultados.ReporteCongreso()
    return jsonify(respuesta)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("servidor " + dataConfig['url-backend'] + " puerto " + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
