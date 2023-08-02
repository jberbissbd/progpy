import os
from os.path import dirname
from unittest import TestCase
import dataclasses
from dataclasses import dataclass, is_dataclass
import pytest
from src.progpy.moduls.curriculum import Lectormateries, Lectorsabers, Lectorsblocs, Lectorcriteris, \
    LectorMateriesCompletes, Lectorcompetencies, InformadorElementsPropis, InformadorMateriaPlantilla
from src.progpy.moduls.estudis import GeneradorArbreMateries
from src.progpy.moduls.missatgeria import Saber, blocs_missatge, criteri_missatge, competencia_missatge

arrel_tests = os.path.join(os.path.abspath(dirname(__file__)), "test.db")
arrel_produccio = os.path.normpath(os.path.join(os.path.abspath(dirname(dirname(__file__))), "src/progpy/dades/dades.db"))


class TestGeneradorArbresMateries(TestCase):

    def test_parametres_inicials(self):
        """Comprova que el Generador té els paràmetres correctes"""
        generador_test = GeneradorArbreMateries(0)
        generador_produccio = GeneradorArbreMateries(1)
        assert generador_test.ruta_arxiu_bbdd == arrel_tests
        assert generador_produccio.ruta_arxiu_bbdd == arrel_produccio