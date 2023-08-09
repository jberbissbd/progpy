from typing import List, Dict, Any
import dataclasses
from decimal import ROUND_UP
import math
import os
import sys
from dataclasses import asdict
from xml.etree.ElementTree import tostring
from PySide6.QtWidgets import QDialog, QApplication, QTreeWidget, QHBoxLayout, QTreeWidgetItem, QVBoxLayout, QComboBox, QWidget, QPushButton, QSpacerItem, QSizePolicy, QAbstractItemView, QSpacerItem
from PySide6.QtCore import Qt, QSize
from PySide6 import QtCore, QtWidgets
from tomlkit import key
from PySide6.QtWidgets import QAbstractItemView

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class WidgetArbre(QtWidgets.QTreeWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setStyleSheet("QTreeView::item { padding: 10px }height:{QFontInfo(self.font()).pixelSize() * 2}px")
        self.setWordWrap(True)
        self.sizeHintForRow(300)
        self.setDragEnabled(True)
        self.setAlternatingRowColors(True)
        self.setColumnCount(3)
        self.setColumnHidden(2, True)
        self.setAcceptDrops(True)
        self.setWordWrap(True)

    def dropEvent(self, event):
        if event.source() == self:
            event.setDropAction(QtCore.Qt.MoveAction)
            super().dropEvent(event)
        else:
            event.setDropAction(QtCore.Qt.CopyAction)
            super().dropEvent(event)

    def mimeData(self, indexes):
        mime_data = super().mimeData(indexes)
        # Add custom data to mime data
        # Include information about the item and its child items
        return mime_data

    def dropMimeData(self, data, action, row, column):
        # Handle the dropped mime data
        return super().dropMimeData(data, action, row, column)
    