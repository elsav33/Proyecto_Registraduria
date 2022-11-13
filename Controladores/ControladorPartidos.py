from Modelos.Partidos import Partidos
# from Modelos.Mesas import Mesas
# from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioPartidos import RepositorioPartidos


class ControladorPartidos():
    def __init__(self):
        print("Creando Controlador de Partidos")
        self.repositorioPartidos = RepositorioPartidos()
        # self.repositorioMesas = RepositorioMesas()

    def crear(self, infoPartido):
        print("Crea un partido")
        partido = Partidos(infoPartido)
        return self.repositorioPartidos.save(partido)

    def consultaPartido(self, id):
        print("Consulta el partido con id: " + id)
        elPartido = Partidos(self.repositorioPartidos.findById(id))
        return elPartido.__dict__

    def consultarPartidos(self):
        print("Consulta todos los partidos")
        return self.repositorioPartidos.findAll()

    def actualizar(self, id, infoPartido):
        print("Actualiza el partido con id: " + id)
        partidoActual = Partidos(self.repositorioPartidos.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.repositorioPartidos.update(id, partidoActual)

    def eliminar(self, id):
        print("Elimina el partido con id: " + id)
        return self.repositorioPartidos.delete(id)