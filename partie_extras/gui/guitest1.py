from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout,
    QTableView, QSplitter, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys
import pandas as pd
from data_source import get_sample_dataframe


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Interface PySide6 avec séparation verticale")
        self.resize(900, 600)

        # Splitter principal
        splitter = QSplitter(Qt.Horizontal)

        # Partie gauche : contrôles
        left_frame = QFrame()
        left_layout = QVBoxLayout()

        self.button1 = QPushButton("Bouton 1")
        self.button2 = QPushButton("Bouton 2")
        self.textfield1 = QLineEdit()
        self.textfield1.setPlaceholderText("Texte 1")
        self.textfield2 = QLineEdit()
        self.textfield2.setPlaceholderText("Texte 2")
        self.quit_button = QPushButton("Quitter")
        self.quit_button.clicked.connect(QApplication.instance().quit)

        for widget in [self.button1, self.button2, self.textfield1, self.textfield2, self.quit_button]:
            left_layout.addWidget(widget)

        left_layout.addStretch()
        left_frame.setLayout(left_layout)

        # Partie droite : tableau
        right_frame = QFrame()
        right_layout = QVBoxLayout()

        self.table = QTableView()
        self.model = self.create_model_from_dataframe(get_sample_dataframe())
        self.table.setModel(self.model)
        right_layout.addWidget(self.table)
        right_frame.setLayout(right_layout)

        # Ajouter au splitter
        splitter.addWidget(left_frame)
        splitter.addWidget(right_frame)
        splitter.setSizes([200, 700])

        # Layout principal
        main_layout = QHBoxLayout()
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def create_model_from_dataframe(self, df: pd.DataFrame) -> QStandardItemModel:
        model = QStandardItemModel(df.shape[0], df.shape[1])
        model.setHorizontalHeaderLabels(df.columns.tolist())

        for row in range(df.shape[0]):
            for col in range(df.shape[1]):
                item = QStandardItem(str(df.iat[row, col]))
                model.setItem(row, col, item)

        return model


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
