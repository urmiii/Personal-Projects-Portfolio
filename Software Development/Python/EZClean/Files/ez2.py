#import libraries
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
from os.path import dirname, realpath, join
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5.uic import loadUiType
import pandas as pd
import numpy as np
import csv
import scipy
from scipy import stats
from scipy.stats import zscore
import re
from PyQt5.QtGui import QIcon



  
       
        

class Ui_Dialog(QWidget):
    def setupUi(self, Dialog):

        
         

        Dialog.setObjectName("Dialog")
        Dialog.resize(1771, 832)
        Dialog.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1801, 841))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_browse = QtWidgets.QPushButton(self.frame)
        self.btn_browse.setGeometry(QtCore.QRect(20, 10, 101, 41))
        self.btn_browse.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_browse.setObjectName("btn_browse")
        self.btn_show = QtWidgets.QPushButton(self.frame)
        self.btn_show.setGeometry(QtCore.QRect(990, 760, 221, 41))
        self.btn_show.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"    border-radius: 2px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_show.setObjectName("btn_show")
        self.tbl_show = QtWidgets.QTableWidget(self.frame)
        self.tbl_show.setGeometry(QtCore.QRect(780, 70, 611, 691))
        self.tbl_show.setStyleSheet("QTableWidget{\n"
"    color: black;\n"
"    selection-background-color: rgb(254, 254, 254);\n"
"    background-color: rgb(238, 238, 238);\n"
"    border-radius: 8px;\n"
"}")
        self.tbl_show.setAlternatingRowColors(False)
        self.tbl_show.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_show.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_show.setObjectName("tbl_show")
        self.tbl_show.setColumnCount(0)
        self.tbl_show.setRowCount(0)
        self.tbl_show.horizontalHeader().setVisible(True)
        self.tbl_show.horizontalHeader().setHighlightSections(False)
        self.tbl_show.verticalHeader().setVisible(False)
        self.tbl_show.verticalHeader().setHighlightSections(True)
        self.tbl_describe = QtWidgets.QTableWidget(self.frame)
        self.tbl_describe.setGeometry(QtCore.QRect(1420, 70, 341, 691))
        self.tbl_describe.setStyleSheet("QTableWidget{\n"
"    color: black;\n"
"    selection-background-color: rgb(254, 254, 254);\n"
"    background-color: rgb(238, 238, 238);\n"
"    border-radius:8px;\n"
"}")
        self.tbl_describe.setAlternatingRowColors(False)
        self.tbl_describe.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_describe.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_describe.setObjectName("tbl_describe")
        self.tbl_describe.setColumnCount(0)
        self.tbl_describe.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_describe.setVerticalHeaderItem(7, item)
        self.tbl_describe.horizontalHeader().setVisible(True)
        self.tbl_describe.horizontalHeader().setHighlightSections(False)
        self.tbl_describe.verticalHeader().setVisible(False)
        self.tbl_describe.verticalHeader().setHighlightSections(True)
        self.btn_describe = QtWidgets.QPushButton(self.frame)
        self.btn_describe.setGeometry(QtCore.QRect(1520, 760, 171, 41))
        self.btn_describe.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"    border-radius: 2px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_describe.setObjectName("btn_describe")
        self.label_null = QtWidgets.QLabel(self.frame)
        self.label_null.setGeometry(QtCore.QRect(20, 100, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_null.setFont(font)
        self.label_null.setStyleSheet("color: white;")
        self.label_null.setObjectName("label_null")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(20, 140, 118, 3))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.spinBox_dropnull = QtWidgets.QSpinBox(self.frame)
        self.spinBox_dropnull.setGeometry(QtCore.QRect(20, 160, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_dropnull.setFont(font)
        self.spinBox_dropnull.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"    border: none;\n"
"}")
        self.spinBox_dropnull.setObjectName("spinBox_dropnull")
        self.btn_dropnull = QtWidgets.QPushButton(self.frame)
        self.btn_dropnull.setGeometry(QtCore.QRect(240, 160, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_dropnull.setFont(font)
        self.btn_dropnull.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_dropnull.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border:  none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"    cursor: pointer;\n"
"}")
        self.btn_dropnull.setObjectName("btn_dropnull")
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(10, 190, 351, 16))
        self.line_2.setStyleSheet("color: white;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.spinBox_replacenull = QtWidgets.QSpinBox(self.frame)
        self.spinBox_replacenull.setGeometry(QtCore.QRect(20, 220, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_replacenull.setFont(font)
        self.spinBox_replacenull.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: none;\n"
"    \n"
"    \n"
"}")
        self.spinBox_replacenull.setObjectName("spinBox_replacenull")
        self.btn_replacenull = QtWidgets.QPushButton(self.frame)
        self.btn_replacenull.setGeometry(QtCore.QRect(230, 210, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_replacenull.setFont(font)
        self.btn_replacenull.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_replacenull.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_replacenull.setObjectName("btn_replacenull")
        self.comboBox_replacenull = QtWidgets.QComboBox(self.frame)
        self.comboBox_replacenull.setGeometry(QtCore.QRect(120, 210, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.comboBox_replacenull.setFont(font)
        self.comboBox_replacenull.setStyleSheet("     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"\n"
"    border-radius: 2px;")
        self.comboBox_replacenull.setObjectName("comboBox_replacenull")
        self.comboBox_replacenull.addItem("")
        self.comboBox_replacenull.addItem("")
        self.comboBox_replacenull.addItem("")
        self.label_drop = QtWidgets.QLabel(self.frame)
        self.label_drop.setGeometry(QtCore.QRect(20, 490, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_drop.setFont(font)
        self.label_drop.setStyleSheet("color: white;")
        self.label_drop.setObjectName("label_drop")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(10, 580, 351, 20))
        self.line_4.setStyleSheet("color: white;")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.spinBox_dropdup = QtWidgets.QSpinBox(self.frame)
        self.spinBox_dropdup.setGeometry(QtCore.QRect(20, 610, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_dropdup.setFont(font)
        self.spinBox_dropdup.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"border: none;\n"
"    \n"
"}")
        self.spinBox_dropdup.setObjectName("spinBox_dropdup")
        self.btn_dropdup = QtWidgets.QPushButton(self.frame)
        self.btn_dropdup.setGeometry(QtCore.QRect(240, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_dropdup.setFont(font)
        self.btn_dropdup.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_dropdup.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_dropdup.setObjectName("btn_dropdup")
        self.spinBox_dropcol = QtWidgets.QSpinBox(self.frame)
        self.spinBox_dropcol.setGeometry(QtCore.QRect(20, 560, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_dropcol.setFont(font)
        self.spinBox_dropcol.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: none;\n"
"}")
        self.spinBox_dropcol.setObjectName("spinBox_dropcol")
        self.btn_dropcol = QtWidgets.QPushButton(self.frame)
        self.btn_dropcol.setGeometry(QtCore.QRect(250, 550, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_dropcol.setFont(font)
        self.btn_dropcol.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_dropcol.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_dropcol.setObjectName("btn_dropcol")
        self.btn_export = QtWidgets.QPushButton(self.frame)
        self.btn_export.setGeometry(QtCore.QRect(1640, 10, 111, 41))
        self.btn_export.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_export.setObjectName("btn_export")
        self.spinBox_add = QtWidgets.QSpinBox(self.frame)
        self.spinBox_add.setGeometry(QtCore.QRect(20, 770, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_add.setFont(font)
        self.spinBox_add.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: none;\n"
"}")
        self.spinBox_add.setObjectName("spinBox_add")
        self.btn_add = QtWidgets.QPushButton(self.frame)
        self.btn_add.setGeometry(QtCore.QRect(210, 760, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_add.setFont(font)
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_add.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.spinBox_gender = QtWidgets.QSpinBox(self.frame)
        self.spinBox_gender.setGeometry(QtCore.QRect(20, 720, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_gender.setFont(font)
        self.spinBox_gender.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"    border: none;\n"
"}")
        self.spinBox_gender.setObjectName("spinBox_gender")
        self.label_inco = QtWidgets.QLabel(self.frame)
        self.label_inco.setGeometry(QtCore.QRect(20, 650, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_inco.setFont(font)
        self.label_inco.setStyleSheet("color: white;")
        self.label_inco.setObjectName("label_inco")
        self.btn_gender = QtWidgets.QPushButton(self.frame)
        self.btn_gender.setGeometry(QtCore.QRect(210, 710, 131, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_gender.setFont(font)
        self.btn_gender.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_gender.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_gender.setObjectName("btn_gender")
        self.spinBox_no = QtWidgets.QSpinBox(self.frame)
        self.spinBox_no.setGeometry(QtCore.QRect(30, 330, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_no.setFont(font)
        self.spinBox_no.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"    \n"
"}")
        self.spinBox_no.setObjectName("spinBox_no")
        self.btn_no = QtWidgets.QPushButton(self.frame)
        self.btn_no.setGeometry(QtCore.QRect(240, 330, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_no.setFont(font)
        self.btn_no.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_no.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_no.setObjectName("btn_no")
        self.spinBox_case = QtWidgets.QSpinBox(self.frame)
        self.spinBox_case.setGeometry(QtCore.QRect(30, 380, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_case.setFont(font)
        self.spinBox_case.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: none;\n"
"}")
        self.spinBox_case.setObjectName("spinBox_case")
        self.label_reformat = QtWidgets.QLabel(self.frame)
        self.label_reformat.setGeometry(QtCore.QRect(20, 270, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_reformat.setFont(font)
        self.label_reformat.setStyleSheet("color: white;")
        self.label_reformat.setObjectName("label_reformat")
        self.btn_case = QtWidgets.QPushButton(self.frame)
        self.btn_case.setGeometry(QtCore.QRect(240, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_case.setFont(font)
        self.btn_case.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_case.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_case.setObjectName("btn_case")
        self.comboBox_case = QtWidgets.QComboBox(self.frame)
        self.comboBox_case.setGeometry(QtCore.QRect(110, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.comboBox_case.setFont(font)
        self.comboBox_case.setStyleSheet("     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"\n"
"    border-radius: 2px;")
        self.comboBox_case.setObjectName("comboBox_case")
        self.comboBox_case.addItem("")
        self.comboBox_case.addItem("")
        self.spinBox_dt = QtWidgets.QSpinBox(self.frame)
        self.spinBox_dt.setGeometry(QtCore.QRect(30, 440, 42, 22))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.spinBox_dt.setFont(font)
        self.spinBox_dt.setStyleSheet("QSpinBox{\n"
"     color: white; \n"
"      border: none;\n"
"    \n"
"}")
        self.spinBox_dt.setObjectName("spinBox_dt")
        self.btn_dt = QtWidgets.QPushButton(self.frame)
        self.btn_dt.setGeometry(QtCore.QRect(240, 440, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        self.btn_dt.setFont(font)
        self.btn_dt.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_dt.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: none;\n"
"    border-radius: 4px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_dt.setObjectName("btn_dt")
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(20, 530, 118, 3))
        self.line_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_11 = QtWidgets.QFrame(self.frame)
        self.line_11.setGeometry(QtCore.QRect(20, 310, 118, 3))
        self.line_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(20, 360, 351, 16))
        self.line_12.setStyleSheet("color: white;")
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(20, 420, 351, 16))
        self.line_13.setStyleSheet("color: white;")
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.frame)
        self.line_14.setGeometry(QtCore.QRect(20, 690, 118, 3))
        self.line_14.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_16 = QtWidgets.QFrame(self.frame)
        self.line_16.setGeometry(QtCore.QRect(10, 740, 351, 16))
        self.line_16.setStyleSheet("color: white;")
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.tbl_dfaux = QtWidgets.QTableWidget(self.frame)
        self.tbl_dfaux.setGeometry(QtCore.QRect(410, 70, 341, 691))
        self.tbl_dfaux.setStyleSheet("QTableWidget{\n"
"    color: black;\n"
"    selection-background-color: rgb(254, 254, 254);\n"
"    background-color: rgb(238, 238, 238);\n"
"    border-radius:8px;\n"
"}")
        self.tbl_dfaux.setAlternatingRowColors(False)
        self.tbl_dfaux.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tbl_dfaux.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tbl_dfaux.setObjectName("tbl_dfaux")
        self.tbl_dfaux.setColumnCount(0)
        self.tbl_dfaux.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_dfaux.setVerticalHeaderItem(7, item)
        self.tbl_dfaux.horizontalHeader().setVisible(True)
        self.tbl_dfaux.horizontalHeader().setHighlightSections(False)
        self.tbl_dfaux.verticalHeader().setVisible(False)
        self.tbl_dfaux.verticalHeader().setHighlightSections(True)
        self.btn_dfaux = QtWidgets.QPushButton(self.frame)
        self.btn_dfaux.setGeometry(QtCore.QRect(470, 760, 221, 41))
        self.btn_dfaux.setStyleSheet("QPushButton{\n"
"     color: white; \n"
"      border: 2px solid  rgb(202, 202, 202);\n"
"    border-radius: 2px;\n"
"  \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(202, 202, 202);\n"
"      color: black;\n"
"}")
        self.btn_dfaux.setObjectName("btn_dfaux")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "EZClean"))
        self.btn_browse.setText(_translate("Dialog", "Browse File"))
        self.btn_show.setText(_translate("Dialog", "Load Data"))
        item = self.tbl_describe.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "count"))
        item = self.tbl_describe.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tbl_describe.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "mean"))
        item = self.tbl_describe.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "min"))
        item = self.tbl_describe.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tbl_describe.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "25%"))
        item = self.tbl_describe.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "50%"))
        item = self.tbl_describe.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "max"))
        self.btn_describe.setText(_translate("Dialog", " Apply ZScore "))
        self.label_null.setText(_translate("Dialog", "Handling Null Values"))
        self.btn_dropnull.setText(_translate("Dialog", "Drop Null Values"))
        self.btn_replacenull.setText(_translate("Dialog", "Replace Null Values"))
        self.comboBox_replacenull.setItemText(0, _translate("Dialog", "Mean"))
        self.comboBox_replacenull.setItemText(1, _translate("Dialog", "Median"))
        self.comboBox_replacenull.setItemText(2, _translate("Dialog", "Mode"))
        self.label_drop.setText(_translate("Dialog", "Dropping Features"))
        self.btn_dropdup.setText(_translate("Dialog", "Drop Rows"))
        self.btn_dropcol.setText(_translate("Dialog", "Drop Column"))
        self.btn_export.setText(_translate("Dialog", "Export CSV"))
        self.btn_add.setText(_translate("Dialog", "Address Inconsistency"))
        self.label_inco.setText(_translate("Dialog", "Remove Inconsistency"))
        self.btn_gender.setText(_translate("Dialog", "Gender Inconsistency"))
        self.btn_no.setText(_translate("Dialog", "Reformat Number"))
        self.label_reformat.setText(_translate("Dialog", "Reformat Values"))
        self.btn_case.setText(_translate("Dialog", "Reformat Cases"))
        self.comboBox_case.setItemText(0, _translate("Dialog", "Uppercase"))
        self.comboBox_case.setItemText(1, _translate("Dialog", "Lowercase"))
        self.btn_dt.setText(_translate("Dialog", "Reformat Date"))
        item = self.tbl_dfaux.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "count"))
        item = self.tbl_dfaux.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tbl_dfaux.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "mean"))
        item = self.tbl_dfaux.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "min"))
        item = self.tbl_dfaux.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "New Row"))
        item = self.tbl_dfaux.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "25%"))
        item = self.tbl_dfaux.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "50%"))
        item = self.tbl_dfaux.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "max"))
        self.btn_dfaux.setText(_translate("Dialog", "Analyze Data"))


        self.btn_browse.clicked.connect(self.OpenFile)
        self.btn_show.clicked.connect(self.dataHead)
        self.btn_dfaux.clicked.connect(self.dfaux)
        self.btn_describe.clicked.connect(self.ZScore)
        self.btn_dropnull.clicked.connect(self.Dropnull)
        self.btn_replacenull.clicked.connect(self.Replacenull)
        self.btn_no.clicked.connect(self.FormatNo)
        self.btn_case.clicked.connect(self.UpperLower)
        self.btn_dt.clicked.connect(self.FormatDT)
        self.btn_dropcol.clicked.connect(self.DropCol)
        self.btn_dropdup.clicked.connect(self.DropDup)
        self.btn_gender.clicked.connect(self.FormatMF)
        self.btn_add.clicked.connect(self.FormatAdd)
        self.btn_export.clicked.connect(self.GetCSV)


    def OpenFile(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')[0]
            self.all_data = pd.read_csv(path)
            print('Its in try')
        except:
            self.all_data = pd.read_csv(path)
            print('Its in except')

    def dataHead(self):
        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)
        self.tbl_show.setColumnCount(len(self.all_data.columns))
        self.tbl_show.setRowCount(NumRows)
        self.tbl_show.setHorizontalHeaderLabels(self.all_data.columns)

        print(numColomn, NumRows)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tbl_show.resizeColumnsToContents()
        self.tbl_show.resizeRowsToContents()   


    def dfaux (self):
        cant = self.all_data.isnull().sum()
        df_aux = pd.DataFrame(index = self.all_data.columns, data =
                             {'feature': self.all_data.columns,
                              'type': self.all_data.dtypes,
                              'unique_values': self.all_data.nunique(),
                              'have_null?': self.all_data.isnull().any(),
                              'how many?' : cant,
                              'per' : cant/self.all_data.shape[0]*100 })
        
        numColomn1 = len(df_aux.columns)
        NumRows1 = len(df_aux.index)
        self.tbl_dfaux.setColumnCount(len(df_aux.columns))
        self.tbl_dfaux.setRowCount(NumRows1)
        self.tbl_dfaux.setHorizontalHeaderLabels(df_aux.columns)

        print(numColomn1, NumRows1)

        for i in range(NumRows1):
            for j in range(len(df_aux.columns)):
                self.tbl_dfaux.setItem(i, j, QTableWidgetItem(str(df_aux.iat[i, j])))

        self.tbl_dfaux.resizeColumnsToContents()
        self.tbl_dfaux.resizeRowsToContents()



    def ZScore(self):
        df = self.all_data.select_dtypes(include=np.number)
        upd_df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
        print(upd_df)

        upd_cols = upd_df.columns
        #df['z_score']=df.apply(zscore)
        for col in upd_cols:
            col_zscore = col + '_zscore'
            upd_df[col_zscore] = (upd_df[col] - upd_df[col].mean())/upd_df[col].std(ddof=0)
            #print(df)

        numColomn = len(upd_df.columns)
        NumRows = len(upd_df.index)

        self.tbl_describe.setColumnCount(len(upd_df.columns))
        self.tbl_describe.setRowCount(NumRows)
        self.tbl_describe.setHorizontalHeaderLabels(upd_df.columns)

        print(numColomn, NumRows)

        for i in range(NumRows):
            for j in range(len(upd_df.columns)):
                self.tbl_describe.setItem(i, j, QTableWidgetItem(str(upd_df.iat[i, j])))

        self.tbl_describe.resizeColumnsToContents()
        self.tbl_describe.resizeRowsToContents() 


    def Dropnull(self):        
        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)
        nCol = self.spinBox_dropnull.value()
        if nCol == 0:
            #nRow = len(self.all_data.columns)
            print('error!')
        else:
            displayCol = nCol - 1
            colName = self.all_data.columns[displayCol]
            print(colName)
            self.all_data = self.all_data.dropna(subset=[(colName)])
            #df.to_csv('NewData.csv', index=False)
            print('done')
            #nRow = nCol #the number which will be selected by the user
            numColomn = len(self.all_data.columns)
            NumRows = len(self.all_data.index)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tbl_show.resizeColumnsToContents()
            self.tbl_show.resizeRowsToContents()
      

       
    def Replacenull(self):
        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)
        nColReplace = self.spinBox_replacenull.value()
        x = self.comboBox_replacenull.currentText()
        if x == 'Mode':
            displayColReplace = nColReplace - 1
            colName = self.all_data.columns[displayColReplace]
            print(colName)
            self.all_data[(colName)] =  self.all_data[(colName)].fillna(self.all_data[(colName)].mode()[0])
            #df_mode = self.all_data
            #df_mode.to_csv('NewData_Mode.csv', index=False)
            print('done')
            #nRow = nCol #the number which will be selected by the user
            #nRow = len(self.all_data.columns)
            numColomn = len(self.all_data.columns)
            NumRows = len(self.all_data.index)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tbl_show.resizeColumnsToContents()
            self.tbl_show.resizeRowsToContents()
    
        elif x == 'Mean':
            displayColReplace = nColReplace - 1
            colName = self.all_data.columns[displayColReplace]
            print(colName)
            self.all_data[(colName)] =  self.all_data[(colName)].fillna(self.all_data[(colName)].mean())
            #df_mean = self.all_data
            #df_mean.to_csv('NewData_Mean.csv', index=False)
            print('done')
            #nRow = nCol #the number which will be selected by the user
            numColomn = len(self.all_data.columns)
            NumRows = len(self.all_data.index)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tbl_show.resizeColumnsToContents()
            self.tbl_show.resizeRowsToContents()

        else: 
            displayColReplace = nColReplace - 1
            colName = self.all_data.columns[displayColReplace]
            print(colName)
            self.all_data[(colName)] =  self.all_data[(colName)].fillna(self.all_data[(colName)].median())
            #df_median = self.all_data
            #df_median.to_csv('NewData_Median.csv', index=False)
            print('done')
            #nRow = nCol #the number which will be selected by the user
            numColomn = len(self.all_data.columns)
            NumRows = len(self.all_data.index)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

            self.tbl_show.resizeColumnsToContents()
            self.tbl_show.resizeRowsToContents()   



    def FormatNo(self):
        nColNO = self.spinBox_no.value()
        if nColNO == 0:
            print('error!')
        else:
            displayCol = nColNO - 1
            colName = self.all_data.columns[displayCol]
            print(colName)

            self.all_data[(colName)] = self.all_data[(colName)].astype(str).apply(lambda x: '('+x[:3]+')'+x[3:6]+'-'+x[6:10])
            print(self.all_data)

        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tbl_show.resizeColumnsToContents()
        self.tbl_show.resizeRowsToContents()



    def UpperLower(self):
        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)
        nColUL = self.spinBox_case.value()

        x = self.comboBox_case.currentText()
        if x == "Uppercase":
            displayCol = nColUL - 1
            colName = self.all_data.columns[displayCol]
            print(colName)
            
            self.all_data[(colName)] =  self.all_data[(colName)].str.upper()
            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))


        else:
            displayCol = nColUL - 1
            colName = self.all_data.columns[displayCol]
            print(colName)
            
            self.all_data[(colName)] =  self.all_data[(colName)].str.lower()
            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))




    def FormatDT(self):
        nColDT = self.spinBox_dt.value()
        if nColDT == 0:
            print('error!')
        else:
            displayCol = nColDT - 1
            colName = self.all_data.columns[displayCol]
            print(colName)
            self.all_data[(colName)] = pd.to_datetime(self.all_data[(colName)])
            self.all_data[(colName)] = self.all_data[(colName)].dt.strftime('%m/%d/%Y')
            
            print(self.all_data)

        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tbl_show.resizeColumnsToContents()
        self.tbl_show.resizeRowsToContents()


    def DropCol(self):
        nColDrop = self.spinBox_dropcol.value()
        if nColDrop == 0:
            print('error!')
        else:

            displayCol = nColDrop - 1
            colName = self.all_data.columns[displayCol]
            print(colName)


            self.all_data = self.all_data.drop([(colName)], axis=1)
            print(self.all_data)
            numColomn = len(self.all_data.columns)
            NumRows = len(self.all_data.index)

            self.tbl_show.setColumnCount(len(self.all_data.columns))
            self.tbl_show.setRowCount(NumRows)
            self.tbl_show.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))



    def DropDup(self):
        nRowDup = self.spinBox_dropdup.value()
        if nRowDup == 0:
            print('error!')
        else:

            displayRow = nRowDup - 1
            #rowName = self.all_data.columns[displayRow]
            #print(rowName)


            self.all_data = self.all_data.drop([self.all_data.index[(displayRow)]])
            print(self.all_data)
            numColomn = len(self.all_data.columns)
            NumRows = len(self.all_data.index)

            self.tbl_show.setColumnCount(len(self.all_data.columns))
            self.tbl_show.setRowCount(NumRows)
            self.tbl_show.setHorizontalHeaderLabels(self.all_data.columns)

            for i in range(NumRows):
                for j in range(len(self.all_data.columns)):
                    self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))



    def FormatMF(self):
        nColMF = self.spinBox_gender.value()
        if nColMF == 0:
            print('error!')
        else:
            displayCol = nColMF - 1
            colName = self.all_data.columns[displayCol]
            print(colName)

            self.all_data[(colName)] = self.all_data[(colName)].apply(lambda s: re.sub(
                                    "(^F)([A-Za-z]+)*",  # pattern
                                    "Female",            # replace
                                    s.strip().title())   # string
                                )
            self.all_data[(colName)] = self.all_data[(colName)].apply(lambda s: re.sub(
                                    "(^M)([A-Za-z]+)*",  # pattern
                                    "Male",            # replace
                                    s.strip().title())   # string
                                )
            
            print(self.all_data)

        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tbl_show.resizeColumnsToContents()
        self.tbl_show.resizeRowsToContents()


    def FormatAdd(self):
        nColAdd = self.spinBox_add.value()
        if nColAdd == 0:
            print('error!')
        else:
            displayCol = nColAdd - 1
            colName = self.all_data.columns[displayCol]
            print(colName)
            self.all_data[(colName)] = self.all_data[(colName)].str.lower()
            self.all_data[(colName)] = self.all_data[(colName)].str.strip()
            self.all_data[(colName)] = self.all_data[(colName)].str.replace('\\.', '')
            self.all_data[(colName)] = self.all_data[(colName)].str.replace('\\bstreet\\b', 'st')
            self.all_data[(colName)] = self.all_data[(colName)].str.replace('\\bapartment\\b', 'apt')
            self.all_data[(colName)] = self.all_data[(colName)].str.replace('\\bav\\b', 'ave')

            print(self.all_data)

        numColomn = len(self.all_data.columns)
        NumRows = len(self.all_data.index)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.tbl_show.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.tbl_show.resizeColumnsToContents()
        self.tbl_show.resizeRowsToContents()


    def GetCSV(self):
        df = self.all_data
        df.to_csv('ExportedData.csv', index=False)
        print('done')


    #def initUI(self):
        
        #self.setGeometry(300, 300, 300, 220)
        #self.setWindowTitle('Icon')
        #self.setWindowIcon(QIcon('logo.png'))        
    
        #self.show()
   
        
        
             
    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet('QDialog{background-color: darkgray;border: 1px solid black;}')
    Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)
    app.setWindowIcon(QIcon("./logo.png"));
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
