from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados
from bson import ObjectId

# De aquí para abajo en construcción
class RepositorioResultados(InterfaceRepositorio[Resultados]):

    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    # esta es mi prueba

    def getListadoMesasCandidatos(self):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def getListadoResultadosCandidato(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "total":{
                    "$sum": "$resultado"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

    def getMayorVotosxMesa(self):
        query1 = {
            "$group": {
                "_id": "$candidatos",
                "total": {
                    "$sum": "$resultado"
                }
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)

    def getPromedioVotosxPartido(self, id_partido):
        query1 = {
            "$match": {"partidos.$id": ObjectId(id_partido)}
        }
        query2 = {
            "$group": {
                "_id": "$partidos",
                "promedio": {
                    "$avg": "$votos"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)
