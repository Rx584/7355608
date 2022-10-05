from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_bombdismantlement import *
import sys

class BombDis(QMainWindow,Ui_Bombdismantlement):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BombDis()
    sys.exit(app.exec_())
