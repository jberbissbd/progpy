import os.path
import sqlite3
from os.path import dirname
import itertools

from missatgeria import (blocs_missatge,
                         competencia_missatge, criteri_missatge,
                         Saber, Curs_missatge, Transversals, Materia, Curriculum)

encoding = 'utf-8'

"""Module per a connectar amb la base de dades segons la ruta proporcionada per la classe Lectorbbdd"""


class Lectorbbdd:
    """Classe per a determinar la ruta a utilitzar de la base de dades
    :parameter mode: 0 per a testing, 1 per a ús normal."""

    def __init__(self, mode: int):
        super().__init__()
        self.mode = mode
        self.ruta_arxiu_bbdd = os.path.normpath(os.path.abspath(dirname(dirname(__file__))))
        if mode == 0:
            self.ruta_arxiu_bbdd = os.path.normpath(
                os.path.abspath(dirname(dirname(self.ruta_arxiu_bbdd))) + "/tests/test.db")
        elif mode == 1:
            self.ruta_arxiu_bbdd = os.path.normpath(self.ruta_arxiu_bbdd + "/dades/dades.db")
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
    """Classe per a obtenir una llista de totes les matèries de la base de
    dades
    :parameter mode: 0 per a testing i 1 per a ús normal"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode
        self.taula = "materia"

    def llistar_materies(self):
        """Funció que retorna una llista de totes les materies de la base de
        dades"""
        try:
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = self.cursor.fetchall()
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning("Error al obtenir la llista de materies:") from error


class LectorCursos(Connectorbbdd):

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode
        self.taula = "curs"

    def obtenir_descripcio(self, curs_id: int):
        """Retorna el curs de la base de dades"""
        try:
            consulta_descripcio = "SELECT curs.curs_id, etapa.etapa_desc, nivell.nivell_nom,\
                                curs_modalitat FROM etapa, nivell, curs \
                                WHERE nivell.nivell_etapa = etapa.etapa_id \
                                AND curs.curs_nivell = nivell.nivell_id AND curs.curs_id = ?"
            self.cursor.execute(consulta_descripcio, (curs_id,))
            resultat_consulta = list(itertools.chain(*self.cursor.fetchall()))
            if len(resultat_consulta) == 0:
                raise ValueError("No s'ha pogut obtenir la descripció del curs")
            if resultat_consulta[3] is None:
                resultat = Curs_missatge(resultat_consulta[0], resultat_consulta[2]+" " + resultat_consulta[1])
            else:
                resultat = Curs_missatge(resultat_consulta[0], resultat_consulta[2] + " " + 
                                         resultat_consulta[1] + " - "+ resultat_consulta[3])
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning from error


class LectorMateriesCompletes(Connectorbbdd):
    """Classe per a obtenir una llista de totes les matèries de la base de
    dades
    :parameter mode: 0 per a testing i 1 per a ús normal"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode
        self.taula = "materia_completa"

    def obtenir_curs_materia(self, materia):
        """Retorna el curs correponent a la matèria"""
        try:
            ordre = "SELECT DISTINCT materia_completa.matcomp_curs from  materia_completa \
                    WHERE materia_completa.matcomp_id = ?"
            self.cursor.execute(ordre, (materia,))
            curs = self.cursor.fetchall()[0][0]
            
        except sqlite3.OperationalError as exc:
            raise Warning from exc
        return curs

    def obtenir_noms_materies(self, materia_consultar):
        """Retorna una llista amb totes les matèries de la base de dades"""
        try:
            ordre_obtenir_noms_materia = "SELECT materia.materia_nom FROM materia, materia_completa \
                                WHERE materia.materia_id = materia_completa.matcomp_mat AND \
                                materia_completa.matcomp_id = ?"
            self.cursor.execute(ordre_obtenir_noms_materia, (materia_consultar,))
            resultat = self.cursor.fetchall()[0][0]
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning("Error al obtenir la llista de materies:") from error
    
    def obtenir_materies(self):
        """Funció que retorna una llista de totes les materies completes
        (materia + curs) de la base de dades
        :returns: lista de tuples"""
        try:
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = self.cursor.fetchall()
            
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning("Error al obtenir la llista de materies:") from error

    def combinar_info_materies(self):
        """Retorna una llista amb totes les matèries de la base de dades combinada amb la informació de les taules
        relacionades
        :returns: lista de tuples, ValueError si no s'ha pogut obtenir la llista"""
        try:
            ordre = f"SELECT DISTINCT materia_completa.matcomp_id, materia.materia_nom, \
                    etapa.etapa_desc, materia_tipus.materia_tipus_text,materia_tipus.materia_tipus_id,\
                    nivell.nivell_nom,curs.curs_id, curs.curs_modalitat \
                    FROM {self.taula}, materia, curs, nivell, etapa, materia_tipus \
                    WHERE materia_completa.matcomp_curs = curs.curs_id AND materia.materia_id = " \
                    f"materia_completa.matcomp_mat\
                    AND nivell.nivell_id = curs.curs_nivell AND nivell.nivell_etapa = etapa.etapa_id \
                    AND materia_tipus.materia_tipus_id = materia.materia_tipus \
                    ORDER BY curs.curs_id ASC"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            
            return resultat_consulta
        except sqlite3.OperationalError as exc:
            raise ValueError("Error: nom de taula incorrecte o taula no existent") from exc

    def transversals_curs(self, materia: int):
        """Retorna els id's de les matèries transversals corresponents a una mtaèria,
        segons el curs de la matèria consultada"""
        if not isinstance(materia, int):
            raise TypeError("Cal proporcionar un nombre per a obtenir les matèries transversals")
        # Obtenim el curs de la matèria consultada:
        curs = self.obtenir_curs_materia(materia)
        transversals = []
        # Obtenim els id's de les matèries transversals:
        try:

            ordre_transversals = "SELECT DISTINCT MATERIA_COMPLETA.matcomp_id from MATERIA, \
                                    materia_completa WHERE materia.materia_tipus = 2 \
                                    AND materia_completa.matcomp_curs = ? \
                                    AND materia.materia_id = materia_completa.matcomp_mat"
            self.cursor.execute(ordre_transversals, (curs,))
            elements = itertools.chain(*self.cursor.fetchall())                
            elements_nous = [element for element in elements if element not in transversals]
            transversals.extend(elements_nous)
            return transversals
        except sqlite3.OperationalError as exc:
            raise Warning from exc


class Lectorsabers(Connectorbbdd):
    """Consulta la taula de sabers de la base de dades"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "sabers"

    def segons_bloc_materia(self, bloc_id: int, materia_id: int):
        """Consulta la taula de sabers de la base de dades, filtrada per bloc i materia
        :returns: lista de tuples, on cada fila conté l'id i la descripcio del saber corresponent"""
        try:
            ordre = f"SELECT DISTINCT sabers_id, sabers_desc FROM {self.taula}, mat_sabers WHERE" \
                    f" sabers.sabers_bloc = ? AND mat_sabers.matsaber_mat = ? " \
                    f"AND mat_sabers.matsaber_saber = sabers.sabers_id " \
                    f"ORDER BY sabers.sabers_id ASC"
            self.cursor.execute(ordre, (bloc_id, materia_id))
            resultat_consulta = self.cursor.fetchall()
            if len(resultat_consulta) == 0:
                raise Warning("Error: No s'ha pogut obtenir la llista de sabers.")
            
            # Formatem com a llista: [(id_saber, descripcio_saber), ...]
            sabers_llista = list(resultat_consulta)
            # Formatem com a missatge:
            sabers_missatge = [Saber(saber[0], saber[1]) for saber in sabers_llista]
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
        """Obté els blocs de la materia
        parameter id_materia: id de la materia
        returns: llista de blocs en format missatgeria
        rtype: list
        raises:
            ValueError: Si no s'ha pogut obtenir els blocs
            Warning: Quan es fa la consulta s'ha de fer amb un nombre
            Warning: Quan no consten blocs asssignats a la materia
        """

        self.id_materia = id_materia
        if not isinstance(self.id_materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            ordre = f"SELECT DISTINCT bloc_id, bloc_text FROM {self.taula}, sabers, mat_sabers WHERE blocs.bloc_id = \
                sabers.sabers_bloc AND sabers.sabers_id = mat_sabers.matsaber_saber " \
                    f"AND mat_sabers.matsaber_mat = {self.id_materia} ORDER BY bloc_id ASC"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            if resultat_consulta is None or len(resultat_consulta) == 0:
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

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "competencies"

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
        materia = materia_id
        if not isinstance(materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            ordre = f"SELECT DISTINCT {self.taula}.competencia_id, {self.taula}.competencia_num, " \
                    f"{self.taula}.competencia_desc FROM competencies, compmat WHERE compmat.compmat_materia =" \
                    f" {materia} " \
                    f"AND compmat.compmat_competencia = competencies.competencia_id ORDER BY competencia_num ASC"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            if len(resultat_consulta) == 0:
                raise Warning("Matèria sense competencies assignades")
            dades_retorn = [list(item) for item in resultat_consulta]
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
        if not isinstance(materia_id, int) or not isinstance(competencia_id, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        try:
            ordre = f"SELECT DISTINCT critaval.critaval_id, critaval.critaval_num, critaval.critaval_desc " \
                    f"FROM {self.taula}, matcomp_aval WHERE critaval.critaval_comp = {competencia_id} " \
                    f"AND matcomp_aval.matcompaval_mat = {materia_id} " \
                    f"AND matcomp_aval.matcompaval_crit = critaval.critaval_id"
            self.cursor.execute(ordre)
            resultat_consulta = self.cursor.fetchall()
            if len(resultat_consulta) == 0:
                raise Warning("Matèria sense criteris assignats")
            return [criteri_missatge(element[0], element[1], element[2]) for element in list(resultat_consulta)]
        except sqlite3.OperationalError as missatge_error:
            raise ValueError(f"Error: {missatge_error}") from missatge_error


class InformadorMateriaPlantilla:
    """Obté tota la informació de  la matèria de la base de dades"""

    def __init__(self, mode: int):
        super().__init__()
        self.id_materia = None
        self.mode = mode

    def obtenir_competencies_criteris(self, materia_id: int):
        """
        args: materia_id: integer, obté les competències de la matèria i els criteris d'avaluació
        corresponents.
        Crea un `Warning` si no es proporciona un valor numèric.
        Retor its id, title, description and related criteria.
        Raises a `ValueError` if the criteria could not be obtained due to an `OperationalError`.
        """
        self.id_materia = materia_id
        if not isinstance(self.id_materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
            # Obtenim les competencies de la materia:
        competencies_materia = list(Lectorcompetencies(self.mode).obtenir_competencies_materia(materia_id))
        # Els creuem amb els criteris:
        for element in competencies_materia:
            element.append(Lectorcriteris(self.mode).obtenir_criteris_materia(materia_id, element[0]))
        competencies_format = [competencia_missatge(element[0], element[1], element[2], element[3]) for element in
                               competencies_materia]
        return competencies_format


class InformadorElementsPropis(InformadorMateriaPlantilla):
    """Obté tota la informació de  la matèria de la base de dades"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode

    def obtenir_blocssabers(self, id_materia: int):
        """Obté els blocs amb els sabers corresponents de la materia de la base de dades
        Parameters:
        id_materia: int, identificador de la materia a consultar
        Returns:
        Llista de blocs, amb els sabers associat a cada bloc
        """
        self.id_materia = id_materia
        if not isinstance(self.id_materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        # Obtenim els blocs de sabers:
        blocs_materia = Lectorsblocs(self.mode).obtenir_blocs(self.id_materia)
        # Els creuem amb els sabers:
        for element in blocs_materia:
            element.sabers_associats = Lectorsabers(self.mode).segons_bloc_materia(element.id, self.id_materia)
        return blocs_materia
    
    def obtencio_curriculum_materia(self, id_materia: int):
        """Obté el curriculum de la materia de la base de dades
        Parameters:
        id_materia: int, identificador de la materia a consultar
        Returns:
        Curriculum de la materia
        """
        self.id_materia = id_materia
        nom_materia = LectorMateriesCompletes(self.mode).obtenir_noms_materies(id_materia)
        id_curs_materia = LectorMateriesCompletes(self.mode).obtenir_curs_materia(self.id_materia)
        nom_curs = LectorCursos(self.mode).obtenir_descripcio(id_curs_materia).descripcio
        blocs = Lectorsblocs(self.mode).obtenir_blocs(self.id_materia)
        competencies = self.obtenir_competencies_criteris(self.id_materia)
        curriculum_materia = Materia(self.id_materia, nom_materia, id_curs_materia, nom_curs, blocs, competencies)
        return curriculum_materia


class InformadorElementsTransversals(InformadorMateriaPlantilla):
    """Classe que informa dels aspectes transversals a avaluar per una o diverses matèries,
    suposant que es tracta de la mateixa etapa i nivell"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode

    def obtenir_transversals_materia(self, materies_id: int):
        """Obté tota la informació de les transversals corresponents a una matèria d'un curs en concret"""
        llista_transversals = []
        self.id_materia = materies_id
        if not isinstance(self.id_materia, int):
            raise Warning("Consulta s'ha de fer amb un nombre")
        # Obtenim el curs corresponent a la matèria:
        id_curs_materia = LectorMateriesCompletes(self.mode).obtenir_curs_materia(self.id_materia)
        nom_curs = LectorCursos(self.mode).obtenir_descripcio(id_curs_materia)
        # Obtenim els transversals:
        transversals = LectorMateriesCompletes(self.mode).transversals_curs(materies_id)
        # Obtenim les competències:
        competencies = []
        for transversal in transversals:
            competencies = []
            competencies = self.obtenir_competencies_criteris(transversal)
            nom_materia = LectorMateriesCompletes(self.mode).obtenir_noms_materies(transversal)
            llista_transversals.append(Transversals(transversal, nom_materia, id_curs_materia, nom_curs.descripcio, competencies))
        return (llista_transversals)


class InformadorGlobal:
    """Obté tota la informació de  la matèria de la base de dades, tant dels seus elements espcífics com
    dels tranvsersals"""

    def __init__(self, mode: int):
        self.mode = mode

    def obtenir_informacio_global(self, materia: int):
        """Obté tota la informació de  la matèria de la base de dades, tant dels seus elements espcífics com
        dels tranvsersals"""
        if not isinstance(materia, int):
            raise TypeError("Consulta s'ha de fer amb un nombre")
        curriculumglobal = Curriculum(InformadorElementsPropis(self.mode).obtencio_curriculum_materia(materia), \
            InformadorElementsTransversals(self.mode).obtenir_transversals_materia(materia))
        return curriculumglobal