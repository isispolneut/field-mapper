# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\control.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.a1_group = QtWidgets.QGroupBox(self.centralwidget)
        self.a1_group.setGeometry(QtCore.QRect(10, 10, 291, 111))
        self.a1_group.setObjectName("a1_group")
        self.a1_pos = QtWidgets.QLineEdit(self.a1_group)
        self.a1_pos.setEnabled(False)
        self.a1_pos.setGeometry(QtCore.QRect(140, 30, 141, 20))
        self.a1_pos.setObjectName("a1_pos")
        self.a1_pos_label = QtWidgets.QLabel(self.a1_group)
        self.a1_pos_label.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.a1_pos_label.setObjectName("a1_pos_label")
        self.a1_step_label = QtWidgets.QLabel(self.a1_group)
        self.a1_step_label.setGeometry(QtCore.QRect(140, 60, 47, 13))
        self.a1_step_label.setObjectName("a1_step_label")
        self.layoutWidget_3 = QtWidgets.QWidget(self.a1_group)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 20, 124, 83))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.a1_controls = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.a1_controls.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.a1_controls.setContentsMargins(0, 0, 0, 0)
        self.a1_controls.setObjectName("a1_controls")
        self.a1_right = QtWidgets.QToolButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a1_right.sizePolicy().hasHeightForWidth())
        self.a1_right.setSizePolicy(sizePolicy)
        self.a1_right.setObjectName("a1_right")
        self.a1_controls.addWidget(self.a1_right, 1, 2, 1, 1)
        self.a1_zero = QtWidgets.QToolButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a1_zero.sizePolicy().hasHeightForWidth())
        self.a1_zero.setSizePolicy(sizePolicy)
        self.a1_zero.setObjectName("a1_zero")
        self.a1_controls.addWidget(self.a1_zero, 1, 1, 1, 1)
        self.a1_left = QtWidgets.QToolButton(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a1_left.sizePolicy().hasHeightForWidth())
        self.a1_left.setSizePolicy(sizePolicy)
        self.a1_left.setObjectName("a1_left")
        self.a1_controls.addWidget(self.a1_left, 1, 0, 1, 1)
        self.a1_step = QtWidgets.QDoubleSpinBox(self.a1_group)
        self.a1_step.setGeometry(QtCore.QRect(140, 80, 141, 22))
        self.a1_step.setMinimum(0.0)
        self.a1_step.setMaximum(10.0)
        self.a1_step.setSingleStep(0.01)
        self.a1_step.setObjectName("a1_step")
        self.a3_group = QtWidgets.QGroupBox(self.centralwidget)
        self.a3_group.setGeometry(QtCore.QRect(10, 230, 291, 111))
        self.a3_group.setObjectName("a3_group")
        self.layoutWidget = QtWidgets.QWidget(self.a3_group)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 124, 83))
        self.layoutWidget.setObjectName("layoutWidget")
        self.a3_controls = QtWidgets.QGridLayout(self.layoutWidget)
        self.a3_controls.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.a3_controls.setContentsMargins(0, 0, 0, 0)
        self.a3_controls.setObjectName("a3_controls")
        self.a3_zero = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a3_zero.sizePolicy().hasHeightForWidth())
        self.a3_zero.setSizePolicy(sizePolicy)
        self.a3_zero.setObjectName("a3_zero")
        self.a3_controls.addWidget(self.a3_zero, 1, 1, 1, 1)
        self.a3_left = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a3_left.sizePolicy().hasHeightForWidth())
        self.a3_left.setSizePolicy(sizePolicy)
        self.a3_left.setObjectName("a3_left")
        self.a3_controls.addWidget(self.a3_left, 1, 0, 1, 1)
        self.a3_right = QtWidgets.QToolButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a3_right.sizePolicy().hasHeightForWidth())
        self.a3_right.setSizePolicy(sizePolicy)
        self.a3_right.setObjectName("a3_right")
        self.a3_controls.addWidget(self.a3_right, 1, 2, 1, 1)
        self.a3_pos = QtWidgets.QLineEdit(self.a3_group)
        self.a3_pos.setEnabled(False)
        self.a3_pos.setGeometry(QtCore.QRect(140, 30, 141, 20))
        self.a3_pos.setObjectName("a3_pos")
        self.a3_pos_label = QtWidgets.QLabel(self.a3_group)
        self.a3_pos_label.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.a3_pos_label.setObjectName("a3_pos_label")
        self.a3_step_label = QtWidgets.QLabel(self.a3_group)
        self.a3_step_label.setGeometry(QtCore.QRect(140, 60, 47, 13))
        self.a3_step_label.setObjectName("a3_step_label")
        self.a3_step = QtWidgets.QDoubleSpinBox(self.a3_group)
        self.a3_step.setGeometry(QtCore.QRect(140, 80, 141, 22))
        self.a3_step.setMinimum(0.0)
        self.a3_step.setMaximum(10.0)
        self.a3_step.setSingleStep(0.01)
        self.a3_step.setObjectName("a3_step")
        self.a2_group = QtWidgets.QGroupBox(self.centralwidget)
        self.a2_group.setGeometry(QtCore.QRect(10, 120, 291, 111))
        self.a2_group.setObjectName("a2_group")
        self.a2_pos = QtWidgets.QLineEdit(self.a2_group)
        self.a2_pos.setEnabled(False)
        self.a2_pos.setGeometry(QtCore.QRect(140, 30, 141, 20))
        self.a2_pos.setObjectName("a2_pos")
        self.a2_pos_label = QtWidgets.QLabel(self.a2_group)
        self.a2_pos_label.setGeometry(QtCore.QRect(140, 10, 47, 13))
        self.a2_pos_label.setObjectName("a2_pos_label")
        self.a2_step_label = QtWidgets.QLabel(self.a2_group)
        self.a2_step_label.setGeometry(QtCore.QRect(140, 60, 47, 13))
        self.a2_step_label.setObjectName("a2_step_label")
        self.layoutWidget_2 = QtWidgets.QWidget(self.a2_group)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 124, 83))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.a2_controls = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.a2_controls.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.a2_controls.setContentsMargins(0, 0, 0, 0)
        self.a2_controls.setObjectName("a2_controls")
        self.a2_right = QtWidgets.QToolButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2_right.sizePolicy().hasHeightForWidth())
        self.a2_right.setSizePolicy(sizePolicy)
        self.a2_right.setObjectName("a2_right")
        self.a2_controls.addWidget(self.a2_right, 1, 2, 1, 1)
        self.a2_zero = QtWidgets.QToolButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2_zero.sizePolicy().hasHeightForWidth())
        self.a2_zero.setSizePolicy(sizePolicy)
        self.a2_zero.setObjectName("a2_zero")
        self.a2_controls.addWidget(self.a2_zero, 1, 1, 1, 1)
        self.a2_left = QtWidgets.QToolButton(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.a2_left.sizePolicy().hasHeightForWidth())
        self.a2_left.setSizePolicy(sizePolicy)
        self.a2_left.setObjectName("a2_left")
        self.a2_controls.addWidget(self.a2_left, 1, 0, 1, 1)
        self.a2_step = QtWidgets.QDoubleSpinBox(self.a2_group)
        self.a2_step.setGeometry(QtCore.QRect(140, 80, 141, 22))
        self.a2_step.setMinimum(0.0)
        self.a2_step.setMaximum(10.0)
        self.a2_step.setSingleStep(0.01)
        self.a2_step.setObjectName("a2_step")
        self.auto_group = QtWidgets.QGroupBox(self.centralwidget)
        self.auto_group.setGeometry(QtCore.QRect(310, 10, 391, 161))
        self.auto_group.setObjectName("auto_group")
        self.auto_scan = QtWidgets.QPushButton(self.auto_group)
        self.auto_scan.setGeometry(QtCore.QRect(210, 130, 171, 23))
        self.auto_scan.setObjectName("auto_scan")
        self.layoutWidget1 = QtWidgets.QWidget(self.auto_group)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 371, 101))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.auto_to = QtWidgets.QLabel(self.layoutWidget1)
        self.auto_to.setObjectName("auto_to")
        self.gridLayout.addWidget(self.auto_to, 0, 2, 1, 1)
        self.auto_from = QtWidgets.QLabel(self.layoutWidget1)
        self.auto_from.setObjectName("auto_from")
        self.gridLayout.addWidget(self.auto_from, 0, 1, 1, 1)
        self.a1_label = QtWidgets.QLabel(self.layoutWidget1)
        self.a1_label.setObjectName("a1_label")
        self.gridLayout.addWidget(self.a1_label, 1, 0, 1, 1)
        self.a2_label = QtWidgets.QLabel(self.layoutWidget1)
        self.a2_label.setObjectName("a2_label")
        self.gridLayout.addWidget(self.a2_label, 2, 0, 1, 1)
        self.a3_label = QtWidgets.QLabel(self.layoutWidget1)
        self.a3_label.setObjectName("a3_label")
        self.gridLayout.addWidget(self.a3_label, 3, 0, 1, 1)
        self.a1_min = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.a1_min.setMinimum(-50.0)
        self.a1_min.setMaximum(50.0)
        self.a1_min.setObjectName("a1_min")
        self.gridLayout.addWidget(self.a1_min, 1, 1, 1, 1)
        self.a1_max = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.a1_max.setMinimum(-50.0)
        self.a1_max.setMaximum(50.0)
        self.a1_max.setObjectName("a1_max")
        self.gridLayout.addWidget(self.a1_max, 1, 2, 1, 1)
        self.a2_min = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.a2_min.setMinimum(-50.0)
        self.a2_min.setMaximum(50.0)
        self.a2_min.setObjectName("a2_min")
        self.gridLayout.addWidget(self.a2_min, 2, 1, 1, 1)
        self.a2_max = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.a2_max.setMinimum(-50.0)
        self.a2_max.setMaximum(50.0)
        self.a2_max.setObjectName("a2_max")
        self.gridLayout.addWidget(self.a2_max, 2, 2, 1, 1)
        self.a3_min = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.a3_min.setMinimum(-50.0)
        self.a3_min.setMaximum(50.0)
        self.a3_min.setObjectName("a3_min")
        self.gridLayout.addWidget(self.a3_min, 3, 1, 1, 1)
        self.a3_max = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.a3_max.setMinimum(-50.0)
        self.a3_max.setMaximum(50.0)
        self.a3_max.setObjectName("a3_max")
        self.gridLayout.addWidget(self.a3_max, 3, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.auto_group)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 130, 191, 25))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.auto_savedir_lay = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.auto_savedir_lay.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.auto_savedir_lay.setContentsMargins(0, 0, 0, 0)
        self.auto_savedir_lay.setObjectName("auto_savedir_lay")
        self.auto_savedir = QtWidgets.QLineEdit(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_savedir.sizePolicy().hasHeightForWidth())
        self.auto_savedir.setSizePolicy(sizePolicy)
        self.auto_savedir.setText("")
        self.auto_savedir.setObjectName("auto_savedir")
        self.auto_savedir_lay.addWidget(self.auto_savedir)
        self.auto_savedir_button = QtWidgets.QToolButton(self.layoutWidget2)
        self.auto_savedir_button.setObjectName("auto_savedir_button")
        self.auto_savedir_lay.addWidget(self.auto_savedir_button)
        self.field_group = QtWidgets.QGroupBox(self.centralwidget)
        self.field_group.setGeometry(QtCore.QRect(310, 180, 181, 161))
        self.field_group.setObjectName("field_group")
        self.gridLayoutWidget = QtWidgets.QWidget(self.field_group)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.x = QtWidgets.QLabel(self.gridLayoutWidget)
        self.x.setObjectName("x")
        self.gridLayout_2.addWidget(self.x, 0, 0, 1, 1)
        self.z = QtWidgets.QLabel(self.gridLayoutWidget)
        self.z.setObjectName("z")
        self.gridLayout_2.addWidget(self.z, 2, 0, 1, 1)
        self.y = QtWidgets.QLabel(self.gridLayoutWidget)
        self.y.setObjectName("y")
        self.gridLayout_2.addWidget(self.y, 1, 0, 1, 1)
        self.mag = QtWidgets.QLabel(self.gridLayoutWidget)
        self.mag.setObjectName("mag")
        self.gridLayout_2.addWidget(self.mag, 3, 0, 1, 1)
        self.x_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.x_val.setEnabled(False)
        self.x_val.setObjectName("x_val")
        self.gridLayout_2.addWidget(self.x_val, 0, 1, 1, 1)
        self.y_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.y_val.setEnabled(False)
        self.y_val.setObjectName("y_val")
        self.gridLayout_2.addWidget(self.y_val, 1, 1, 1, 1)
        self.z_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.z_val.setEnabled(False)
        self.z_val.setObjectName("z_val")
        self.gridLayout_2.addWidget(self.z_val, 2, 1, 1, 1)
        self.mag_val = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.mag_val.setEnabled(False)
        self.mag_val.setClearButtonEnabled(False)
        self.mag_val.setObjectName("mag_val")
        self.gridLayout_2.addWidget(self.mag_val, 3, 1, 1, 1)
        self.settings_group = QtWidgets.QGroupBox(self.centralwidget)
        self.settings_group.setGeometry(QtCore.QRect(500, 180, 201, 161))
        self.settings_group.setObjectName("settings_group")
        self.widget = QtWidgets.QWidget(self.settings_group)
        self.widget.setGeometry(QtCore.QRect(10, 20, 181, 48))
        self.widget.setObjectName("widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.quantity_label = QtWidgets.QLabel(self.widget)
        self.quantity_label.setObjectName("quantity_label")
        self.gridLayout_4.addWidget(self.quantity_label, 1, 1, 1, 1)
        self.quantity_combo = QtWidgets.QComboBox(self.widget)
        self.quantity_combo.setObjectName("quantity_combo")
        self.quantity_combo.addItem("")
        self.quantity_combo.addItem("")
        self.gridLayout_4.addWidget(self.quantity_combo, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.a1_group.setTitle(_translate("MainWindow", "Axis 1"))
        self.a1_pos_label.setText(_translate("MainWindow", "Position"))
        self.a1_step_label.setText(_translate("MainWindow", "Step size"))
        self.a1_right.setText(_translate("MainWindow", "->"))
        self.a1_zero.setText(_translate("MainWindow", "Zero"))
        self.a1_left.setText(_translate("MainWindow", "<-"))
        self.a1_step.setSuffix(_translate("MainWindow", " mm"))
        self.a3_group.setTitle(_translate("MainWindow", "Axis 3"))
        self.a3_zero.setText(_translate("MainWindow", "Zero"))
        self.a3_left.setText(_translate("MainWindow", "<-"))
        self.a3_right.setText(_translate("MainWindow", "->"))
        self.a3_pos_label.setText(_translate("MainWindow", "Position"))
        self.a3_step_label.setText(_translate("MainWindow", "Step size"))
        self.a3_step.setSuffix(_translate("MainWindow", " mm"))
        self.a2_group.setTitle(_translate("MainWindow", "Axis 2"))
        self.a2_pos_label.setText(_translate("MainWindow", "Position"))
        self.a2_step_label.setText(_translate("MainWindow", "Step size"))
        self.a2_right.setText(_translate("MainWindow", "->"))
        self.a2_zero.setText(_translate("MainWindow", "Zero"))
        self.a2_left.setText(_translate("MainWindow", "<-"))
        self.a2_step.setSuffix(_translate("MainWindow", " mm"))
        self.auto_group.setTitle(_translate("MainWindow", "Autoscan Gradient"))
        self.auto_scan.setText(_translate("MainWindow", "Scan"))
        self.auto_to.setText(_translate("MainWindow", "To"))
        self.auto_from.setText(_translate("MainWindow", "From"))
        self.a1_label.setText(_translate("MainWindow", "A1"))
        self.a2_label.setText(_translate("MainWindow", "A2"))
        self.a3_label.setText(_translate("MainWindow", "A3"))
        self.auto_savedir.setPlaceholderText(_translate("MainWindow", "Save directory..."))
        self.auto_savedir_button.setText(_translate("MainWindow", "..."))
        self.field_group.setTitle(_translate("MainWindow", "Field"))
        self.x.setText(_translate("MainWindow", "X"))
        self.z.setText(_translate("MainWindow", "Z"))
        self.y.setText(_translate("MainWindow", "Y"))
        self.mag.setText(_translate("MainWindow", "|B|"))
        self.settings_group.setTitle(_translate("MainWindow", "Settings"))
        self.quantity_label.setText(_translate("MainWindow", "Quantity"))
        self.quantity_combo.setItemText(0, _translate("MainWindow", "Gradient"))
        self.quantity_combo.setItemText(1, _translate("MainWindow", "Field"))

