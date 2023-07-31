import os
from os.path import dirname
from unittest import TestCase
import dataclasses
from dataclasses import dataclass, is_dataclass
import pytest
from src.progpy.moduls.bbdd import Lectormateries, Lectorbbdd, Lectorsabers, Lectorsblocs, Lectorcriteris, \
    LectorMateriesCompletes, Lectorcompetencies, InformadorElementsPropis, InformadorMateriaPlantilla
from src.progpy.moduls.missatgeria import Saber, blocs_missatge, criteri_missatge, competencia_missatge


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


class TestLlistadormateries(TestCase):
    """Comprova la classe Lectormateries"""

    def test_llistar_materies_error_taula(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Lectormateries(0)
        llistat.taula = "materies"
        with pytest.raises(Warning):
            llistat.llistar_materies()

    def test_llistar_materies_error_bbdd(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Lectormateries(0)
        llistat.taula = "materies"
        llistat.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        with pytest.raises(Warning):
            llistat.llistar_materies()

    def test_llistar_materies(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = Lectormateries(0)
        self.assertTrue(isinstance(llistat.llistar_materies(), list))


class TestLlistadormateriesCompletes(TestCase):
    """Comprova la classe LectorMateriesCompletes"""

    def test_llistar_materies_error_taula(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = LectorMateriesCompletes(0)
        llistat.taula = "materies"
        with pytest.raises(Warning):
            llistat.obtenir_materies()

    def test_llistar_materies_error_bbdd(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = LectorMateriesCompletes(0)
        llistat.taula = "materies"
        llistat.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        with pytest.raises(Warning):
            llistat.obtenir_materies()

    def test_llistar_materies(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = LectorMateriesCompletes(0)
        self.assertTrue(isinstance(llistat.obtenir_materies(), list))

    def test_combinar_materies(self):
        """Comprova que retorna una llista de totes les matèries de la base de dades"""
        llistat = LectorMateriesCompletes(0)
        self.assertTrue(isinstance(llistat.combinar_info_materies(), list))

    def test_combinar_materies_error_bbdd(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = LectorMateriesCompletes(0)
        llistat.taula = "materies"
        llistat.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        with pytest.raises(ValueError):
            llistat.combinar_info_materies()

    def test_combinar_materies_error_taula(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = LectorMateriesCompletes(0)
        llistat.taula = "materies"
        with pytest.raises(ValueError):
            llistat.combinar_info_materies()

    def test_combinar_info_materies_edge_case_nonexistent_table(self):
        """Comprova que es genera un ValueError si la taula no existeix"""
        # Arrange
        lector = LectorMateriesCompletes(1)
        lector.taula = "nonexistent_table"

        # Act & Assert
        with pytest.raises(ValueError):
            lector.combinar_info_materies()


class TestLlistadorSabers(TestCase):
    """Comprova la classe Lectorsabers"""

    def test_llistar_sabers_error_taula(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Lectorsabers(0)
        llistat.taula = "saber"
        self.assertRaises(Warning, msg="La classe Llistador materies no provoca un warning quan la taula no és "
                                       "correcte")

    def test_llistar_sabers_error_parametres(self):
        """Comprova que amb valors sense resultat, genera un avís"""
        llistat = Lectorsabers(0)
        llistat.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        with pytest.raises(Warning):
            llistat.segons_bloc_materia(999, 999)

    def test_segons_bloc_materia_operational_error(self):
        """Comprova que amb valors sense resultat, genera un av."""
        lector = Lectorsabers(1)
        with pytest.raises(Warning):
            lector.segons_bloc_materia(100, 100)

    def test_segons_bloc_materia(self):
        """Comprova que el format de retorn es una llista"""
        llistat = Lectorsabers(0)
        retorn = llistat.segons_bloc_materia(1, 1)
        assert isinstance(retorn, list)

    def test_format_blocs_materials(self):
        """Comprova que amb una taula errònia, genera un avís"""
        llistat = Lectorsabers(0)
        retorn = llistat.segons_bloc_materia(1, 1)
        for element in retorn:
            assert dataclasses.is_dataclass(element)

    def test_error_bbdd(self):
        """Comprova que amb una taula erronia genera un Value Error"""
        lector = Lectorsabers(0)
        lector.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        lector.taula = "comp"
        with pytest.raises(ValueError):
            lector.segons_bloc_materia(1, 1)


class TestLlistadorsBlocs(TestCase):
    """Test de Lllistador de blocs"""

    def test_parametres_inici(self):
        """Comprova els parametres d'entrada"""
        lector_bloc = Lectorsblocs(0)
        assert lector_bloc.id_materia is None
        assert lector_bloc.taula == "blocs"

    # noinspection PyTypeChecker
    def test_obtenir_bloc_format_entrada(self):
        """Comprova que el format de retorn es una llista"""
        lector_bloc = Lectorsblocs(0)
        with pytest.raises(Warning):
            lector_bloc.obtenir_blocs("a")  # type: ignore

    def test_obtenir_blocs_materia(self):
        """Comprova que el format de retorn es una llista"""
        lbloc = Lectorsblocs(0)
        retorn = lbloc.obtenir_blocs(1)
        assert isinstance(retorn, list), "El format de retorn es una llista"

    def test_obtenir_blocs_nonexistent_id(self):
        """Comprova que genera un Warning amb un bloc que sabem que es incorrecte"""
        lectors_blocs = Lectorsblocs(1)
        with pytest.raises(Warning):
            lectors_blocs.obtenir_blocs(999)

    def test_obtenir_blocs_format(self):
        """Comprova que el format de retorn es una llista"""
        lectors_blocs = Lectorsblocs(0)
        resultat = lectors_blocs.obtenir_blocs(1)
        assert isinstance(resultat, list)

    def test_obtenir_blocs_format_element(self):
        """Comprova que el format dels elements de la llista te el format bloc missatge"""
        lectors_blocs = Lectorsblocs(0)
        resultat = lectors_blocs.obtenir_blocs(1)
        assert dataclasses.is_dataclass(resultat[0])

    def test_error_bbdd(self):
        """Comprova que genera un ValueError si la taula no existeix"""
        lector = Lectorsblocs(0)
        lector.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        lector.taula = "comp"
        with pytest.raises(ValueError):
            lector.obtenir_blocs(1)


# noinspection PyTypeChecker
class TestLectorCompetencies(TestCase):
    """Test sobre la classe de lector de competencies"""

    def test_format_parametres_entrada(self):
        """Comprova que la funcio competencies tan sols admet un nmbre com a entrada"""
        lector = Lectorcompetencies(0)
        with pytest.raises(Warning):
            lector.obtenir_competencies_materia("a")  # type: ignore

    def test_obtenir_competencies(self):
        """Comprova el format de retorn amb una materia que sabem que te dades"""
        lector = Lectorcompetencies(0)
        resultat = lector.obtenir_competencies_materia(1)
        assert isinstance(resultat, list)
        assert len(resultat) > 0

    def test_materia_sense_competencies(self):
        """Comprova que genera un Warning si la matèria no té competències assignades"""
        lector = Lectorcompetencies(1)
        with pytest.raises(Warning):
            lector.obtenir_competencies_materia(9999)

    def test_error_bbdd(self):
        """Comprova que genera un ValueError si la taula no existeix"""
        lector = Lectorcompetencies(0)
        lector.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        lector.taula = "comp"
        with pytest.raises(ValueError):
            lector.obtenir_competencies_materia(1)


class TestLectorcriteris(TestCase):
    """Comprova la classe Lectorcriteris"""

    def test_parametres_arrencada(self):
        """Comprova els parametres d'entrada"""
        lector = Lectorcriteris(0)
        assert lector.taula == "critaval"

    # noinspection PyTypeChecker
    def test_format_entrada(self):
        """Comprova que es genera un Warning si els parametres d'entrada no son correctes"""
        lector = Lectorcriteris(0)
        with pytest.raises(Warning):
            lector.obtenir_criteris_materia("a", "a")  # type: ignore

    def test_formats_resultats(self):
        """Comprovem el format de retorn"""
        lector = Lectorcriteris(0)
        resultat = lector.obtenir_criteris_materia(1, 1)
        assert isinstance(resultat, list)
        for element in resultat:
            assert dataclasses.is_dataclass(element)

    def test_error_bbdd(self):
        """Comprova que genera un ValueError si la taula no existeix"""
        lector = Lectorcriteris(0)
        lector.ruta_arxiu_bbdd = os.path.join(arrel_tests, "dummy.db")
        lector.taula = "comp"
        with pytest.raises(ValueError):
            lector.obtenir_criteris_materia(1, 1)

    def test_nocriteris_warning(self):
        """Comprova que genera un Warning si no s'introdueix nmbre de criteris"""
        lector = Lectorcriteris(0)
        with pytest.raises(Warning):
            lector.obtenir_criteris_materia(99999, 1)  # type: ignore


class TestInformadorMateriaPlantilla(TestCase):
    def test_error_competencies(self):
        """Comprova que genera un Warning si no s'introdueix un nombre de materia"""
        lector = InformadorMateriaPlantilla(0)
        with pytest.raises(Warning):
            lector.obtenir_competencies_criteris("a")  # type: ignore

    def test_materia_erronia(self):
        """Comprova que genera un Warning si no s'introdueix un nombre de materia"""
        lector = InformadorMateriaPlantilla(0)
        with pytest.raises(Warning):
            lector.obtenir_competencies_criteris(9999)  # type: ignore


    def test_format_competencies(self):
        resultat_consulta = InformadorMateriaPlantilla(0).obtenir_competencies_criteris(1)
        assert isinstance(resultat_consulta, list)
        assert len(resultat_consulta) > 0
        for element in resultat_consulta:
            assert is_dataclass(competencia_missatge) is True


class TestInformadorElementsPropis(TestCase):

    def test_creador_materia(self):
        """Comprova que el format de retorn es una llista"""
        lector = InformadorElementsPropis(0)
        assert lector.mode == 0
        assert lector.id_materia is None

    def test_blocssabers(self):
        """Comprova que es genera un Warning si no s'introdueix un nombre de materia"""
        lector = InformadorElementsPropis(0)
        with pytest.raises(Warning):
            lector.obtenir_blocssabers("a")  # type: ignore

    def test_obtenir_blocssabers_formats(self):
        # Happy path test for obtenir_blocssabers
        informador = InformadorElementsPropis(1)
        blocs = informador.obtenir_blocssabers(1)
        assert isinstance(blocs, list) is True
        assert all(dataclasses.is_dataclass(item) for item in blocs)
        assert all(dataclasses.is_dataclass(saber)
                   for bloc in blocs for saber in bloc.sabers_associats)

    def test_obtenir_criteris_tipologia_input(self):
        informador = InformadorElementsPropis(1)
        with pytest.raises(Warning):
            informador.obtenir_competencies_criteris("a")  # type: ignore

    def test_obtenir_criteris_materia_erronia(self):
        informador = InformadorElementsPropis(1)
        with pytest.raises(Warning):
            informador.obtenir_competencies_criteris(9999)


if __name__ == '__main__':

    pytest.main()
