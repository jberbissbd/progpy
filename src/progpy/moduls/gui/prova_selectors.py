from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QFormLayout, QComboBox, QDialog
from PySide6.QtWidgets import QStyleFactory
from PySide6.QtCore import (
    Qt, QSize, QPoint, QPointF, QRectF,
    QEasingCurve, QPropertyAnimation, QSequentialAnimationGroup,
    Slot, Property)

from botoanimat import AnimatedToggle

from PySide6.QtWidgets import QCheckBox
from PySide6.QtGui import QColor, QBrush, QPaintEvent, QPen, QPainter
encoding = "utf-8"

class Finestra(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccio de la materia per a la programacio didactica.")
        self.AmpladaMaxima = 200
        self.setMinimumSize(400, 300)
        self.layout = QVBoxLayout(self)
        self.DistribucioOpcions = QFormLayout()
        self.layout.addLayout(self.DistribucioOpcions)
        self.SelectorEtapa = QComboBox()
        self.SelectorEtapa.setMaximumWidth(self.AmpladaMaxima)
        self.SelectorModalitat = QComboBox()
        self.SelectorCurs = QComboBox()
        self.SelectorCurs.setPlaceholderText("Seleccioneu una etapa")
        self.SelectorCurs.setEnabled(False)
        self.SelectorCurs.setCurrentIndex(-1)
        self.SelectorCurs.setMaximumWidth(self.AmpladaMaxima)
        self.SelectorMateria = QComboBox()
        self.SelectorMateria.setEnabled(False)
        self.SelectorMateria.setPlaceholderText("Seleccioneu primer un curs")
        self.boto = AnimatedToggle()
        self.boto.setFixedWidth(60)
        self.boto.setFixedHeight(40)
        self.DistribucioOpcions.addRow("Boto", self.boto)
        self.DistribucioOpcions.setAlignment(Qt.AlignCenter)
        self.DistribucioOpcions.addRow("Etapa", self.SelectorEtapa)
        self.DistribucioOpcions.addRow("Modalitat", self.SelectorModalitat)
        self.DistribucioOpcions.setRowVisible(self.SelectorModalitat, False)
        self.DistribucioOpcions.addRow("Curs", self.SelectorCurs)
        self.DistribucioOpcions.addRow("Materia", self.SelectorMateria)
        self.afegir_valors()
        self.SelectorEtapa.currentIndexChanged.connect(self.visibilitat_modalitat)
        self.SelectorCurs.currentIndexChanged.connect(self.activacioMateria)
        self.boto.stateChanged.connect(self.valors_boto)

    def afegir_valors(self):
        self.SelectorEtapa.addItems(["Eso", "Batxillerat"])
        self.SelectorEtapa.setCurrentIndex(-1)
        self.SelectorMateria.addItem("mATEMÀTIQUES")

    def visibilitat_modalitat(self):
        self.SelectorMateria.setEnabled(False)
        self.SelectorMateria.setCurrentIndex(-1)
        if self.SelectorEtapa.currentIndex() == 1:
            self.DistribucioOpcions.setRowVisible(self.SelectorModalitat, True)
            self.SelectorCurs.setEnabled(False)
            self.SelectorCurs.setCurrentIndex(-1)
        else:
            self.DistribucioOpcions.setRowVisible(self.SelectorModalitat, False)
            self.SelectorCurs.setEnabled(True)
            self.SelectorCurs.clear()
            self.SelectorCurs.addItems(["1ER", "2n"])

    def activacion_curs(self):
        self.SelectorCurs.setEnabled(True)

    def activacioMateria(self):
        if self.SelectorCurs.currentIndex() != -1:
            self.SelectorMateria.setEnabled(True)


    def valors_boto(self):
        if self.boto.isChecked():
            print("Activat")
        else:
            print("Desactivat")

if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = Finestra()
    finestra.show()

    app.exec()
