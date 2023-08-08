import dataclasses
import os
import sys
from dataclasses import asdict
from xml.etree.ElementTree import tostring
from PySide6.QtWidgets import QDialog, QApplication, QTreeWidget, QHBoxLayout, QTreeWidgetItem, QVBoxLayout, QComboBox
from PySide6.QtCore import Qt
from tomlkit import key

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bbdd.curriculum import Lectorcriteris, Lectorcompetencies, InformadorMateriaPlantilla, LectorMateriesCompletes


def conversioarbre(arbre: list):
    llista_arbre = {}
    for items in arbre:
        # Convertim el primer nivell del missatge en diccionari:
        items = items.__dict__
        llista_arbre[items["id"]] = items
    # Iterem per convertir cada element de la llista de criteris en diccionari
    for item in llista_arbre.values():
        criteris_dict = {}
        for element in item["criteris"]:
            element = element.__dict__
            criteris_dict[element["id"]] = element
        item["criteris"] = criteris_dict
    return llista_arbre


class Finestra(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccio de la materia per a la programacio didactica.")
        self.AmpladaMaxima = 200
        self.setMinimumSize(400, 300)
        self.distribucio = QHBoxLayout()
        self.setLayout(self.distribucio)
        self.distribucio_competencies = QVBoxLayout()
        self.distribucio.addLayout(self.distribucio_competencies)
        self.dades_originals = QTreeWidget()
        self.selector_materia = QComboBox()
        self.selector_materia.currentIndexChanged.connect(self.canvi_materia_seleccionada)
        self.selector_materia.setPlaceholderText("Seleccioneu primer una materia")
        self.selector_materia.showPopup()
        self.distribucio_competencies.addWidget(self.selector_materia)
        self.distribucio_competencies.addWidget(self.dades_originals)
        self.dades_originals.setAlternatingRowColors(True)
        self.dades_originals.setColumnCount(3)
        self.dades_originals.setHeaderLabels(["Competencia", "Descripció", "ID"])
        self.dades_originals.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dades_originals.setColumnHidden(2, True)
        self.generar_opcions_materies()
        self.dades_originals.clicked.connect(self.seleccio_valors)

    def generar_opcions_materies(self):
        self.dades_selector_materia = LectorMateriesCompletes(0).obtenir_materies()
        self.dades_selector_materia = [element.__dict__ for element in self.dades_selector_materia]
        print(self.dades_selector_materia)
        for materia in self.dades_selector_materia:
            self.selector_materia.addItem(materia["nom"], materia["id_materia"])

    def canvi_materia_seleccionada(self):
        valor_actual = self.selector_materia.currentIndex()
        id = self.dades_selector_materia[valor_actual]["id_materia"]
        self.afegir_dades(id)

    def afegir_dades(self, materia):
        self.dades_originals.clear()
        dades = conversioarbre(InformadorMateriaPlantilla(0).obtenir_competencies_criteris(materia))
        items = []
        for clau, values in dades.items():
            # Afegim les dades del diccionari corresponent
            valor_actual = str(values['num'])
            clau_actual = str(clau)
            text_competencia = f"Competencia {valor_actual}"
            descripcio = values['descripcio']
            criteris = values['criteris']
            self.dades_originals.setColumnWidth(0, 90)
            item = QTreeWidgetItem([valor_actual, descripcio, clau_actual])
            for element in criteris.values():
                id_criteri = element['id']
                text_criteri = f"{valor_actual}.{element['num']}: {element['descripcio']}"
                nou_item = QTreeWidgetItem(["", text_criteri, str(id_criteri)])
                item.addChild(nou_item)
            items.append(item)
        self.dades_originals.insertTopLevelItems(0, items)

    def seleccio_valors(self):
        print(self.dades_originals.currentIndex().row())


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = Finestra()
    finestra.show()

    app.exec()
