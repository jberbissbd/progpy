from progpy.moduls.bbdd import Connectorbbdd
from progpy.moduls.missatgeria import Etapa, Modalitat

# Context from Class or Interface src/progpy/moduls/missatgeria.py:Modalitat
# Class Modalitat:
# 	Fields:
# 		id: int
# 		descripcio: str

class GeneradorArbreMateries(Connectorbbdd):
    """Proporciona totes les opcions per a la interficie gràfica per a la
    creació de la programació anual"""

    def __init__(self, mode):
        super().__init__(0)
        self.mode = mode

    def obtenir_nivells(self):
        """Proporciona els nivells en els que hi ha una matèria comuna registrada"""
        ordre_nivells = "SELECT DISTINCT etapa.etapa_id,etapa_desc FROM etapa,materia, materia_completa,\
            curs, nivell WHERE materia.materia_tipus = 1 AND materia.materia_id = materia_completa.matcomp_mat \
            AND materia_completa.matcomp_curs = CURS.curs_id \
            AND curs.curs_nivell= nivell.nivell_id \
            AND nivell_etapa = etapa.etapa_id"
        nivells_bbdd = self.cursor.execute(ordre_nivells).fetchall()
        self.cursor.close()
        nivells_formatats = [Etapa(item[0], item[1]) for item in nivells_bbdd]
        return nivells_formatats

    def obtenir_modealitats(self):
        """Proporciona els nivells en els que hi ha una matèria comuna registrada"""
        ordre_nivells = "SELECT DISTINCT curs.curs_id, curs.curs_modalitat FROM curs,materia, \
            materia_completa \
            WHERE materia_completa.matcomp_curs = curs.curs_id \
            AND materia.materia_id = materia_completa.matcomp_mat \
            AND materia.materia_tipus =1"
        modalitats_bbdd = self.cursor.execute(ordre_nivells).fetchall()
        self.cursor.close()
        modalitats_formatats = [Modalitat(item[0], item[1]) for item in modalitats_bbdd]
        return modalitats_formatats
        