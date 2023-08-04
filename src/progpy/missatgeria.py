"""Missatgeria interna de l'aplicació"""

from dataclasses import dataclass, field


@dataclass(repr=True)
class Etapa:
    """Missatgeria de l'Etapa"""
    id: int
    descripcio: str
    
    def __post_init__(self):
        if isinstance(self.id, int) is False or isinstance(self.descripcio, str) is False:
            raise TypeError("Id no té format numèric  o descripcio no tenen format de text")
    

@dataclass(repr=True)
class Modalitat:
    """Missatgeria de la modalitat"""
    id: int
    descripcio: str

    def __post_init__(self):
        if isinstance(self.id, int) is False or isinstance(self.descripcio, str) is False:
            raise TypeError("Id no té format numèric  o descripcio no tenen format de text")


@dataclass(repr=True)
class Curs:
    """Missatgeria del curs"""
    id: int
    descripcio: str

    def __post_init__(self):
        if isinstance(self.id, int) is False or isinstance(self.descripcio, str) is False:
            raise TypeError("Id no té format numèric  o descripcio no tenen format de text")


@dataclass(repr=True)
class NovaProgramacio:
    """Classe de missatge per a noves programacions"""
    nom: str
    descripcio: str
    durada: float = field(default=0.0)

    def __post_init__(self):
        if isinstance(self.nom, str) is False or isinstance(self.descripcio, str) is False:
            raise TypeError("Nom o descripcio no tenen format de text")


@dataclass(repr=True)
class Programacio:
    """Programacio de la Base de dades"""
    id: int
    nom: str
    descripcio: str
    durada: float = field(default=0.0)

@dataclass(repr=True)
class criteri_missatge:
    id: int
    num: int
    descripcio: str

@dataclass(repr=True)
class Curs_missatge:
    id: int
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
class Saber:
    """Missatgeria que transmet els sabers de la matèria"""
    id: int
    descripcio: str


@dataclass(repr=True)
class MateriaBase:
    """Missatge d'una matèria"""
    id_materia: int
    nom: str



@dataclass(repr=True)
class Materia(MateriaBase):
    """Missatge d'una matèria especifica"""
    id_curs: int
    curs: str
    blocs: list
    competencies: list


@dataclass(repr=True)
class Transversals:
    """Missatge de les competències transversals a treballar"""
    id_materia: int
    nom: str
    id_curs: int
    curs: str
    competencies: list

# Aquest ha de ser l'element que la interficie processi quan es carregui una programació
@dataclass(repr=True)
class Curriculum:
    """Missatge dels elements curriculars a tenir en compte, tant els especifics
    de la matèria com els transversals"""
    especific: list
    transversal: list
