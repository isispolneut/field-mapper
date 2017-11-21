from control import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore

import sys, esp300, gauss460, time

import numpy as np

class RobotControl(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        super(RobotControl, self).setupUi(self)

        self.esp = esp300.esp300(1,0)
        self.gauss = gauss460.gauss460(8,1)

        self.scanning = False

        pos_updater = QtCore.QTimer(self)
        # Inline declaration preferred over lambda to allow spreading
        # over multiple lines, so as not to have a gigantic line.
        # I can add the field updating here too.
        def update():
            if not self.scanning:
                self.a1_pos.setText(str(self.esp.axis1.pos) + " mm")
                self.a2_pos.setText(str(self.esp.axis2.pos) + " mm")
                self.a3_pos.setText(str(self.esp.axis3.pos) + " mm")

                field = self.gauss.allf()

                self.x_val.setText(str(field[0]))
                self.y_val.setText(str(field[1]))
                self.z_val.setText(str(field[2]))
                self.mag_val.setText(str(field[3]))

        pos_updater.timeout.connect(update)
        pos_updater.start(100)

        # Axis 1 Controls

        self.a1_left.clicked.connect(
            lambda _: setattr(self.esp.axis1, 'pos', self.esp.axis1.pos - self.a1_step.value())
        )
        self.a1_right.clicked.connect(
            lambda _: setattr(self.esp.axis1, 'pos', self.esp.axis1.pos + self.a1_step.value())
        )
        self.a1_zero.clicked.connect(
            lambda _: self.esp.axis1.go_home()
        )

        # Axis 2 Controls

        self.a2_left.clicked.connect(
            lambda _: setattr(self.esp.axis2, 'pos', self.esp.axis2.pos - self.a2_step.value())
        )
        self.a2_right.clicked.connect(
            lambda _: setattr(self.esp.axis2, 'pos', self.esp.axis2.pos + self.a2_step.value())
        )
        self.a2_zero.clicked.connect(
            lambda _: self.esp.axis2.go_home()
        )

        # Axis 3 Controls

        self.a3_left.clicked.connect(
            lambda _: setattr(self.esp.axis3, 'pos', self.esp.axis3.pos - self.a3_step.value())
        )
        self.a3_right.clicked.connect(
            lambda _: setattr(self.esp.axis3, 'pos', self.esp.axis3.pos + self.a3_step.value())
        )
        self.a3_zero.clicked.connect(
            lambda _: self.esp.axis3.go_home()
        )

        self.auto_savedir_button.clicked.connect(self.set_savedir)

        def scan():
            if self.quantity_combo.currentText() == "Gradient":
                self.scan_volume_gradient()
            elif self.quantity_combo.currentText() == "Field":
                self.scan_volume_field()        
        self.auto_scan.clicked.connect(scan)

    def set_savedir(self):
         self.fn = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
         self.auto_savedir.setText(self.fn)

    def scan_volume_gradient(self):
        self.scanning = True

        dim1 = int((abs(self.a1_max.value() - self.a1_min.value()))/ self.a1_step.value())
        dim2 = int((abs(self.a2_max.value() - self.a2_min.value()))/ self.a2_step.value())
        dim3 = int((abs(self.a3_max.value() - self.a3_min.value()))/ self.a3_step.value())

        grad_mag = np.zeros((dim1+1,dim2+1,dim3+1))
        i=0
        j=0
        k=0

        for x in np.linspace(self.a1_min.value(), self.a1_max.value(), num=dim1+1):
            j=0
            for y in np.linspace(self.a2_min.value(), self.a2_max.value(), num=dim2+1):
                k=0
                for z in np.linspace(self.a3_min.value(), self.a3_max.value(), num=dim3+1):
                    try:
                        x_grad = []
                        y_grad = []
                        z_grad = []

                        grad = []

                        self.esp.axis1.pos = x
                        self.esp.axis2.pos = y
                        self.esp.axis3.pos = z

                        self.esp.axis1.pos = x - self.a1_step.value()
                        x_grad.append(self.gauss.field)
                        self.esp.axis1.pos = x + self.a1_step.value()
                        x_grad.append(self.gauss.field)
                        self.esp.axis1.pos = x

                        grad.append((x_grad[1] - x_grad[0])/(2*(self.a1_step.value()*1e-3)))

                        self.esp.axis2.pos = y - self.a2_step.value()
                        y_grad.append(self.gauss.field)
                        self.esp.axis2.pos = y + self.a2_step.value()
                        y_grad.append(self.gauss.field)
                        self.esp.axis2.pos = y

                        grad.append((y_grad[1]-y_grad[0])/(2*(self.a2_step.value()*1e-3)))

                        self.esp.axis3.pos = z - self.a3_step.value()
                        z_grad.append(self.gauss.field)
                        self.esp.axis3.pos = z + self.a3_step.value()
                        z_grad.append(self.gauss.field)
                        self.esp.axis3.pos = z

                        grad.append((z_grad[1]-z_grad[0])/(2*(self.a3_step.value()*1e-3)))

                        grad_mag[i,j,k] = np.sqrt(grad[0]**2+grad[1]**2+grad[2]**2)
                    except Exception as ex:
                        print("Caught an error, skipping point")
                        print(ex)
                        np.save(self.fn + "/grad.errbak",grad_mag)

                    k+=1
                j+=1
            i+=1

        np.save(self.fn + "/grad",grad_mag)

        self.scanning = False

    def scan_volume_field(self):

        dim1 = int((abs(self.a1_max.value() - self.a1_min.value()))/ self.a1_step.value())
        dim2 = int((abs(self.a2_max.value() - self.a2_min.value()))/ self.a2_step.value())
        dim3 = int((abs(self.a3_max.value() - self.a3_min.value()))/ self.a3_step.value())

        grad_mag = np.zeros((dim1+1,dim2+1,dim3+1))
        i=0
        j=0
        k=0

        for x in np.linspace(self.a1_min.value(), self.a1_max.value(), num=dim1+1):
            j=0
            for y in np.linspace(self.a2_min.value(), self.a2_max.value(), num=dim2+1):
                k=0
                for z in np.linspace(self.a3_min.value(), self.a3_max.value(), num=dim3+1):
                    x_grad = []
                    y_grad = []
                    z_grad = []

                    grad = []

                    self.esp.axis1.pos = x
                    self.esp.axis2.pos = y
                    self.esp.axis3.pos = z

                    grad_mag[i,j,k] = self.gauss.field

                    k+=1
                j+=1
            i+=1

        np.save(self.fn + "/grad",grad_mag)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    aw = RobotControl()

    aw.show()
    sys.exit(app.exec_())
