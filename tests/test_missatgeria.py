import dataclasses
from dataclasses import *
from unittest import TestCase
import pytest

from src.progpy.missatgeria import Etapa, Modalitat, NovaProgramacio


class EtapaTests(TestCase):
    
    def test_format_variables_creacio(self):
        "Comprova que les variables de l'objecte NovaProgramacio son correctes"
        with pytest.raises(TypeError):
            error_descripcio = Etapa(1, 1)  # pylint: ignore=unused-variable
        with pytest.raises(TypeError):
            error_id = Etapa("a", "a")  # pylint: ignore=unused-variable

    def test_creacio_nova_programacio(self):
        "Comprova que l'objecte NovaProgramacio es una instància de la classe NovaProgramacio"
        nova_prova = Etapa(1, "Curs de prova")
        assert issubclass(nova_prova.__class__, Etapa)


class ModalitatTests(TestCase):
    
    def test_format_variables_creacio(self):
        "Comprova que les variables de l'objecte NovaProgramacio son correctes"
        with pytest.raises(TypeError):
            modalitat_descripcio = Modalitat(1, 1)  # pylint: ignore=unused-variable
        with pytest.raises(TypeError):
            modalitat_id = Modalitat("a", "a")  # pylint: ignore=unused-variable

    def test_creacio_nova_programacio(self):
        "Comprova que l'objecte NovaProgramacio es una instància de la classe NovaProgramacio"
        modalitat_prova = Modalitat(1, "Curs de prova")
        assert issubclass(modalitat_prova.__class__, Modalitat)


class Programacio(TestCase):
    
    def test_format_variables_creacio(self):
        "Comprova que les variables de l'objecte NovaProgramacio son correctes"
        with pytest.raises(TypeError):
            nova_prova = NovaProgramacio(1, "Curs de prova")  # pylint: ignore=unused-variable

    def test_creacio_nova_programacio(self):
        "Comprova que l'objecte NovaProgramacio es una instància de la classe NovaProgramacio"
        nova_prova = NovaProgramacio("a", "Curs de prova")
        assert issubclass(nova_prova.__class__, NovaProgramacio)
