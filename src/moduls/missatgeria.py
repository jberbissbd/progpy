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
class materia:
    id_materia: int
    nom: str
    curs: str
    blocs: list
    competencies: list
