from dataclasses import is_dataclass
import sqlite3

from bbdd.bbdd import Connectorbbdd #  pylint: ignore import-error
from progpy.missatgeria import NovaProgramacio


class ControladorProgramacions(Connectorbbdd):
    """Controla les operacions relacionades amb una programació"""
    def __init__(self, mode: int):
        super().__init__(mode)
        self.taula = "proganual"

    def crear_programacio(self, missatge: NovaProgramacio):
        """Funció per a crear una programacio"""
        # Comprovem el format d'entrada:
        if is_dataclass(missatge) is False:
            raise TypeError("Missatge no és dataclass")
        try:
            ordre = f"INSERT INTO {self.taula} ?, ?, ?"
            self.cursor.execute(ordre, (missatge.nom, missatge.descripcio, missatge.durada))
            self.cursor.close()
            return True
        except sqlite3.OperationalError as missatge_error:
            raise ValueError("Error:") from missatge_error

    def actualitzar_programacio(self, missatge: list):
        "Actualitzar una programacio o diverses proporcionades per una llista"
        # Comprovem que el missatge d'entrada és una llista
        if isinstance(missatge, list) is False:
            raise TypeError("Missatge no és una llista")
        # Comprovem el format d'entrada de les programacions a actualitzar:
        try:
            for element in missatge:
                if is_dataclass(element) is False:
                    raise TypeError("Missatge no és dataclass")
                ordre = f"UPDATE {self.taula} SET proganual_nom = ?, proganual_descripcio = ?, proganual_durada = ? \
                        WHERE proganual_id = ?"
                self.cursor.execute(ordre, (element.nom, element.descripcio, element.durada, element.id))
                self.cursor.close()
                resultat = self.cursor.rowcount
                if resultat == 0:
                    raise ValueError("Error: no s'ha trobat la programacio indicada")
        except sqlite3.OperationalError as error_bbdd:
            raise ValueError("Error:") from error_bbdd
            

    def obtenir_programacions(self):
        pass

    def obtenir_programacio(self, id_programacio: int):
        pass

    def actualitzar_programació(self,id_programacio: int):
        pass