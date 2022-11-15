import bson
from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultados import Resultados
from bson import ObjectId


class RepositorioResultados(InterfaceRepositorio[Resultados]):

    # --- Repositorio Resultados Reportes

    def getReporteCandidatos(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "Total": {
                    "$sum": "$resultado"
                },
                "candidato": {
                    "$first": "$candidato"
                },
                "partido": {
                    "$first": "$partido"
                }
            }
        }
        query2 = {
            "$sort": {
                "Total": -1
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def getReporteCandidatosMesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": "$candidato",
                "Total": {
                    "$sum": "$resultado"
                },
                "candidato": {
                    "$first": "$candidato"
                },
                "partido": {
                    "$first": "$partido"
                }
            }
        }
        query3 = {
            "$sort": {
                "Total": -1
            }
        }
        pipeline = [query1, query2, query3]
        return self.queryAggregation(pipeline)

    def getReportePartidos(self):
        query1 = {
            "$group": {
                "_id": "$partido",
                "Total": {
                    "$sum": "$resultado"
                },
                "doc": {
                    "$first": "$partido"
                }
            }
        }
        query2 = {
            "$sort": {
                "Total": -1
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def getReportePartidosMesa(self, id_mesa):
        query1 = {
            "$match": {"mesa.$id": ObjectId(id_mesa)}
        }
        query2 = {
            "$group": {
                "_id": "$partido",
                "Total": {
                    "$sum": "$resultado"
                },
                "doc": {
                    "$first": "$partido"
                }
            }
        }
        query3 = {
            "$sort": {
                "Total": -1
            }
        }
        pipeline = [query1, query2, query3]
        return self.queryAggregation(pipeline)

    def getReporteMesas(self):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "Total": {
                    "$sum": "$resultado"
                },
                "doc": {
                    "$first": "$mesa"
                }
            }
        }
        query2 = {
            "$sort": {
                "Total": 1
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)

    def getReporteCongreso(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "SubTotal": {
                    "$sum": "$resultado"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        query2 = {
            "$sort": {
                "SubTotal": -1
            }
        }
        query3 = {
            "$limit": 15
        }
        query4 = {
            "$group": {
                "_id": {
                    "partido": "$doc.partido"
                },
                "count": {
                    "$sum": 1},

            "doc": {
                "$first": "$$ROOT"
            }
            }
        }
        query5 = {
            "$project": {
                "doc.doc.partido":1,
                "count": 1,
                "porcentaje": {
                    "$multiply": [{
                        "$divide": [100, 15]}, "$count"]
                }
            }
        }
        pipeline = [query1, query2, query3, query4, query5]
        return self.queryAggregation(pipeline)
