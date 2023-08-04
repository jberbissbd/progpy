import os.path
import sqlite3
from os.path import dirname

encoding = 'utf-8'

"""Module per a connectar amb la base de dades segons la ruta proporcionada per la classe Lectorbbdd"""


class Lectorbbdd:
    """Classe per a determinar la ruta a utilitzar de la base de dades
    :parameter mode: 0 per a testing, 1 per a ús normal."""

    def __init__(self, mode: int):
        super().__init__()
        self.mode = mode
        self.ruta_arxiu_bbdd = os.path.normpath(os.path.abspath(dirname(dirname(dirname(__file__)))))
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