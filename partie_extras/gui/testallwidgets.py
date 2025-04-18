# https://www.pythonguis.com/tutorials/pyside6-widgets/

import sys

from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

class HDial(QDial):
    def __init__(self):
        super().__init__()
        self.setNotchesVisible(True)

    def on_dialed_changed(self):
        print(self.value())


class HoverButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setMouseTracking(True)


    def enterEvent(self, event):
        super().enterEvent(event)
        self.setText("Clicked Me + ENTERED")

    def leaveEvent(self, event):
        super().leaveEvent(event)
        self.setText("Clicked Me")



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout()
        widgets = [
            QCheckBox,
            QComboBox,
            QDateEdit,
            QDateTimeEdit,
            HDial,
            QDoubleSpinBox,
            QFontComboBox,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
        ]

        for widget in widgets:
            w = widget()
            if isinstance(w, QDial):
                    w.setMinimum(0)
                    w.setMaximum(100)
                    w.setValue(50)
                    w.valueChanged.connect(w.on_dialed_changed)

            layout.addWidget(widget())


        mybutton = HoverButton("Click Me")
        mybutton.clicked.connect(self.activer_bouton)
        layout.addWidget(mybutton)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)
    def activer_bouton(self):
        print("Le bouton a ete active")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()