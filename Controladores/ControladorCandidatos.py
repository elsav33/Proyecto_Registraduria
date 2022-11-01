from Modelos.Candidatos import Candidatos
from Modelos.Partidos import Partidos
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioPartidos import RepositorioPartidos

class ControladorCandidatos():
    def __init__(self):
        print("Creando Controlador de Candidatos")
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioPartidos = RepositorioPartidos()

    def crear(self, infoCandidato):
        print("Crear un Candidato")
        candidato = Candidatos(infoCandidato)
        return self.repositorioCandidatos.save(candidato)

    def consultaCandidato(self, id):
        print("Consulta el Candidato con id: " + id)
        elCandidato = Candidatos(self.repositorioCandidatos.findById(id))
        return elCandidato.__dict__

    def consultarCandidatos(self):
        print("Consulta todos los candidatos")
        return self.repositorioCandidatos.findAll()

    def actualizar(self, id, infoCandidato):
        print("Actualizando el Candidato con id: " + id)
        candidatoActual = Candidatos(self.repositorioCandidatos.findById(id))
        if infoCandidato["cedula"] != "":
            candidatoActual.cedula = infoCandidato["cedula"]
        if infoCandidato["numero_resolucion"] != "":
            candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        if infoCandidato["nombre"] != "":
            candidatoActual.nombre = infoCandidato["nombre"]
        if infoCandidato["apellido"] != "":
            candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidatos.update(id, candidatoActual)

    def eliminar(self, id):
        print("Eliminando el candidato con id: " + id)
        return self.repositorioCandidatos.delete(id)

    # Relacion Partido y Candidato
    def asignaPartido(self, id, id_partido):
        candidato = Candidatos(self.repositorioCandidatos.findById(id))
        partidoActual = Partidos(self.repositorioPartidos.findById(id_partido))
        candidato.partido = partidoActual
        return self.repositorioCandidatos.save(candidato)