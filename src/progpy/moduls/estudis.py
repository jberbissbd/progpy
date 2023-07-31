from src.progpy.moduls.bbdd import Connectorbbdd

# Context from Class or Interface src/progpy/moduls/missatgeria.py:Modalitat
# Class Modalitat:
# 	Fields:
# 		id: int
# 		descripcio: str

class GeneradorArbreMateries(Connectorbbdd):

    def __init__(self, mode):
        super().__init__(0)
        self.mode = mode

    def obtenir_nivells(self):
        """Proporciona els nivells en els que hi ha una ma"""