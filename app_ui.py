# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 607)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setMaximumSize(QtCore.QSize(130, 16777215))
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.sidebar_label = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sidebar_label.setFont(font)
        self.sidebar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sidebar_label.setObjectName("sidebar_label")
        self.verticalLayout_4.addWidget(self.sidebar_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/icons8-home-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout.addWidget(self.home_btn_2)
        self.motor_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/icons8-stepper-motor-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.motor_btn_2.setIcon(icon1)
        self.motor_btn_2.setCheckable(True)
        self.motor_btn_2.setAutoExclusive(True)
        self.motor_btn_2.setObjectName("motor_btn_2")
        self.verticalLayout.addWidget(self.motor_btn_2)
        self.sensor_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/icons8-proximity-sensor-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sensor_btn_2.setIcon(icon2)
        self.sensor_btn_2.setCheckable(True)
        self.sensor_btn_2.setAutoExclusive(True)
        self.sensor_btn_2.setObjectName("sensor_btn_2")
        self.verticalLayout.addWidget(self.sensor_btn_2)
        self.logs_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/icons8-log-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logs_btn_2.setIcon(icon3)
        self.logs_btn_2.setCheckable(True)
        self.logs_btn_2.setAutoExclusive(True)
        self.logs_btn_2.setObjectName("logs_btn_2")
        self.verticalLayout.addWidget(self.logs_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 432, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/icons/icons8-close-window-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_2.setIcon(icon4)
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setMaximumSize(QtCore.QSize(55, 16777215))
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout_2.addWidget(self.home_btn_1)
        self.motor_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.motor_btn_1.setText("")
        self.motor_btn_1.setIcon(icon1)
        self.motor_btn_1.setCheckable(True)
        self.motor_btn_1.setAutoExclusive(True)
        self.motor_btn_1.setObjectName("motor_btn_1")
        self.verticalLayout_2.addWidget(self.motor_btn_1)
        self.sensor_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.sensor_btn_1.setText("")
        self.sensor_btn_1.setIcon(icon2)
        self.sensor_btn_1.setCheckable(True)
        self.sensor_btn_1.setAutoExclusive(True)
        self.sensor_btn_1.setObjectName("sensor_btn_1")
        self.verticalLayout_2.addWidget(self.sensor_btn_1)
        self.logs_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.logs_btn_1.setText("")
        self.logs_btn_1.setIcon(icon3)
        self.logs_btn_1.setCheckable(True)
        self.logs_btn_1.setAutoExclusive(True)
        self.logs_btn_1.setObjectName("logs_btn_1")
        self.verticalLayout_2.addWidget(self.logs_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 461, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        self.exit_btn_1.setIcon(icon4)
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.header_widget = QtWidgets.QWidget(self.widget_3)
        self.header_widget.setGeometry(QtCore.QRect(10, 10, 901, 31))
        self.header_widget.setObjectName("header_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_btn = QtWidgets.QPushButton(self.header_widget)
        self.change_btn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/icons/icons8-menu-32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon5)
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(410, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.header_widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(410, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setGeometry(QtCore.QRect(-20, 50, 931, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setKerning(True)
        self.page.setFont(font)
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(290, 10, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.layoutWidget = QtWidgets.QWidget(self.page_2)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 280, 911, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.widget_5 = QtWidgets.QWidget(self.page_2)
        self.widget_5.setGeometry(QtCore.QRect(20, 330, 911, 211))
        self.widget_5.setObjectName("widget_5")
        self.line_2 = QtWidgets.QFrame(self.widget_5)
        self.line_2.setGeometry(QtCore.QRect(440, 0, 20, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_2.setFont(font)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setGeometry(QtCore.QRect(0, 0, 441, 41))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.label_9 = QtWidgets.QLabel(self.widget_6)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        spacerItem7 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setGeometry(QtCore.QRect(460, 0, 441, 41))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.label_10 = QtWidgets.QLabel(self.widget_7)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem9 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.widget_11 = QtWidgets.QWidget(self.widget_5)
        self.widget_11.setGeometry(QtCore.QRect(0, 46, 441, 161))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem10 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem10)
        self.widget_13 = QtWidgets.QWidget(self.widget_11)
        self.widget_13.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_13)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_31 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_11.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_11.addWidget(self.label_32)
        self.label_33 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_11.addWidget(self.label_33)
        self.label_34 = QtWidgets.QLabel(self.widget_13)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_11.addWidget(self.label_34)
        self.horizontalLayout_12.addWidget(self.widget_13)
        spacerItem11 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.widget_15 = QtWidgets.QWidget(self.widget_5)
        self.widget_15.setGeometry(QtCore.QRect(470, 40, 441, 161))
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem12 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.widget_17 = QtWidgets.QWidget(self.widget_15)
        self.widget_17.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_17)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_35 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_12.addWidget(self.label_35)
        self.label_36 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_12.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.verticalLayout_12.addWidget(self.label_37)
        self.label_38 = QtWidgets.QLabel(self.widget_17)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.verticalLayout_12.addWidget(self.label_38)
        self.horizontalLayout_13.addWidget(self.widget_17)
        spacerItem13 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem13)
        self.layoutWidget1 = QtWidgets.QWidget(self.page_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 20, 911, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        self.widget_8 = QtWidgets.QWidget(self.page_2)
        self.widget_8.setGeometry(QtCore.QRect(20, 70, 911, 211))
        self.widget_8.setObjectName("widget_8")
        self.line_3 = QtWidgets.QFrame(self.widget_8)
        self.line_3.setGeometry(QtCore.QRect(440, 0, 20, 201))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.line_3.setFont(font)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setGeometry(QtCore.QRect(0, 0, 441, 41))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem16 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.label_11 = QtWidgets.QLabel(self.widget_9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        spacerItem17 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem17)
        self.widget_10 = QtWidgets.QWidget(self.widget_8)
        self.widget_10.setGeometry(QtCore.QRect(460, 0, 441, 41))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem18 = QtWidgets.QSpacerItem(178, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem18)
        self.label_12 = QtWidgets.QLabel(self.widget_10)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        spacerItem19 = QtWidgets.QSpacerItem(177, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.widget_12 = QtWidgets.QWidget(self.widget_8)
        self.widget_12.setGeometry(QtCore.QRect(0, 46, 441, 161))
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem20 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem20)
        self.widget_14 = QtWidgets.QWidget(self.widget_12)
        self.widget_14.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.widget_14)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_39 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.verticalLayout_13.addWidget(self.label_39)
        self.label_40 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.verticalLayout_13.addWidget(self.label_40)
        self.label_41 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.verticalLayout_13.addWidget(self.label_41)
        self.label_42 = QtWidgets.QLabel(self.widget_14)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.verticalLayout_13.addWidget(self.label_42)
        self.horizontalLayout_14.addWidget(self.widget_14)
        spacerItem21 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem21)
        self.widget_16 = QtWidgets.QWidget(self.widget_8)
        self.widget_16.setGeometry(QtCore.QRect(470, 40, 441, 161))
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem22 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem22)
        self.widget_18 = QtWidgets.QWidget(self.widget_16)
        self.widget_18.setMinimumSize(QtCore.QSize(200, 0))
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.widget_18)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_43 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.verticalLayout_14.addWidget(self.label_43)
        self.label_44 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.verticalLayout_14.addWidget(self.label_44)
        self.label_45 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.verticalLayout_14.addWidget(self.label_45)
        self.label_46 = QtWidgets.QLabel(self.widget_18)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.verticalLayout_14.addWidget(self.label_46)
        self.horizontalLayout_15.addWidget(self.widget_18)
        spacerItem23 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem23)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.layoutWidget_2 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 20, 911, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem24)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem25)
        self.layoutWidget_3 = QtWidgets.QWidget(self.page_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 280, 911, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem26)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem27)
        self.widget_19 = QtWidgets.QWidget(self.page_3)
        self.widget_19.setGeometry(QtCore.QRect(40, 50, 901, 231))
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem28 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem28)
        self.widget_20 = QtWidgets.QWidget(self.widget_19)
        self.widget_20.setEnabled(True)
        self.widget_20.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_20.setObjectName("widget_20")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.widget_20)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_47 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_15.addWidget(self.label_47)
        self.label_48 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_15.addWidget(self.label_48)
        self.label_49 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.verticalLayout_15.addWidget(self.label_49)
        self.label_50 = QtWidgets.QLabel(self.widget_20)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.verticalLayout_15.addWidget(self.label_50)
        self.horizontalLayout_16.addWidget(self.widget_20)
        spacerItem29 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem29)
        self.widget_21 = QtWidgets.QWidget(self.page_3)
        self.widget_21.setGeometry(QtCore.QRect(40, 310, 901, 231))
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem30 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem30)
        self.widget_23 = QtWidgets.QWidget(self.widget_21)
        self.widget_23.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_23.setObjectName("widget_23")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.widget_23)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_55 = QtWidgets.QLabel(self.widget_23)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.verticalLayout_17.addWidget(self.label_55)
        self.label_56 = QtWidgets.QLabel(self.widget_23)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.verticalLayout_17.addWidget(self.label_56)
        self.label_57 = QtWidgets.QLabel(self.widget_23)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.verticalLayout_17.addWidget(self.label_57)
        self.label_58 = QtWidgets.QLabel(self.widget_23)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.verticalLayout_17.addWidget(self.label_58)
        self.horizontalLayout_18.addWidget(self.widget_23)
        spacerItem31 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem31)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(440, 30, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.motor_btn_1.toggled['bool'].connect(self.motor_btn_2.setChecked) # type: ignore
        self.motor_btn_2.toggled['bool'].connect(self.motor_btn_1.setChecked) # type: ignore
        self.sensor_btn_1.toggled['bool'].connect(self.sensor_btn_2.setChecked) # type: ignore
        self.sensor_btn_2.toggled['bool'].connect(self.sensor_btn_1.setChecked) # type: ignore
        self.logs_btn_1.toggled['bool'].connect(self.logs_btn_2.setChecked) # type: ignore
        self.logs_btn_2.toggled['bool'].connect(self.logs_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sidebar_label.setText(_translate("MainWindow", "Sidebar"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.motor_btn_2.setText(_translate("MainWindow", "Motor Status"))
        self.sensor_btn_2.setText(_translate("MainWindow", "Sensors Status"))
        self.logs_btn_2.setText(_translate("MainWindow", "Logs"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "Some Text"))
        self.label.setText(_translate("MainWindow", "Map of the Venus Surface"))
        self.label_3.setText(_translate("MainWindow", "Robot 2"))
        self.label_9.setText(_translate("MainWindow", "Left Motor"))
        self.label_10.setText(_translate("MainWindow", "Right Motor"))
        self.label_31.setText(_translate("MainWindow", "• Status: Running"))
        self.label_32.setText(_translate("MainWindow", "• Direction: Forward"))
        self.label_33.setText(_translate("MainWindow", "• Power: --Watts"))
        self.label_34.setText(_translate("MainWindow", "• Speed: 1 m/s"))
        self.label_35.setText(_translate("MainWindow", "• Status: Running"))
        self.label_36.setText(_translate("MainWindow", "• Direction: Forward"))
        self.label_37.setText(_translate("MainWindow", "• Power: --Watts"))
        self.label_38.setText(_translate("MainWindow", "• Speed: 1 m/s"))
        self.label_2.setText(_translate("MainWindow", "Robot 1"))
        self.label_11.setText(_translate("MainWindow", "Left Motor"))
        self.label_12.setText(_translate("MainWindow", "Right Motor"))
        self.label_39.setText(_translate("MainWindow", "• Status: Running"))
        self.label_40.setText(_translate("MainWindow", "• Direction: Forward"))
        self.label_41.setText(_translate("MainWindow", "• Power: --Watts"))
        self.label_42.setText(_translate("MainWindow", "• Speed: 1 m/s"))
        self.label_43.setText(_translate("MainWindow", "• Status: Running"))
        self.label_44.setText(_translate("MainWindow", "• Direction: Forward"))
        self.label_45.setText(_translate("MainWindow", "• Power: --Watts"))
        self.label_46.setText(_translate("MainWindow", "• Speed: 1 m/s"))
        self.label_7.setText(_translate("MainWindow", "Robot 1"))
        self.label_5.setText(_translate("MainWindow", "Robot 2"))
        self.label_47.setText(_translate("MainWindow", "• Status: ON"))
        self.label_48.setText(_translate("MainWindow", "• Red: 125"))
        self.label_49.setText(_translate("MainWindow", "• Green: 125"))
        self.label_50.setText(_translate("MainWindow", "• Blue: 125"))
        self.label_55.setText(_translate("MainWindow", "• Status: ON"))
        self.label_56.setText(_translate("MainWindow", "• Red: 125"))
        self.label_57.setText(_translate("MainWindow", "• Green: 125"))
        self.label_58.setText(_translate("MainWindow", "• Blue: 125"))
        self.label_6.setText(_translate("MainWindow", "Logs Page"))
import resource_rc
