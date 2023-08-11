from PySide6.QtWidgets import QApplication, QMainWindow,QToolBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QCursor
import pyautogui


amp_limit = int(pyautogui.size()[0]*0.75)
alt_limit = int(pyautogui.size()[1]*0.75)


class FinestraPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Programacio didactica")
        self.resize(amp_limit, alt_limit)
        self.barra_lateral = QToolBar()
        self.barra_lateral.setOrientation(Qt.Orientation.Vertical)
        self.barra_lateral.setFloatable(False)
        self.addToolBar(self.barra_lateral)



if __name__ == "__main__":
    app = QApplication([])
    app.setStyle("Fusion")
    finestra = FinestraPrincipal()
    finestra.show()

    app.exec()
