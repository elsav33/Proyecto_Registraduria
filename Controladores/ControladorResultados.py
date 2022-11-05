from Modelos.Resultados import Resultados
from Modelos.Candidatos import Candidatos
from Modelos.Mesas import Mesas
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioMesas import RepositorioMesas


class ControladorResultados:
    def __init__(self):
        print("Creando Controlador de Resultados")
        self.repositorioResultados = RepositorioResultados()
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioMesas = RepositorioMesas()

    def crear(self, infoResultado, id_candidato, id_mesa):
        print("Crear Resultado")
        resultado = Resultados(infoResultado)
        candidato = Candidatos(self.repositorioCandidatos.findById(id_candidato))
        mesa = Mesas(self.repositorioMesas.findById(id_mesa))
        resultado.candidato = candidato
        resultado.mesa = mesa
        return self.repositorioResultados.save(resultado)

    def consultaResultado(self, id):
        print("Consulta Resultado con id: " + id)
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def consultarResultados(self):
        print("Consulta todas los resultados")
        return self.repositorioResultados.findAll()

    def actualizar(self, id, infoResultado, id_candidato, id_mesa):
        print("Actualizando un resultado con id: " + id)
        resultadoActual = Resultados(self.repositorioResultados.findById(id))
        resultadoActual.resultado = infoResultado["resultado"]
        candidato = Candidatos(self.repositorioCandidatos.findById(id_candidato))
        mesa = Mesas(self.repositorioMesas.findById(id_mesa))
        resultadoActual.candidato = candidato
        resultadoActual.mesa = mesa
        return self.repositorioResultados.save(resultadoActual)

    def eliminar(self, id):
        print("Eliminando un resultado con id: " + id)
        return self.repositorioResultados.delete(id)
