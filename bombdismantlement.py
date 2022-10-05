from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_bombdismantlement import *
import sys

class BombDis(QMainWindow,Ui_Bombdismantlement):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password_ = ""
        self.password.setDigitCount(10)
        self.password.setEnabled(False)
        self.one.clicked.connect(self.one_add)
        self.two.clicked.connect(self.two_add)
        self.three.clicked.connect(self.three_add)
        self.four.clicked.connect(self.four_add)
        self.five.clicked.connect(self.five_add)
        self.six.clicked.connect(self.six_add)
        self.seven.clicked.connect(self.seven_add)
        self.eight.clicked.connect(self.eight_add)
        self.nine.clicked.connect(self.nine_add)
        self.zero.clicked.connect(self.zero_add)
        self.show()
    def one_add(self):
        self.password_=self.password_+"1"
        self.update_password()
    def two_add(self):
        self.password_=self.password_+"2"
        self.update_password()
    def three_add(self):
        self.password_=self.password_+"3"
        self.update_password()
    def four_add(self):
        self.password_=self.password_+"4"
        self.update_password()
    def five_add(self):
        self.password_=self.password_+"5"
        self.update_password()
    def six_add(self):
        self.password_=self.password_+"6"
        self.update_password()
    def seven_add(self):
        self.password_=self.password_+"7"
        self.update_password()
    def eight_add(self):
        self.password_=self.password_+"8"
        self.update_password()
    def nine_add(self):
        self.password_=self.password_+"9"
        self.update_password()
    def zero_add(self):
        self.password_=self.password_+"0"
        self.update_password()
    def update_password(self):
        self.password.display(self.password_)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BombDis()
    sys.exit(app.exec_())
