from Modelos.Mesas import Mesas
from Repositorios.RepositorioMesas import RepositorioMesas


class ControladorMesas():
    def __init__(self):
        print("Creando Controlador de Mesas")
        self.repositorioMesas = RepositorioMesas()

    def crear(self, infoMesa):
        print("Crear una Mesa")
        mesa = Mesas(infoMesa)
        return self.repositorioMesas.save(mesa)

    def consultaMesa(self, id):
        print("Consulta la Mesa con id: " + id)
        laMesa = Mesas(self.repositorioMesas.findById(id))
        return laMesa.__dict__

    def consultarMesas(self):
        print("Consulta todas las Mesas")
        return self.repositorioMesas.findAll()

    def actualizar(self, id, infoMesa):
        print("Actualizando la Mesa con id: " + id)
        mesaActual = Mesas(self.repositorioMesas.findById(id))
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesas.update(id, mesaActual)

    def eliminar(self, id):
        print("Eliminando la Mesa con id: " + id)
        return self.repositorioMesas.delete(id)