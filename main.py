from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from arayuz import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_sum)

    def calculate_sum(self):
        sayi1 = int(self.ui.lineEdit.text())
        sayi2 = int(self.ui.lineEdit_2.text())
        sonuc = sayi1 + sayi2
        self.ui.lineEdit_3.setText(str(sonuc))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
