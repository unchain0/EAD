import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import QSize


class HelloWindow(QMainWindow):
    def __init__(self) -> None:
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(280, 120))
        self.setWindowTitle("Olá, Mundo! Exemplo PyQT5")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        title = QLabel("Olá Mundo para PyQt", self)
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        grid_layout.addWidget(title, 0, 0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit(app.exec_())
