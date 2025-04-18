import sys
import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableView
)
from PySide6.QtCore import Qt, QAbstractTableModel
from utilitaires.data_utils import load_reservations

class PandasModel(QAbstractTableModel):
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self._df = df

    def rowCount(self, parent=None):
        return len(self._df)

    def columnCount(self, parent=None):
        return len(self._df.columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._df.iat[index.row(), index.column()]
            return str(value)
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._df.columns[section])
            if orientation == Qt.Vertical:
                return str(self._df.index[section])
        return None

class ReservationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Réservations")
        self.resize(600, 400)

        layout = QVBoxLayout(self)

        df = load_reservations("reservations.json")
        model = PandasModel(df)

        table = QTableView()
        table.setModel(model)
        table.resizeColumnsToContents()

        layout.addWidget(table)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReservationApp()
    window.show()
    sys.exit(app.exec())
