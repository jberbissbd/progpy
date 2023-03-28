import os.path
import sqlite3
import sys
from os.path import dirname

encoding = 'utf-8'


class Lectorbbdd:
    """Classe per a determinar la ruta a utilitzar de la base de dades
    :parameter mode: 0 per a testing, 1 per a ús normal."""

    def __init__(self, mode: int):
        super().__init__()
        self.mode = mode
        self.ruta_arxiu_bbdd = os.path.abspath(dirname(dirname(__file__)))
        if mode == 0:
            self.ruta_arxiu_bbdd = self.ruta_arxiu_bbdd + "/tests/test.db"
        elif mode == 1:
            self.ruta_arxiu_bbdd = self.ruta_arxiu_bbdd + "/src/dades/dades.db"
        else:
            raise ValueError("Mode del programa establert incorrectament, ha de ser 0 o 1")


class Connectorbbdd(Lectorbbdd):
    """Classe per a connectar amb la base de dades segons la ruta proporcionada per la classe Lectorbbdd
    :parameter mode: 0 per a testing i 1 per a ús normal"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.mode = mode
        self.taula = None
        self.conexio = sqlite3.connect(Lectorbbdd(self.mode).ruta_arxiu_bbdd)
        self.cursor = self.conexio.cursor()


class Llistadormateries(Connectorbbdd):
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
            raise Warning("Error al obtenir la llista de materies completes:") from tipus_error

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
                raise ValueError("Error: No s'ha pogut obtenir la llista de materies.") from error_basedades


class Llistadorsabers(Connectorbbdd):
    """Consulta la taula de sabers de la base de dades"""

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "sabers"

    def consulta_no_filtrada(self):
        """Consulta la taula de sabers de la base de dades, no filtrada
        :returns: lista de tuples, on cada fila conté l'id i la descripcio del saber corresponent"""
        try:
            self.cursor.execute(f"SELECT sabers_id, sabers_desc FROM {self.taula}")
            resultat_consulta = self.cursor.fetchall()
            self.cursor.close()
            return resultat_consulta
        except sqlite3.OperationalError as missatge_error:
            raise ValueError(f"Error: {missatge_error}")

    def consulta_blocs(self):
        """Consulta la taula de sabers de la base de dades, filtrada per sabers_id
        :returns: lista de tuples, on cada fila conté l'id i la descripcio del saber corresponent"""
        try:
            self.cursor.execute(f"SELECT sabers_id, sabers_desc, sabers_bloc, bloc_text FROM {self.taula}, "
                                f"blocs WHERE sabers.sabers_bloc = blocs.bloc_id ORDER BY sabers_id")
            resultat_consulta = self.cursor.fetchall()
            self.cursor.close()
            return resultat_consulta
        except sqlite3.OperationalError as missatge_error:
            raise ValueError(f"Error: {missatge_error}")


a = Llistadorsabers(1).consulta_blocs()
print(a)
