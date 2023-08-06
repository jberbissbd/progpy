from dataclasses import dataclass, is_dataclass
import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bbdd.base import Connectorbbdd
from missatgeria import NovaProgramacio, Programacio


class ControladorTemes(Connectorbbdd):

    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "tema"



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
        pass


