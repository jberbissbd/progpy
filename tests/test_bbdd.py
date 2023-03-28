import sqlite3
import unittest
import sys
import os

directori = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.join(directori, "src"))
from bbdd import Lectorbbdd, Connectorbbdd, Llistadormateries, Llistadorsabers


class TestLector(unittest.TestCase):
    """Comprova la classe Lector"""

    def test_mode_testing(self):
        """Comprova la ruta de l'arxiu de base de dades en el mode testeig"""
        lector = Lectorbbdd(0)
        self.assertEqual(lector.ruta_arxiu_bbdd, "/home/jordi/Documents/Projectes/Progpy/tests/test.db",
                         msg="La ruta de l'arxiu en mode testeig no es correcte")

    def test_mode_produccio(self):
        """Comprova la ruta de l'arxiu de base de dades en el mode de producció"""
        lector = Lectorbbdd(1)
        self.assertEqual(lector.ruta_arxiu_bbdd, "/home/jordi/Documents/Projectes/Progpy/src/dades/dades.db",
                         msg="La ruta de l'arxiu en mode producció no es correcte")

    def test_valors_invalids(self):
        """Comprova si la classe Lector accepta valors invàlids"""
        self.assertRaises(ValueError, Lectorbbdd, 2)


class TestConnector(unittest.TestCase):
    """Comprova la classe Connectorbbdd"""

    def test_mode_testing(self):
        """Comprova la connexió a la base de dades en el mode de test"""
        connector = Connectorbbdd(0)
        self.assertEqual(connector.ruta_arxiu_bbdd, "/home/jordi/Documents/Projectes/Progpy/tests/test.db",
                         msg="La ruta de l'arxiu en mode testeig no es correcte")

    def test_mode_produccio(self):
        """Comprova la connexió a la base de dades en el mode de producció"""
        connector = Connectorbbdd(1)
        self.assertEqual(connector.ruta_arxiu_bbdd, "/home/jordi/Documents/Projectes/Progpy/src/dades/dades.db",
                         msg="La ruta de l'arxiu en mode producció no es correcte")


class TestLlistadormateries(unittest.TestCase):
    """Comprova la classe Llistadormateries"""

    def test_llistar_materies_error_taula(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Llistadormateries(0)
        llistat.taula = "materies"
        self.assertRaises(Warning, msg="La classe Llistador materies no provoca un warning quan la taula no és "
                                       "correcte")

    def test_llistar_materies(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Llistadormateries(0)
        self.assertTrue(isinstance(llistat.llistar_materies(), list))

    def test_llistar_materies_completes(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Llistadormateries(0)
        self.assertTrue(isinstance(llistat.llistar_materies_completes(), list))

    def test_llistar_materies_completes(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Llistadormateries(0)
        self.assertTrue(isinstance(llistat.combinar_info_materies(), list))

    def test_llistar_materies_completes_llargada(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Llistadormateries(0)
        self.assertTrue(len(llistat.combinar_info_materies())>0)

    def test_llistar_materies_error_bbdd(self):
        """Comprova que amb una bbdd errònia, genera un avís"""
        llistat = Llistadormateries(0)
        llistat.ruta_arxiu_bbdd = "/home/jordi/Documents/Projectes/Progpy/tests/dummy.db"
        self.assertRaises(ValueError, msg="La classe Llistador materies no provoca un warning quan la bbdd no és ")


class TestLlistadorSabers(unittest.TestCase):
    """Comprova la classe Llistadorsabers"""

    def test_llistar_sabers_error_taula(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Llistadorsabers(0)
        llistat.taula = "saber"
        self.assertRaises(Warning, msg="La classe Llistador materies no provoca un warning quan la taula no és "
                                       "correcte")

    def test_llistar_sabers(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Llistadorsabers(0)
        a = llistat.consulta_no_filtrada()
        self.assertTrue(isinstance(a, list))

    def test_llistar_sabers_longitud_positiva(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Llistadorsabers(0)
        self.assertTrue(len(llistat.consulta_no_filtrada())>0)

    def test_llistar_sabers_blocs(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Llistadorsabers(0)
        a = llistat.consulta_blocs()
        self.assertTrue(isinstance(a, list))

    def test_llistar_sabers_blocs_longitud_positiva(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Llistadorsabers(0)
        self.assertTrue(len(llistat.consulta_blocs())>0)


if __name__ == '__main__':
    unittest.main()
