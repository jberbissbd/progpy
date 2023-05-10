import os.path
import sqlite3
from os.path import dirname
from moduls.missatgeria import saber_missatgeria, blocs_missatge, criteri, competencia_missatge

encoding = 'utf-8'


class Lectorbbdd:
    """Classe per a determinar la ruta a utilitzar de la base de dades
    :parameter mode: 0 per a testing, 1 per a ús normal."""

    def __init__(self, mode: int):
        super().__init__()
        self.mode = mode
        self.ruta_arxiu_bbdd = os.path.abspath(dirname(dirname(__file__)))
        if mode == 0:
            self.ruta_arxiu_bbdd = os.path.abspath(dirname(self.ruta_arxiu_bbdd)) + "/tests/test.db"
        elif mode == 1:
            self.ruta_arxiu_bbdd = self.ruta_arxiu_bbdd + "/dades/dades.db"
        else:
            raise ValueError(
                "Mode del programa establert incorrectament, ha de ser 0 o 1")


class Connectorbbdd(Lectorbbdd):
    """Classe per a connectar amb la base de dades segons la ruta proporcionada per la classe Lectorbbdd
    :parameter mode: 0 per a testing i 1 per a ús normal"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode
        self.taula = None
        self.conexio = sqlite3.connect(Lectorbbdd(self.mode).ruta_arxiu_bbdd)
        self.cursor = self.conexio.cursor()


class Lectormateries(Connectorbbdd):
    """Classe per a obtenir una llista de totes les matèries de la base de dades
    :parameter mode: 0 per a testing i 1 per a ús normal"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode
        self.taula = "materia"

    def llistar_materies(self):
        """Funció que retorna una llista de totes les materies de la base de dades"""
        try:
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = self.cursor.fetchall()
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning("Error al obtenir la llista de materies:") from error

    def llistar_materies_completes(self):
        """Funció que retorna una llista de totes les materies completes (materia + curs) de la base de dades
        :returns: lista de tuples"""
        try:
            self.taula = "materia_completa"
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = self.cursor.fetchall()
            return resultat
        except Exception as tipus_error:
            raise Warning(
                "Error al obtenir la llista de materies completes:") from tipus_error

    def combinar_info_materies(self):
        """Retorna una llista amb totes les matèries de la base de dades combinada amb la informació de les taules
        relacionades
        :returns: lista de tuples, ValueError si no s'ha pogut obtenir la llista"""
        if self.llistar_materies() is not None and self.llistar_materies_completes() is not None:
            try:
                self.cursor.execute("SELECT matcomp_id, materia_nom,materia_id, nivell_nom, etapa_desc FROM "
                                    "materia, materia_completa, curs, nivell, etapa WHERE matcomp_mat = materia_id AND"
                                    " matcomp_curs = curs_id AND curs_nivell = nivell_id AND nivell_etapa = etapa_id")
                resultat_consulta = self.cursor.fetchall()
                self.cursor.close()
                if resultat_consulta is not None:
                    return resultat_consulta
            except sqlite3.OperationalError as error_basedades:
                raise ValueError(
                    "Error: No s'ha pogut obtenir la llista de materies.") from error_basedades


class Lectorsabers(Connectorbbdd):
    """Consulta la taula de sabers de la base de dades"""

    def __init__(self, mode: int):
        super().__init__(mode)

        self.taula = "sabers"

    def segons_bloc_materia(self, bloc_id: int, materia_id: int):
        """Consulta la taula de sabers de la base de dades, filtrada per bloc i materia
        :returns: lista de tuples, on cada fila conté l'id i la descripcio del saber corresponent"""
        try:
            ordre = f"SELECT DISTINCT sabers_id, sabers_desc FROM {self.taula}, mat_sabers WHERE sabers.sabers_bloc = ? AND \
                mat_sabers.matsaber_mat = ? AND mat_sabers.matsaber_id = sabers.sabers_id ORDER BY sabers.sabers_id ASC"
            self.cursor.execute(ordre, (bloc_id, materia_id))
            resultat_consulta = self.cursor.fetchall()
            self.cursor.close()
            # Formatem com a llista: [(id_saber, descripcio_saber), ...]
            sabers_llista = list(resultat_consulta)
            # Formatem com a missatge:
            sabers_missatge = [saber_missatgeria(
                saber[0], saber[1]) for saber in sabers_llista]
            return sabers_missatge
        except sqlite3.OperationalError as missatge_error:
            raise ValueError("Error:") from missatge_error


class Lectorsblocs(Connectorbbdd):

    """Consulta la taula de blocs de la base de dades"""
    def __init__(self, mode: int):
        """
        Initializes a new instance of the class.

        Args:
            mode (int): The mode to use for initialization.

        Returns:
            None
        """
        super().__init__(mode)
        self.id_materia = None
        self.taula = "blocs"

    def obtenir_blocs(self, id_materia: int):
        self.id_materia = id_materia
        if not isinstance(self.id_materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            ordre = f"SELECT DISTINCT bloc_id, bloc_text FROM {self.taula}, sabers, mat_sabers WHERE blocs.bloc_id = \
                sabers.sabers_bloc AND sabers.sabers_id = mat_sabers.matsaber_saber " \
                    f"AND mat_sabers.matsaber_mat = {self.id_materia} ORDER BY bloc_id ASC"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            self.cursor.close()
            if resultat_consulta is None:
                raise Warning("Matèria sense blocs assignats")
            dades_retorn = list(resultat_consulta)
            dades_retorn = sorted(dades_retorn, key=lambda x: x[0])
            dades_retorn = [list(element) for element in dades_retorn]
            blocs_missatgeria = [blocs_missatge(
                element[0], element[1], []) for element in dades_retorn]
            return blocs_missatgeria
        except sqlite3.OperationalError as missatge_error:
            raise ValueError(f"Error: {missatge_error}") from missatge_error


class Lectorcompetencies(Connectorbbdd):
    """Consulta la taula de competencies de la base de dades"""

    def obtenir_competencies_materia(self, materia_id: int):
        """Consulta la taula de competencies de la base de dades, filtrada per materia relacionada
        Parameters:
        materia_id: int, identificador de la materia a consultar
        Returns:
        lista de tuples, on cada fila conté l'id i la descripcio de la competencia corresponent
        Raises:
        ValueError si no s'ha pogut obtenir la llista de competencies de la materia
        Warning si no hi han competencies assignades
        """
        self.materia_id = materia_id
        if not isinstance(self.materia_id, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            ordre = f"SELECT DISTINCT competencies.competencia_id, competencies.competencia_num, " \
                    f"competencies.competencia_desc FROM competencies, compmat WHERE compmat.compmat_materia =" \
                    f" {self.materia_id} " \
                    f"AND compmat.compmat_competencia = competencies.competencia_id ORDER BY competencia_num ASC"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            self.cursor.close()
            if resultat_consulta is None:
                raise Warning("Matèria sense competencies assignats")
            dades_brut = list(resultat_consulta)
            dades_retorn = []
            for element in dades_brut:
                element = list(element)
                element.append([])
                dades_retorn.append(element)
            return dades_retorn
        except sqlite3.OperationalError as missatge_error:
            raise ValueError(f"Error: {missatge_error}") from missatge_error


class Lectorcriteris(Connectorbbdd):

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "critaval"

    def obtenir_criteris_materia(self, materia_id: int, competencia_id: int):
        """Consulta la taula de criteris de la base de dades, filtrada per materia relacionada
        Parameters:
        materia_id: int, identificador de la materia a consultar
        Returns:
        lista de tuples, on cada fila conté l'id i la descripcio de la criterium corresponent
        Raises:
        ValueError si no s'ha pogut obtenir la llista de criteris de la materia
        Warning si no hi han criteris assignades
        """
        self.materia_id = materia_id
        if not isinstance(self.materia_id, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            ordre = f"SELECT DISTINCT critaval.critaval_id, critaval.critaval_num, critaval.critaval_desc " \
                    f"FROM {self.taula}, matcomp_aval WHERE critaval.critaval_comp = {competencia_id} " \
                    f"AND matcomp_aval.matcompaval_mat = {materia_id} " \
                    f"AND matcomp_aval.matcompaval_crit = critaval.critaval_id" \
                # f"ORDER BY critaval.critaval_id ASC"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            self.cursor.close()
            if resultat_consulta is None:
                raise Warning("Matèria sense criteris assignats")
            dades_brut = list(resultat_consulta)
            dades_retorn = [criteri(element[0], element[1], element[2])
                            for element in dades_brut]
            return dades_retorn
        except sqlite3.OperationalError as missatge_error:
            raise ValueError(f"Error: {missatge_error}") from missatge_error


class InformadorMateria:
    """Obté tota la informació de  la matèria de la base de dades"""

    def __init__(self, mode: int):
        self.id_materia = None
        self.mode = mode

    def obtenir_blocssabers(self, id_materia: int):
        self.id_materia = id_materia
        if not isinstance(self.id_materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            # Obtenim els blocs de sabers:
            blocs_materia = Lectorsblocs(
                self.mode).obtenir_blocs(self.id_materia)
            # Els creuem amb els sabers:
            for element in blocs_materia:
                element.sabers_associats = Lectorsabers(
                    self.mode).segons_bloc_materia(element.id, self.id_materia)
            return blocs_materia
        except ValueError as error:
            raise ValueError("Error: No s'ha pogut obtenir els blocs de sabers.") from error

    def obtenir_criteris_materia(self, materia_id: int):
        self.materia_id = materia_id
        if not isinstance(self.materia_id, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            # Obtenim les competencies de la materia:
            competencies_materia = Lectorcompetencies(self.mode).obtenir_competencies_materia(materia_id)
            # Els creuem amb els criteris:
            for element in competencies_materia:
                element[3] = Lectorcriteris(
                    self.mode).obtenir_criteris_materia(materia_id, element[0])
            competencies_format = [competencia_missatge(element[0], element[1], element[2], element[3]) for element in
                                   competencies_materia]
            return competencies_format
        except ValueError as error:
            raise ValueError(
                "Error: No s'ha pogut obtenir els criteris de sabers.") from error

