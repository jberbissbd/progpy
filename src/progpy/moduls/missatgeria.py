"""Missatgeria interna de l'aplicació"""

from dataclasses import dataclass


@dataclass(repr=True)
class criteri_missatge:
    id: int
    num: int
    descripcio: str


@dataclass(repr=True)
class blocs_missatge:
    id: int
    text: str
    sabers_associats: list


@dataclass(repr=True)
class competencia_missatge:
    id: int
    num: int
    descripcio: str
    criteris: list


@dataclass(repr=True)
class saber_missatgeria:
    id: int
    descripcio: str


@dataclass(repr=True)
class Materia:
    id_materia: int
    nom: str
    curs: str
    blocs: list
    competencies: list


@dataclass(repr=True)
class Transversals:
    """Missatge de les competències transversals a treballar"""
    id_materia: int
    nom: str
    curs: str
    competencies: list

# Aquest ha de ser l'element que la interficie processi quan es carregui una programació
@dataclass(repr=True)
class Curriculum:
    """Missatge dels elements curriculars a tenir en compte, tant els especifics
    de la matèria com els transversals"""
    especific: list
    trasnversal: list
