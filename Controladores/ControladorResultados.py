from Modelos.Resultados import Resultados
from Modelos.Candidatos import Candidatos
from Modelos.Mesas import Mesas
from Modelos.Partidos import Partidos
from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioCandidatos import RepositorioCandidatos
from Repositorios.RepositorioMesas import RepositorioMesas
from Repositorios.RepositorioPartidos import RepositorioPartidos



class ControladorResultados:
    def __init__(self):
        print("Creando Controlador de Resultados")
        self.repositorioResultados = RepositorioResultados()
        self.repositorioCandidatos = RepositorioCandidatos()
        self.repositorioMesas = RepositorioMesas()
        self.repositorioPartidos = RepositorioPartidos()

    def crear(self, infoResultado, id_candidato, id_mesa, id_partido):
        print("Crea Resultado")
        resultado = Resultados(infoResultado)
        candidato = Candidatos(self.repositorioCandidatos.findById(id_candidato))
        mesa = Mesas(self.repositorioMesas.findById(id_mesa))
        partido = Partidos(self.repositorioPartidos.findById(id_partido))
        resultado.candidato = candidato
        resultado.mesa = mesa
        resultado.partido = partido
        return self.repositorioResultados.save(resultado)

    def consultaResultado(self, id):
        print("Consulta Resultado con id: " + id)
        elResultado = Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__

    def consultarResultados(self):
        print("Consulta todas los resultados")
        return self.repositorioResultados.findAll()

    def actualizar(self, id, infoResultado, id_candidato, id_mesa, id_partido):
        print("Actualiza resultado con id: " + id)
        resultadoActual = Resultados(self.repositorioResultados.findById(id))
        resultadoActual.resultado = infoResultado["resultado"]
        candidato = Candidatos(self.repositorioCandidatos.findById(id_candidato))
        mesa = Mesas(self.repositorioMesas.findById(id_mesa))
        partido = Partidos(self.repositorioPartidos.findById(id_partido))
        resultadoActual.candidato = candidato
        resultadoActual.mesa = mesa
        resultadoActual.partido = partido
        return self.repositorioResultados.save(resultadoActual)

    def eliminar(self, id):
        print("Elimina resultado con id: " + id)
        return self.repositorioResultados.delete(id)

    # --- Controlador Resultados Reportes

    def ReporteCandidatos(self):
        print("Consulta votación por candidatos")
        return self.repositorioResultados.getReporteCandidatos()

    def ReporteCandidatosMesa(self, id_mesa):
        print("Consulta votación por candidato para mesa: " + id_mesa)
        return self.repositorioResultados.getReporteCandidatosMesa(id_mesa)

    def ReportePartidos(self):
        print("Consulta votación por partidos")
        return self.repositorioResultados.getReportePartidos()

    def ReportePartidosMesa(self, id_mesa):
        print("Consulta votación por partido para mesa: " + id_mesa)
        return self.repositorioResultados.getReportePartidosMesa(id_mesa)

    def ReporteMesas(self):
        return self.repositorioResultados.getReporteMesas()

    def ReporteCongreso(self):
        return self.repositorioResultados.getReporteCongreso()
