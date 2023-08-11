import os
import sys
import pyautogui
import math

from PySide6.QtWidgets import QApplication, QWidget

amplada_maxima = pyautogui.size()[0] * 0.75
alçada_maxima = pyautogui.size()[1] * 0.75


class Finestra(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Prova per a la mida")
        self.resize(math.ceil(amplada_maxima), math.ceil(alçada_maxima))


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = Finestra()
    finestra.show()

    app.exec()
