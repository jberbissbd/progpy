import dataclasses
import os
import sys
from dataclasses import asdict
from xml.etree.ElementTree import tostring
from PySide6.QtWidgets import QDialog, QApplication, QTreeWidget, QHBoxLayout, QTreeWidgetItem
from PySide6.QtCore import Qt
from tomlkit import key


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bbdd.curriculum import Lectorcriteris, Lectorcompetencies, InformadorMateriaPlantilla

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
        self.dades_originals = QTreeWidget()
        self.dades_originals.setAlternatingRowColors(True)
        self.dades_originals.setColumnCount(3)
        self.dades_originals.setHeaderLabels(["ID","Nom", "Descripció"])
        self.distribucio.addWidget(self.dades_originals)
        self.afegir_dades()
        self.dades_originals.clicked.connect(self.seleccio_valors)

    def afegir_dades(self):
        dades = conversioarbre(InformadorMateriaPlantilla(0).obtenir_competencies_criteris(1))
        items = []
        for clau, values in dades.items():
            valor_actual = values['num']
            clau_actual = str(clau)
            text_competencia = f"Competencia {valor_actual}"
            descripcio = values['descripcio']
            item = QTreeWidgetItem([clau_actual, text_competencia, descripcio])
            for value in values:
                print(value[1])

            items.append(item)
        self.dades_originals.insertTopLevelItems(0, items)
    
    def seleccio_valors(self):
        print(self.dades_originals.currentColumn(),self.dades_originals.currentIndex().row())



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = Finestra()
    finestra.show()

    app.exec()
