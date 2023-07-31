from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QFormLayout, QComboBox
from PySide6.QtWidgets import QStyleFactory


class Finestra(QWidget):
    def __init__(self):
        super().__init__()
        self.AmpladaMaxima = 200
        self.setMinimumSize(800, 600)
        self.layout = QVBoxLayout(self)
        self.DistribucioOpcions = QFormLayout()
        self.layout.addLayout(self.DistribucioOpcions)
        self.SelectorEtapa = QComboBox()
        self.SelectorEtapa.setMaximumWidth(self.AmpladaMaxima)
        self.SelectorModalitat = QComboBox()
        self.SelectorCurs = QComboBox()
        self.SelectorCurs.setPlaceholderText("Seleccioneu primer una etapa")
        self.SelectorCurs.setEnabled(False)
        self.SelectorCurs.setMaximumWidth(100)
        self.SelectorMateria = QComboBox()
        self.SelectorMateria.setPlaceholderText("Seleccioneu primer un curs")
        self.DistribucioOpcions.addRow("Etapa", self.SelectorEtapa)
        self.DistribucioOpcions.addRow("Modalitat", self.SelectorModalitat)
        self.DistribucioOpcions.setRowVisible(self.SelectorModalitat, False)
        self.DistribucioOpcions.addRow("Curs", self.SelectorCurs)
        self.DistribucioOpcions.addRow("Materia", self.SelectorMateria)
        self.afegir_valors()
        self.SelectorEtapa.currentIndexChanged.connect(self.visibilitat_modalitat)

    def afegir_valors(self):
        self.SelectorEtapa.addItems(["Eso", "Batxillerat"])
        self.SelectorEtapa.setCurrentIndex(-1)

    def visibilitat_modalitat(self):
        print(self.SelectorEtapa.currentIndex())
        if self.SelectorEtapa.currentIndex() == 1:
            self.DistribucioOpcions.setRowVisible(self.SelectorModalitat, True)
        else:
            self.DistribucioOpcions.setRowVisible(self.SelectorModalitat, False)
            self.SelectorCurs.setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = Finestra()
    finestra.show()

    app.exec()
