from dataclasses import dataclass


@dataclass(repr=False)
class criteri:
    id: int
    num: int
    descripcio: str


@dataclass(repr=False)
class competencia:
    id: int
    num: int
    descripcio: str


@dataclass(repr=False)
class saber:
    id: int
    descripcio: str


@dataclass(repr=False)
class materia:
    id_materia: int
    nom: str
    curs: int
    criteris: list
    sabers: list
    competencies: list
