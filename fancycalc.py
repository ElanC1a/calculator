from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(488, 637)
        MainWindow.setStyleSheet("background-color: rgb(177, 145, 200);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 160, 441, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_comma = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_comma.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_comma.sizePolicy().hasHeightForWidth())
        self.button_comma.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_comma.setFont(font)
        self.button_comma.setIconSize(QtCore.QSize(18, 18))
        self.button_comma.setObjectName("button_comma")
        self.gridLayout.addWidget(self.button_comma, 5, 2, 1, 1)
        self.button_zero = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_zero.sizePolicy().hasHeightForWidth())
        self.button_zero.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_zero.setFont(font)
        self.button_zero.setIconSize(QtCore.QSize(18, 18))
        self.button_zero.setObjectName("button_zero")
        self.gridLayout.addWidget(self.button_zero, 5, 1, 1, 1)
        self.button_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_plus.sizePolicy().hasHeightForWidth())
        self.button_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_plus.setFont(font)
        self.button_plus.setIconSize(QtCore.QSize(18, 18))
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 4, 3, 1, 1)
        self.button_nine = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_nine.sizePolicy().hasHeightForWidth())
        self.button_nine.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_nine.setFont(font)
        self.button_nine.setIconSize(QtCore.QSize(18, 18))
        self.button_nine.setObjectName("button_nine")
        self.gridLayout.addWidget(self.button_nine, 2, 2, 1, 1)
        self.button_seven = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_seven.sizePolicy().hasHeightForWidth())
        self.button_seven.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_seven.setFont(font)
        self.button_seven.setIconSize(QtCore.QSize(18, 18))
        self.button_seven.setObjectName("button_seven")
        self.gridLayout.addWidget(self.button_seven, 2, 0, 1, 1)
        self.button_minus_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus_plus.sizePolicy().hasHeightForWidth())
        self.button_minus_plus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_minus_plus.setFont(font)
        self.button_minus_plus.setIconSize(QtCore.QSize(18, 18))
        self.button_minus_plus.setObjectName("button_minus_plus")
        self.gridLayout.addWidget(self.button_minus_plus, 5, 0, 1, 1)
        self.button_five = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_five.sizePolicy().hasHeightForWidth())
        self.button_five.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_five.setFont(font)
        self.button_five.setIconSize(QtCore.QSize(18, 18))
        self.button_five.setObjectName("button_five")
        self.gridLayout.addWidget(self.button_five, 3, 1, 1, 1)
        self.button_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_delete.setFont(font)
        self.button_delete.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.button_delete.setIconSize(QtCore.QSize(18, 18))
        self.button_delete.setObjectName("button_delete")
        self.gridLayout.addWidget(self.button_delete, 0, 3, 1, 1)
        self.button_erase_c = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_erase_c.sizePolicy().hasHeightForWidth())
        self.button_erase_c.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_erase_c.setFont(font)
        self.button_erase_c.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.button_erase_c.setIconSize(QtCore.QSize(18, 18))
        self.button_erase_c.setObjectName("button_erase_c")
        self.gridLayout.addWidget(self.button_erase_c, 0, 2, 1, 1)
        self.button_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_equal.sizePolicy().hasHeightForWidth())
        self.button_equal.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_equal.setFont(font)
        self.button_equal.setIconSize(QtCore.QSize(18, 18))
        self.button_equal.setObjectName("button_equal")
        self.gridLayout.addWidget(self.button_equal, 5, 3, 1, 1)
        self.button_division = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_division.sizePolicy().hasHeightForWidth())
        self.button_division.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_division.setFont(font)
        self.button_division.setIconSize(QtCore.QSize(18, 18))
        self.button_division.setObjectName("button_division")
        self.gridLayout.addWidget(self.button_division, 1, 3, 1, 1)
        self.button_one = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_one.sizePolicy().hasHeightForWidth())
        self.button_one.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_one.setFont(font)
        self.button_one.setIconSize(QtCore.QSize(18, 18))
        self.button_one.setObjectName("button_one")
        self.gridLayout.addWidget(self.button_one, 4, 0, 1, 1)
        self.button_two = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_two.sizePolicy().hasHeightForWidth())
        self.button_two.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_two.setFont(font)
        self.button_two.setIconSize(QtCore.QSize(18, 18))
        self.button_two.setObjectName("button_two")
        self.gridLayout.addWidget(self.button_two, 4, 1, 1, 1)
        self.button_three = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_three.sizePolicy().hasHeightForWidth())
        self.button_three.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_three.setFont(font)
        self.button_three.setIconSize(QtCore.QSize(18, 18))
        self.button_three.setObjectName("button_three")
        self.gridLayout.addWidget(self.button_three, 4, 2, 1, 1)
        self.button_six = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_six.sizePolicy().hasHeightForWidth())
        self.button_six.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_six.setFont(font)
        self.button_six.setIconSize(QtCore.QSize(18, 18))
        self.button_six.setObjectName("button_six")
        self.gridLayout.addWidget(self.button_six, 3, 2, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_minus.sizePolicy().hasHeightForWidth())
        self.button_minus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_minus.setFont(font)
        self.button_minus.setIconSize(QtCore.QSize(18, 18))
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 3, 3, 1, 1)
        self.button_x_root = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_x_root.sizePolicy().hasHeightForWidth())
        self.button_x_root.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_x_root.setFont(font)
        self.button_x_root.setIconSize(QtCore.QSize(18, 18))
        self.button_x_root.setObjectName("button_x_root")
        self.gridLayout.addWidget(self.button_x_root, 1, 2, 1, 1)
        self.button_multiplication = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_multiplication.sizePolicy().hasHeightForWidth())
        self.button_multiplication.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_multiplication.setFont(font)
        self.button_multiplication.setIconSize(QtCore.QSize(18, 18))
        self.button_multiplication.setObjectName("button_multiplication")
        self.gridLayout.addWidget(self.button_multiplication, 2, 3, 1, 1)
        self.button_percentage = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_percentage.sizePolicy().hasHeightForWidth())
        self.button_percentage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_percentage.setFont(font)
        self.button_percentage.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.button_percentage.setIconSize(QtCore.QSize(18, 18))
        self.button_percentage.setObjectName("button_percentage")
        self.gridLayout.addWidget(self.button_percentage, 0, 0, 1, 1)
        self.button_x_squared = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_x_squared.sizePolicy().hasHeightForWidth())
        self.button_x_squared.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_x_squared.setFont(font)
        self.button_x_squared.setIconSize(QtCore.QSize(18, 18))
        self.button_x_squared.setObjectName("button_x_squared")
        self.gridLayout.addWidget(self.button_x_squared, 1, 1, 1, 1)
        self.button_erase_ce = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_erase_ce.sizePolicy().hasHeightForWidth())
        self.button_erase_ce.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_erase_ce.setFont(font)
        self.button_erase_ce.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));")
        self.button_erase_ce.setIconSize(QtCore.QSize(18, 18))
        self.button_erase_ce.setObjectName("button_erase_ce")
        self.gridLayout.addWidget(self.button_erase_ce, 0, 1, 1, 1)
        self.button_eight = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_eight.sizePolicy().hasHeightForWidth())
        self.button_eight.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_eight.setFont(font)
        self.button_eight.setIconSize(QtCore.QSize(18, 18))
        self.button_eight.setObjectName("button_eight")
        self.gridLayout.addWidget(self.button_eight, 2, 1, 1, 1)
        self.button_four = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_four.sizePolicy().hasHeightForWidth())
        self.button_four.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_four.setFont(font)
        self.button_four.setIconSize(QtCore.QSize(18, 18))
        self.button_four.setObjectName("button_four")
        self.gridLayout.addWidget(self.button_four, 3, 0, 1, 1)
        self.button_smile = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_smile.sizePolicy().hasHeightForWidth())
        self.button_smile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(17)
        self.button_smile.setFont(font)
        self.button_smile.setIconSize(QtCore.QSize(18, 18))
        self.button_smile.setObjectName("button_smile")
        self.gridLayout.addWidget(self.button_smile, 1, 0, 1, 1)
        self.text_frame = QtWidgets.QTextEdit(self.centralwidget)
        self.text_frame.document().setDefaultTextOption(QtGui.QTextOption(QtCore.Qt.AlignRight))
        self.text_frame.setGeometry(QtCore.QRect(10, 20, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(65)
        self.text_frame.setFont(font)
        self.text_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.text_frame.setStyleSheet("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));")
        self.text_frame.setObjectName("text_frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.input_press()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_comma.setText(_translate("MainWindow", "."))
        self.button_zero.setText(_translate("MainWindow", "0"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_nine.setText(_translate("MainWindow", "9"))
        self.button_seven.setText(_translate("MainWindow", "7"))
        self.button_minus_plus.setText(_translate("MainWindow", "+/-"))
        self.button_five.setText(_translate("MainWindow", "5"))
        self.button_delete.setText(_translate("MainWindow", "⇚"))
        self.button_erase_c.setText(_translate("MainWindow", "C"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_division.setText(_translate("MainWindow", "/"))
        self.button_one.setText(_translate("MainWindow", "1"))
        self.button_two.setText(_translate("MainWindow", "2"))
        self.button_three.setText(_translate("MainWindow", "3"))
        self.button_six.setText(_translate("MainWindow", "6"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_x_root.setText(_translate("MainWindow", "√"))
        self.button_multiplication.setText(_translate("MainWindow", "*"))
        self.button_percentage.setText(_translate("MainWindow", "%"))
        self.button_x_squared.setText(_translate("MainWindow", "x²"))
        self.button_erase_ce.setText(_translate("MainWindow", "CE"))
        self.button_eight.setText(_translate("MainWindow", "8"))
        self.button_four.setText(_translate("MainWindow", "4"))
        self.button_smile.setText(_translate("MainWindow", ":)"))

    def input_press(self):
        self.button_minus_plus.clicked.connect(lambda: self.into_text_box(self.button_minus_plus.text()))
        self.button_zero.clicked.connect(lambda: self.into_text_box(self.button_zero.text()))
        self.button_comma.clicked.connect(lambda: self.into_text_box(self.button_comma.text()))
        self.button_equal.clicked.connect(self.result)

        self.button_one.clicked.connect(lambda: self.into_text_box(self.button_one.text()))
        self.button_two.clicked.connect(lambda: self.into_text_box(self.button_two.text()))
        self.button_three.clicked.connect(lambda: self.into_text_box(self.button_three.text()))
        self.button_plus.clicked.connect(lambda: self.into_text_box(self.button_plus.text()))
        self.button_four.clicked.connect(lambda: self.into_text_box(self.button_four.text()))
        self.button_five.clicked.connect(lambda: self.into_text_box(self.button_five.text()))
        self.button_six.clicked.connect(lambda: self.into_text_box(self.button_six.text()))
        self.button_minus.clicked.connect(lambda: self.into_text_box(self.button_minus.text()))
        self.button_seven.clicked.connect(lambda: self.into_text_box(self.button_seven.text()))
        self.button_eight.clicked.connect(lambda: self.into_text_box(self.button_eight.text()))
        self.button_nine.clicked.connect(lambda: self.into_text_box(self.button_nine.text()))
        self.button_multiplication.clicked.connect(lambda: self.into_text_box(self.button_multiplication.text()))
        self.button_smile.clicked.connect(lambda: self.into_text_box(self.button_smile.text()))
        self.button_x_squared.clicked.connect(lambda: self.into_text_box(self.button_x_squared.text()))

        self.button_x_root.clicked.connect(lambda: self.into_text_box(self.button_x_root.text()))

        self.button_division.clicked.connect(lambda: self.into_text_box(self.button_division.text()))
        self.button_percentage.clicked.connect(lambda: self.into_text_box(self.button_percentage.text()))
        self.button_erase_ce.clicked.connect(lambda: self.text_frame.setText(""))
        self.button_erase_c.clicked.connect(lambda: self.text_frame.setText(""))
        self.button_delete.clicked.connect(lambda: self.erase())

    def into_text_box(self, the_variable):
        text = self.text_frame.toPlainText()
        if "x²" == the_variable:
            the_variable = "²"

        self.text_frame.setText(text + the_variable)

    def result(self):
        text = self.text_frame.toPlainText()
        for i in range(len(text)): 
            if text[i] == "²":          #5²+√2
                first_phase = text[:i]
                second_phase = text[i+1:]
                text = first_phase + "**2" + second_phase
        for i in range(len(text)): 
            if text[i] == "√": 
                text_1 = text[:i]
                text_2 = text[i+1:] #root
                chetzik = 0 #index
                
                try:
                    while text_2[chetzik] != "+" and text_2[chetzik] != "-" and text_2[chetzik] != "/" and text_2[chetzik] != "*" and text_2[chetzik] != "%" and text_2[chetzik] != ":)":
                        chetzik += 1
                        if chetzik > (len(text_2)-1):
                            # chetzik -= 1
                            break
                except:
                    self.text_frame.setText("ERROR")
                new_text_1 = text_2[:chetzik]
                new_text_1 += "**0.5"
                new_text_2 = text_2[chetzik:] 
                print(new_text_2)
                text = text_1 + new_text_1 + new_text_2
        # i forgot what I was writing here, figure out urself, gl
        # basically i didn't finish it, would be nice if you could)
        # for i in range(len(text)-1):
        #     print(i)
        #     if text[i] == "%":          # 5-25%6 i = 4
        #         text_1 = text[:i]
        #         chetzik_1 = 1
        #         while text_1[-chetzik_1] != "+" and text_1[-chetzik_1] != "-" and text_1[-chetzik_1] != "/" and text_1[-chetzik_1] != "*" and text_1[-chetzik_1] != "%" and text_1[-chetzik_1] != ":)":
        #             chetzik_1 += 1
        #             if chetzik_1 >= (len(text_1)):
        #                 chetzik_1 -= 1
        #                 break
        #         new_text_1 = text_1[-chetzik_1:]
        #         print(new_text_1)

        #         text_2 = text[i+1:] #to the right side  text_2 = 6 ego i = 5
        #         chetzik_2 = 0
        #         while text_2[chetzik_2] != "+" and text_2[chetzik_2] != "-" and text_2[chetzik_2] != "/" and text_2[chetzik_2] != "*" and text_2[chetzik_2] != "%" and text_2[chetzik_2] != ":)":
        #             chetzik_2 += 1 
        #             if chetzik_2 > (len(text_2)-1):
        #                 # chetzik -= 1
        #                 break
        #         new_text_2 = text_2[:chetzik_2]
        #         print(new_text_2)
                
        #         banana = True
        #         new_text_1 = int(new_text_1)        #5-25%6-2
        #         new_text_2 = int(new_text_2)
        #         while banana:
        #             new_text_1 = new_text_1 - new_text_2        # 25 % 6 ->25-6= 19  i =
        #             g = new_text_1
        #             if g < new_text_2:
        #                 percentage_answer = g  
        #                 print(percentage_answer)
        #                 banana = False             
        #         text = text_1[:-chetzik_1] + str(percentage_answer) + text_2[chetzik_2:]
        try:
            the_answer = eval(text)
            self.text_frame.setText(str(the_answer))
        except:
            print("ERROR")
            self.text_frame.setText("ERROR")
            

    # def plus_minus(self):
    #     text = self.text_frame.toPlainText()
    #     not done, not lazy obviously...


    def erase(self):
        text = self.text_frame.toPlainText()
        self.text_frame.setText(text[:-1])

    def square(self):
        text = self.text_frame.toPlainText()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
