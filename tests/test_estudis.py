import os
from os.path import dirname
from unittest import TestCase
import sqlite3
import pytest
from dataclasses import is_dataclass


from src.progpy.moduls.bbdd.estudis import GeneradorArbreMateries
from src.progpy.missatgeria import MateriaBase

arrel_tests = os.path.join(os.path.abspath(dirname(__file__)), "test.db")
arrel_produccio = os.path.normpath(os.path.join(os.path.abspath(dirname(dirname(__file__))),
                                                "src/progpy/dades/dades.db"))


class TestGeneradorArbresMateries(TestCase):
    """Comprova la classe GeneradorArbreMateries"""

    def test_parametres_inicials(self):
        """Comprova que el Generador té els paràmetres correctes"""
        generador_test = GeneradorArbreMateries(0)
        generador_produccio = GeneradorArbreMateries(1)
        assert generador_test.ruta_arxiu_bbdd == arrel_tests
        assert generador_produccio.ruta_arxiu_bbdd == arrel_produccio

        # Tests that an exception is raised when the database connection fails
    def test_database_connection_fails(self):
        """Comprova que l'objecte GeneradorArbreMateries genera un avís d'error quan falla la \
            connexio a la base de dades"""
        with pytest.raises(sqlite3.ProgrammingError):
            generador = GeneradorArbreMateries(0)
            generador.conexio.close()
            generador.obtenir_nivells()

        # Tests that the 'obtenir_cursos_amb_modalitat' method raises an exception when the \
        # parameter is not an integer
    def test_obtenir_cursos_amb_modalitat_raises_exception_when_parameter_not_integer(self):
        """Comprova que genera un error si el paràmetre no és un integer"""
        generador = GeneradorArbreMateries(0)
        with pytest.raises(TypeError):
            generador.obtenir_cursos_amb_modalitat('not an integer')  # type: ignore

    def test_obtenir_materies_curs_raises_exception_when_parameter_not_integer(self):
        """Comprova que l'objecte GeneradorArbreMateries genera un avís d'error quan se li \
            proporciona un paràmetre que no és un integer"""
        generador = GeneradorArbreMateries(0)
        with pytest.raises(TypeError):
            generador.obtenir_materies_curs('not an integer')  # type: ignore

    def test_obtenir_nivells_returns_empty_list_when_no_values_in_database(self):
        """Comprova que la bbdd retorna una llista buida dels nivells si es canvia a una
        tipologia de materies que no existeix"""
        generador = GeneradorArbreMateries(0)
        generador.tipus_materies = 3
        assert generador.obtenir_nivells() == []

    def test_obtenir_modalitats_returns_empty_list_when_no_values_in_database(self):
        """Comprova que la bbdd retorna una llista buida de les matèries si es canvia a una
        tipologia de materies que no existeix"""
        generador = GeneradorArbreMateries(0)
        generador.tipus_materies = 3
        assert generador.obtenir_modalitats() == []

    def test_obtenir_cursos_sense_modalitat_returns_empty_list_when_no_values_in_database(self):
        """Comprova que la bbdd retorna una llista buida de les matèries si es canvia a una
        modalitat que no existeix"""
        generador = GeneradorArbreMateries(0)
        generador.tipus_materies = 3
        assert generador.obtenir_cursos_sense_modalitat() == []

    def test_materies_curs(self):
        """Comprova que  la bbdd retorna les matèries esperades"""
        materia_esperada = [MateriaBase(1, "Matemàtiques")]
        generador = GeneradorArbreMateries(0)
        generador_resultat = generador.obtenir_materies_curs(2)
        assert isinstance(generador_resultat, list), "Generador retorna una llista"
        assert is_dataclass(generador_resultat[0]), "Els lements de la llista han de ser dataclass"
        assert generador_resultat == materia_esperada, "Hauria de retornar Matemàtiques de 2n d'ESO"
