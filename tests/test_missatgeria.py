import dataclasses
from dataclasses import dataclass
from unittest import TestCase
import pytest

from missatgeria import Etapa, Modalitat, NovaProgramacio


class EtapaTests(TestCase):
    
    def test_format_variables_creacio(self):
        "Comprova que les variables de l'objecte NovaProgramacio son correctes"
        with pytest.raises(TypeError):
            error_descripcio = Etapa(1, 1)  # type: ignore # noqa: F841 pylint: disable=unused-variable
        with pytest.raises(TypeError):
            error_id = Etapa("a", "a")  # type: ignore # pylint: disable=unused-variable, type: ignore # noqa: F841

    def test_creacio_nova_programacio(self):
        "Comprova que l'objecte NovaProgramacio es una instància de la classe NovaProgramacio"
        nova_prova = Etapa(1, "Curs de prova")
        assert issubclass(nova_prova.__class__, Etapa)


class ModalitatTests(TestCase):
    
    def test_format_variables_creacio(self):
        "Comprova que les variables de l'objecte NovaProgramacio son correctes"
        with pytest.raises(TypeError):
            modalitat_descripcio = Modalitat(1, 1)  # type: ignore pylint: ignore=unused-variable # noqa: F841
        with pytest.raises(TypeError):
            modalitat_id = Modalitat("a", "a")  # type: ignore pylint: ignore=unused-variable # noqa: F841

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
