import sqlite3
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bbdd.base import Connectorbbdd
from missatgeria import Etapa, Modalitat, Curs, MateriaBase


# Context from Class or Interface src/progpy/moduls/missatgeria.py:Modalitat
# Class Modalitat:
# 	Fields:
# 		id: int
# 		descripcio: str


class GeneradorArbreMateries(Connectorbbdd):
    """Proporciona totes les opcions per a la interficie gràfica per a la
    creació de la programació anual"""

    def __init__(self, mode):
        super().__init__(mode)
        self.mode = mode
        self.tipus_materies = 1

    def obtenir_nivells(self):
        """Proporciona els nivells en els que hi ha una matèria comuna registrada"""
        try:
            ordre_nivells = "SELECT DISTINCT etapa.etapa_id,etapa_desc FROM etapa,materia, materia_completa,\
                curs, nivell WHERE materia.materia_tipus = ? AND materia.materia_id = materia_completa.matcomp_mat \
                AND materia_completa.matcomp_curs = CURS.curs_id \
                AND curs.curs_nivell= nivell.nivell_id \
                AND nivell_etapa = etapa.etapa_id"
            nivells_bbdd = self.cursor.execute(ordre_nivells, (self.tipus_materies,)).fetchall()
            self.cursor.close()
            nivells_formatats = [Etapa(item[0], item[1]) for item in nivells_bbdd]
            return nivells_formatats
        except sqlite3.OperationalError as error:
            raise Warning from error

    def obtenir_modalitats(self):
        """Proporciona els nivells en els que hi ha una matèria comuna registrada"""
        try:
            ordre_nivells = "SELECT DISTINCT curs.curs_modalitat, modalitats.modalitats_desc \
                FROM curs, materia, materia_completa, modalitats \
                WHERE materia_completa.matcomp_curs = curs.curs_id \
                AND materia.materia_id = materia_completa.matcomp_mat \
                AND modalitats.modalitats_id = curs.curs_modalitat \
                AND materia.materia_tipus = ? ORDER BY modalitats.modalitats_desc ASC"
            modalitats_bbdd = self.cursor.execute(ordre_nivells, (self.tipus_materies,)).fetchall()
            self.cursor.close()
            modalitats_formatats = [Modalitat(item[0], item[1]) for item in modalitats_bbdd]
            return modalitats_formatats
        except sqlite3.OperationalError as exc:
            raise Warning from exc

    def obtenir_cursos_sense_modalitat(self):
        """Retorna el curs correponent a la matèria"""
        try:
            ordre = "SELECT DISTINCT curs.curs_id, nivell.nivell_nom, etapa.etapa_desc from  materia, \
                materia_completa ,modalitats, curs, nivell, etapa WHERE curs.curs_nivell = nivell.nivell_id\
                AND etapa.etapa_id = nivell.nivell_etapa AND curs.curs_modalitat = modalitats.modalitats_id\
                AND materia.materia_id = materia_completa.matcomp_mat AND materia_completa.matcomp_curs = \
                curs.curs_id AND materia.materia_tipus = ?\
                ORDER BY curs.curs_id ASC"
            self.cursor.execute(ordre, (self.tipus_materies,))
            cursos_bbdd = list(self.cursor.fetchall())
            self.cursor.close()
            cursos_formatats = [Curs(curs[0], str(curs[1] + " - " + curs[2])) for curs in cursos_bbdd]
            return cursos_formatats
        except sqlite3.OperationalError as exc:
            raise Warning from exc

    def obtenir_cursos_amb_modalitat(self, modalitat: int):
        """Retorna el curs correponent a la matèria"""
        if not isinstance(modalitat, int):
            raise TypeError("Modalitat ha de ser un nombre")
        try:
            ordre = "SELECT DISTINCT curs.curs_id, nivell.nivell_nom, etapa.etapa_desc from  materia, \
                materia_completa ,modalitats, curs, nivell, etapa WHERE curs.curs_nivell = nivell.nivell_id\
                AND etapa.etapa_id = nivell.nivell_etapa AND curs.curs_modalitat = modalitats.modalitats_id\
                AND materia.materia_id = materia_completa.matcomp_mat AND materia_completa.matcomp_curs = \
                curs.curs_id AND materia.materia_tipus = 1 AND modalitats.modalitats_id = ?\
                ORDER BY curs.curs_id ASC"
            self.cursor.execute(ordre, (modalitat,))
            cursos_bbdd = list(self.cursor.fetchall())
            self.cursor.close()
            cursos_formatats = [Curs(curs[0], str(curs[1] + " - " + curs[2])) for curs in cursos_bbdd]
            return cursos_formatats
        except sqlite3.OperationalError as exc:
            raise Warning from exc

    def obtenir_materies_curs(self, curs: int):
        "Retorna les matèries per a un curs concret"
        if not isinstance(curs, int):
            raise TypeError("Curs ha de ser un nombre")
        try:
            ordre = "SELECT DISTINCT materia_completa.matcomp_id, materia.materia_nom FROM materia, \
            materia_completa, curs WHERE curs.curs_id = materia_completa.matcomp_curs\
            AND materia.materia_id = materia_completa.matcomp_mat AND materia.materia_tipus = 1\
            AND curs.curs_id = ?\
            ORDER BY materia_completa.matcomp_id ASC"
            self.cursor.execute(ordre, (curs,))
            materies_bbdd = list(self.cursor.fetchall())
            self.cursor.close()
            materies_formatades = [MateriaBase(materia[0], materia[1]) for materia in materies_bbdd]
            return materies_formatades
        except sqlite3.OperationalError as exc:
            raise Warning from exc