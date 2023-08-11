import dataclasses
from decimal import ROUND_UP
import math
import os
import sys
from dataclasses import asdict
from xml.etree.ElementTree import tostring
from PySide6.QtWidgets import QDialog, QApplication, QTreeWidget, QHBoxLayout, QTreeWidgetItem, QVBoxLayout, QComboBox, QWidget, QPushButton, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QSize
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


class Finestra(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccio de la materia per a la programacio didactica.")
        self.AmpladaMaxima = 200
        self.setMinimumSize(400, 300)
        self.distribucio = QHBoxLayout()
        self.setLayout(self.distribucio)
        self.distribucio_competencies = QVBoxLayout()
        self.disposicio_botons = QVBoxLayout()
        self.botons_espaciador = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.distribucio.addLayout(self.distribucio_competencies)
        self.distribucio.addLayout(self.disposicio_botons)
        self.boto_afegir = QPushButton("Afegir")
        self.boto_eliminar = QPushButton("Eliminar")
        self.disposicio_botons.addWidget(self.boto_afegir)
        self.disposicio_botons.addWidget(self.boto_eliminar)
        self.disposicio_botons.addSpacerItem(self.botons_espaciador)
        self.dades_curriculum = QTreeWidget()
        self.dades_curriculum.setStyleSheet("QTreeView::item { padding: 10px }height:{QFontInfo(self.font()).pixelSize() * 2}px")
        self.dades_curriculum.setWordWrap(True)
        self.dades_curriculum.sizeHintForRow(300)
        self.dades_programacio = QTreeWidget()
        self.dades_programacio.setAlternatingRowColors(True)
        self.dades_programacio.setColumnCount(3)
        self.dades_programacio.setHeaderLabels(["Competencia", "Descripció", "ID"])
        self.dades_programacio.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dades_programacio.setColumnHidden(2, True)
        self.dades_programacio.setWordWrap(True)
        self.distribucio.addWidget(self.dades_programacio)
        self.selector_materia = QComboBox()
        self.selector_materia.currentIndexChanged.connect(self.canvi_materia_seleccionada)
        self.selector_materia.setPlaceholderText("Seleccioneu primer una materia")
        self.selector_materia.showPopup()
        self.distribucio_competencies.addWidget(self.selector_materia)
        self.distribucio_competencies.addWidget(self.dades_curriculum)
        self.dades_curriculum.setAlternatingRowColors(True)
        self.dades_curriculum.setColumnCount(3)
        self.dades_curriculum.setHeaderLabels(["Competencia", "Descripció", "ID"])
        self.dades_curriculum.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.dades_curriculum.setColumnHidden(2, True)
        self.generar_opcions_materies()
        self.boto_afegir.clicked.connect(self.afegir_criteris)
        self.boto_eliminar.clicked.connect(self.eliminar_elements)

    def generar_opcions_materies(self):
        self.dades_selector_materia = LectorMateriesCompletes(0).obtenir_materies()
        self.dades_selector_materia = [element.__dict__ for element in self.dades_selector_materia]
        for materia in self.dades_selector_materia:
            self.selector_materia.addItem(materia["nom"], materia["id_materia"])

    def canvi_materia_seleccionada(self):
        valor_actual = self.selector_materia.currentIndex()
        id = self.dades_selector_materia[valor_actual]["id_materia"]
        self.afegir_dades(id)

    def afegir_dades(self, materia):
        self.dades_curriculum.clear()
        self.dades_programacio.clear()
        dades = conversioarbre(InformadorMateriaPlantilla(0).obtenir_competencies_criteris(materia))
        items = []
        for clau, values in dades.items():
            # Afegim les dades del diccionari corresponent
            valor_actual = str(values['num'])
            clau_actual = str(clau)
            descripcio = values['descripcio']
            calcul_alçada = len(descripcio)/30
            criteris = values['criteris']
            self.dades_curriculum.setColumnWidth(0, 90)
            item = QTreeWidgetItem([valor_actual, descripcio, clau_actual])
            item.setSizeHint(0, QSize(310, math.ceil(calcul_alçada)*11))
            for element in criteris.values():
                id_criteri = element['id']
                text_criteri = f"{valor_actual}.{element['num']}: {element['descripcio']}"
                nou_item = QTreeWidgetItem(["", text_criteri, str(id_criteri)], type=10)            
                nombre_files = (math.ceil(len(text_criteri)/30))
                nou_item.setSizeHint(0, QSize(310, nombre_files*12))
                item.addChild(nou_item)
            items.append(item)
        self.dades_curriculum.insertTopLevelItems(0, items)



    def afegir_criteris(self):
        """Afegir criteris a l'arbre"""

            
        def presencia_subitem():
            """Retorna True si existeix element a afegir"""
            # Comprovem tots els elements arrel del widget:
            if self.dades_programacio.topLevelItemCount() == 0:
                return False
            # Comprovem que no existeixi element a afegir:
            for item in range(0, self.dades_programacio.invisibleRootItem().childCount()):
                for subitem in range(0, self.dades_programacio.topLevelItem(item).childCount()):
                    if self.dades_programacio.topLevelItem(item).child(subitem).text(1) == self.dades_curriculum.currentItem().text(1):
                        return True
            return False
            # Si coincideix amb el text de l'element superior, no s'afegeix:
        
        def comprovar_pares():
            """Retorna True si existeix element pare a afegir"""
            # Comprovem tots els elements arrel del widget:
            if self.dades_programacio.topLevelItemCount() == 0:
                return False
            for item in range(0, self.dades_programacio.topLevelItemCount()):
                # Comprovem que hi hagin elements pare:
                if self.dades_programacio.topLevelItem(item).text(1) == \
                        self.dades_curriculum.currentItem().parent().text(1):
                    return True
            return False

        if self.dades_curriculum.currentItem() is not None:
            element_afegir = self.dades_curriculum.currentItem()
            elements_presents = self.dades_programacio.findItems(element_afegir.text(1), Qt.MatchExactly, column=1)
            if element_afegir.type() == 0:
                if elements_presents == [] or element_afegir.text(1) not in elements_presents[0].text(1):
                    # "Clonem" l'element actual:
                    nou_element = QTreeWidgetItem([element_afegir.text(0), element_afegir.text(1), element_afegir.text(2)], type=0)
                    calcul_alçada_nou_element = len(nou_element.text(1))/30
                    nou_element.setSizeHint(0, QSize(310, math.ceil(calcul_alçada_nou_element)*11))
                    # Copiem els elements fills de l'element actual:
                    for fill in range(0, element_afegir.childCount()):
                        nou_fill = QTreeWidgetItem([element_afegir.child(fill).text(0),
                                                    element_afegir.child(fill).text(1), element_afegir.child(fill).text(2)], type=10)
                        calcul_alçada_nou_fill = len(nou_fill.text(1))/30
                        nou_fill.setSizeHint(0, QSize(310, math.ceil(calcul_alçada_nou_fill)*11))
                        nou_element.addChild(nou_fill)
                    self.dades_programacio.insertTopLevelItem(0, nou_element)


            # Si és un sub-item, el tipus és 0:
            elif element_afegir.type() == 10:
                item_pare = element_afegir.parent()
                # Comprovem que l'element no existeixi:
                if presencia_subitem() is False:
                    # Utilitzem aquesta manera perquè si no, no es copia el paràmetre type, encara que s'utilitzi
                    # el mètod clone:
                    nou_fill = QTreeWidgetItem([element_afegir.text(0), element_afegir.text(1), element_afegir.text(2)], type=10)
                    calcul_alçada_nou_fill = len(nou_fill.text(1))/30
                    nou_fill.setSizeHint(0, QSize(310, math.ceil(calcul_alçada_nou_fill)*11))
                    # Comprovem que l'element arrel no existeixi:
                    if comprovar_pares() is False:
                    # Si no existeix, se'n fa una copia, però incloent tan sols el subelement:
                        nou_pare = QTreeWidgetItem([item_pare.text(0), item_pare.text(1), item_pare.text(2)], type=0)
                        nou_pare.addChild(nou_fill)
                        calcul_alçada_nou_pare = len(nou_pare.text(1))/30
                        nou_pare.setSizeHint(0, QSize(310, math.ceil(calcul_alçada_nou_pare)*11))
                        self.dades_programacio.insertTopLevelItem(0, nou_pare)
                    elif comprovar_pares() is True:
                    # Si existeix, s'adjunta al ja existent:
                        self.dades_programacio.findItems(item_pare.text(1), Qt.MatchExactly, column=1)[0].addChild(nou_fill)
            self.dades_programacio.sortByColumn(0, Qt.AscendingOrder)
            llista_afegir = []
            for num_item_pare in range(self.dades_programacio.topLevelItemCount()):
                id_pare = [int(self.dades_programacio.topLevelItem(num_item_pare).text(2))]
                ids_fills = [int(self.dades_programacio.topLevelItem(num_item_pare).child(fill).text(2)) for fill in \
                             range(self.dades_programacio.topLevelItem(num_item_pare).childCount())]
                id_pare.append(ids_fills)
                llista_afegir.append(id_pare)
            print(llista_afegir)


    def eliminar_elements(self):
        
        def recull_elements_post_eliminar():
            llista_eliminar = []
            for num_item_pare in range(self.dades_programacio.topLevelItemCount()):
                id_pare = [int(self.dades_programacio.topLevelItem(num_item_pare).text(2))]
                ids_fills = [int(self.dades_programacio.topLevelItem(num_item_pare).child(fill).text(2)) for fill in \
                            range(self.dades_programacio.topLevelItem(num_item_pare).childCount())]
                id_pare.append(ids_fills)
                llista_eliminar.append(id_pare)
            print(llista_eliminar)
        
        element_eliminar = self.dades_programacio.currentItem()
        print(element_eliminar.type())
        if element_eliminar.type() == 0:
            self.dades_programacio.takeTopLevelItem(self.dades_programacio.indexOfTopLevelItem(element_eliminar))
            recull_elements_post_eliminar()
        elif element_eliminar.type() == 10:
            index_element_eliminar = self.dades_programacio.currentItem().parent().indexOfChild(element_eliminar)
            index_pare = self.dades_programacio.indexOfTopLevelItem(element_eliminar.parent())
            self.dades_programacio.topLevelItem(index_pare).takeChild(index_element_eliminar)
            if self.dades_programacio.topLevelItem(index_pare).childCount() == 0:
                self.dades_programacio.takeTopLevelItem(index_pare)
            recull_elements_post_eliminar()


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = Finestra()
    finestra.show()

    app.exec()
