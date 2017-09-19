from control import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore

import sys, esp300

class RobotControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        super(RobotControl, self).setupUi(self)

        esp = esp300.esp300(1)

        pos_updater = QtCore.QTimer(self)
        # Inline declaration preferred over lambda to allow spreading
        # over multiple lines, so as not to have a gigantic line
        def pos_update():
            self.a1_pos.setText(str(esp.axis1.pos))
            self.a2_pos.setText(str(esp.axis2.pos))
            self.a3_pos.setText(str(esp.axis3.pos))
        pos_updater.timeout.connect(pos_update)
        pos_updater.start(100)

        # Axis 1 Controls

        self.a1_left.clicked.connect(
            lambda _: esp.axis1.pos-=self.a1_step.value()
        )
        self.a1_right.clicked.connect(
            lambda _: esp.axis1.pos+=self.a1_step.value()
        )
        self.a1_zero.clicked.connect(
            lambda _: esp.axis1.go_home()
        )

        # Axis 2 Controls

        self.a2_left.clicked.connect(
            lambda _: esp.axis2.pos-=self.a2_step.value()
        )
        self.a2_right.clicked.connect(
            lambda _: esp.axis2.pos+=self.a2_step.value()
        )
        self.a2_zero.clicked.connect(
            lambda _: esp.axis2.go_home()
        )

        # Axis 3 Controls

        self.a3_left.clicked.connect(
            lambda _: esp.axis3.pos-=self.a3_step.value()
        )
        self.a3_right.clicked.connect(
            lambda _: esp.axis3.pos+=self.a3_step.value()
        )
        self.a3_zero.clicked.connect(
            lambda _: esp.axis3.go_home()
        )


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aw = RobotControl()

    aw.show()
    sys.exit(app.exec_())
