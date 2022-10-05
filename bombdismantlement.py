from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_bombdismantlement import *
import os
import sys

class BombDis(QMainWindow,Ui_Bombdismantlement):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.password_ = ""
        self.timer=QTimer()
        self.remtime = 180
        self.bomb_state = False
        self.disbomb.setEnabled(False)
        self.password.setDigitCount(10)
        self.time.setDigitCount(10)
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
        self.timer.timeout.connect(self.update_time)
        self.set_bomb.clicked.connect(self.set_pw)
        self.disbomb.clicked.connect(self.dis_bomb)
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
    def set_pw(self):
        if not(self.bomb_state):
            self.pw = self.password_
            self.password_ = ""
            self.set_bomb.text = "拆弹"
            QMessageBox.information(self,"设置完成","炸弹设置完成，将在180秒后爆炸")
            self.disbomb.setEnabled(True)
            self.bomb_state = True
            self.set_bomb.setEnabled(False)
            self.update_password()
            self.timer.start(1000)
    def update_time(self):
        if self.retime <=0:
            QMessageBox.information(self,"yui~a~Boom!","拆弹失败，电脑将在5秒后关机")
            self.shutdown()
        self.remtime -=1
        self.time.display(self.remtime)
    def dis_bomb(self):
        if self.password_ == self.pw:
            self.timer.stop()
            QMessageBox.information(self,"成功","炸弹已拆除")
            self.zero.setEnabled(False)
            self.one.setEnabled(False)
            self.two.setEnabled(False)
            self.three.setEnabled(False)
            self.four.setEnabled(False)
            self.five.setEnabled(False)
            self.six.setEnabled(False)
            self.seven.setEnabled(False)
            self.eight.setEnabled(False)
            self.nine.setEnabled(False)
            self.disbomb.setEnabled(False)
            self.password.display("BOMB DISED")
            self.time.display("BOMB DISED")
        else:
            QMessageBox.information(self,"错误","错误的拆弹密码")
            self.password_ = ""
            self.update_password()
    def shutdown(self):
        os.system("shutdown -s -t 5")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BombDis()
    sys.exit(app.exec_())
