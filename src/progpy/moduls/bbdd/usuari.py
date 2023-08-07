from dataclasses import is_dataclass
import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bbdd.base import Connectorbbdd  # noqa: E402
from bbdd.curriculum import Lectorcriteris
from missatgeria import NovaProgramacio, Programacio, NouTema, criteri_missatge  # noqa: E402


class LectorCriterisTemes(Connectorbbdd):

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "tema_critaval"

    def lectura_criteris_temes(self):
        try:
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = self.cursor.fetchall()
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning("Error al obtenir la llista de criteris del tema:") from error

class ControladorTemes(Connectorbbdd):

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "tema"

    def crear_tema(self, missatge: list):
        """Funció per a crear una tema"""
        if issubclass(missatge[0].__class__, NouTema) is False or issubclass(missatge[1].__class__, 
            Programacio) is False or isinstance(missatge, list) is False:
            raise TypeError("Error: No s'ha proporcionat missatge amb la classe adequada")
        tema_num = missatge[0].num
        tema_descripcio = missatge[0].descripcio
        tema_proganual_id = missatge[1].id
        try:
            ordre = f"INSERT INTO {self.taula} ?, ?, ?"
            self.cursor.execute(ordre, (tema_num, tema_descripcio, tema_proganual_id))
            return True
        except sqlite3.OperationalError as missatge_error:
            raise ValueError("Error:") from missatge_error
        finally:
            self.cursor.close()

    def lectura_simple_temes(self):
        """Funció per a obtenir totes les temes de la base de dades"""
        try:
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = self.cursor.fetchall()
            return resultat
        except sqlite3.OperationalError as error:
            raise Warning("Error al obtenir la llista de temes:") from error
        finally:
            self.cursor.close()

    def lectura_integral_temes(self):
        """Funció per a obtenir els temes de la base de dades amb tots els seus atributs"""
        pass


class ControladorProgramacions(Connectorbbdd):
    """Controla les operacions relacionades amb una programació"""
    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "proganual"

    def crear_programacio(self, missatge: NovaProgramacio):
        """Funció per a crear una programacio"""
        try:
            ordre = f"INSERT INTO {self.taula} ?, ?, ?"
            self.cursor.execute(ordre, (missatge.nom, missatge.descripcio, missatge.durada))
            return True
        except sqlite3.OperationalError as missatge_error:
            raise ValueError("Error:") from missatge_error
        finally:
            self.cursor.close()

    def actualitzar_programacio(self, missatge: list):
        "Actualitzar una programacio o diverses proporcionades per una llista"
        if not isinstance(missatge, list):
            raise TypeError("Missatge no és una llista")
        try:
            for element in missatge:
                if not is_dataclass(element):
                    raise TypeError("Missatge no és dataclass")
                ordre = f"UPDATE {self.taula} SET proganual_nom = ?, proganual_descripcio = ?, proganual_durada = ? \
                        WHERE proganual_id = ?"
                self.cursor.execute(ordre, (element.nom, element.descripcio, element.durada, element.id))
                resultat = self.cursor.rowcount
                if resultat == 0:
                    raise ValueError("Error: no s'ha trobat la programacio indicada")
        except sqlite3.OperationalError as error_bbdd:
            raise ValueError("Error:") from error_bbdd
        finally:
            self.cursor.close()

    def obtenir_programacions(self):
        """Obtenir les programacions de la base de dades"""
        try:
            self.cursor.execute(f"SELECT * FROM {self.taula}")
            resultat = list(self.cursor.fetchall())
            registres = self.cursor.rowcount
            if registres == -1:
                raise ValueError("Error: no s'ha trobat cap programacio")
            resultat_formatat = [Programacio(element[0], element[1], element[2], element[3]) for element in resultat]
            return resultat_formatat
        except sqlite3.OperationalError as error:
            raise ValueError("Error:") from error
        finally:
            self.cursor.close()

    def obtenir_programacio(self, id_programacio: int):
        """Obtenir una programació de la base de dades"""
        if isinstance(id_programacio, int) is False:
            raise TypeError("id_programacio no és int")
        try:
            ordre = f"SELECT * FROM {self.taula} WHERE proganual_id = ?"
            retorn = self.cursor.execute(ordre, (id_programacio,)).fetchall()
            nombre_retorns = self.cursor.rowcount
            if nombre_retorns == -1:
                raise ValueError("Error: no s'ha trobat cap programacio")
            return Programacio(retorn[0], retorn[1], retorn[2], retorn[3])
        except sqlite3.OperationalError as error:
            raise ValueError("Error:") from error
        finally:
            self.cursor.close()
