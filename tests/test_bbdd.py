import os
from os.path import dirname
from unittest import TestCase
from src.progpy.moduls.bbdd.bbdd import Lectorbbdd

arrel_tests = os.path.join(os.path.abspath(dirname(__file__)), "test.db")
arrel_produccio = os.path.normpath(os.path.join(os.path.abspath(dirname(dirname(__file__))), "src/progpy/dades/dades.db"))


class TestLector(TestCase):
    """Comprova la classe Lector"""

    def test_mode_testing(self):
        """Comprova la ruta de l'arxiu de base de dades en el mode testeig"""
        lector = Lectorbbdd(0)
        self.assertEqual(lector.ruta_arxiu_bbdd, arrel_tests,
                         msg="La ruta de l'arxiu en mode testeig no es correcte")

    def test_mode_produccio(self):
        """Comprova la ruta de l'arxiu de base de dades en el mode de producció"""
        lector = Lectorbbdd(1)
        self.assertEqual(lector.ruta_arxiu_bbdd, arrel_produccio,
                         msg="La ruta de l'arxiu en mode producció no es correcte")

    def test_valors_invalids(self):
        """Comprova si la classe Lector accepta valors invàlids"""
        self.assertRaises(ValueError, Lectorbbdd, 2)


class TestConnector(TestCase):
    """Comprova la classe Connectorbbdd"""

    def test_mode_testing(self):
        """Comprova la ruta de l'arxiu de base de dades en el mode testeig"""
        lector = Lectorbbdd(0)
        self.assertEqual(lector.ruta_arxiu_bbdd, arrel_tests,
                         msg="La ruta de l'arxiu en mode testeig no es correcte")

    def test_mode_produccio(self):
        """Comprova la ruta de l'arxiu de base de dades en el mode de producció"""
        lector = Lectorbbdd(1)
        self.assertEqual(lector.ruta_arxiu_bbdd, arrel_produccio,
                         msg="La ruta de l'arxiu en mode producció no es correcte")
