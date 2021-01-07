#from typing import Any

import os
import cv2
import sys
import shutil
import glob
import math
import warnings
import numpy as np
from PIL import Image
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import cpu_count
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QWidget, QLabel
from PySide2.QtGui import QIcon, QPixmap
from time import sleep
from PIL import Image, ImageTk
from tkinter import Canvas, Tk, Label, LEFT, Frame, filedialog, messagebox


#----------------------------------------------------KMEANS--------------------------------------------------------------------------------------
#------------------------------------------------------ALGORITHM------------------------------------------------------------------------------------------
class K_means:

    def __init__(self, k=2, size=False, resample=128):
        self.k = k
        self.cluster = []
        self.data = []
        self.end = []
        self.i = 0
        self.size = size
        self.resample = resample

    def manhattan_distance(self, x1, x2):
        s = 0.0
        for i in range(len(x1)):
            s += abs(float(x1[i]) - float(x2[i]))
        return s

    def euclidian_distance(self, x1, x2):
        s = 0.0
        for i in range(len(x1)):
            s += math.sqrt((float(x1[i]) - float(x2[i])) ** 2)
        return s

    def read_image(self, im):
        if self.i >= self.k:
            self.i = 0
        try:
            img = Image.open(im)
            osize = img.size
            img.thumbnail((self.resample, self.resample))
            v = [float(p) / float(img.size[0] * img.size[1]) * 100 for p in np.histogram(np.asarray(img))[0]]
            if self.size:
                v += [osize[0], osize[1]]
            i = self.i
            self.i += 1
            return [i, v, im]
        except Exception as e:
            print("Error reading ", im, e)
            return [None, None, None]

    def generate_k_means(self):
        final_mean = []
        for c in range(self.k):
            partial_mean = []
            for i in range(len(self.data[0])):
                s = 0.0
                t = 0
                for j in range(len(self.data)):
                    if self.cluster[j] == c:
                        s += self.data[j][i]
                        t += 1
                if t != 0:
                    partial_mean.append(float(s) / float(t))
                else:
                    partial_mean.append(float('inf'))
            final_mean.append(partial_mean)
        return final_mean

    def generate_k_clusters(self, folder):
        pool = ThreadPool(cpu_count())
        result = pool.map(self.read_image, folder)
        pool.close()
        pool.join()
        self.cluster = [r[0] for r in result if r[0] != None]
        self.data = [r[1] for r in result if r[1] != None]
        self.end = [r[2] for r in result if r[2] != None]

    def rearrange_clusters(self):
        isover = False
        while (not isover):
            isover = True
            m = self.generate_k_means()
            for x in range(len(self.cluster)):
                dist = []
                for a in range(self.k):
                    dist.append(self.manhattan_distance(self.data[x], m[a]))
                _mindist = dist.index(min(dist))
                if self.cluster[x] != _mindist:
                    self.cluster[x] = _mindist
                    isover = False


class groupImgGUI(QWidget):
    # ----------------------------------------------------MAIN--------------------------------------------------------------------------------------
    # ------------------------------------------------------WINDOW------------------------------------------------------------------------------------------
    def __init__(self, parent=None):
        super(groupImgGUI, self).__init__(parent)
        self.dir = None
        self.img_processed = False
        self.width = 400
        self.height = 300
        self.createSettings()  # image grouping box
        self.editSettings()  # edit image box
        self.nextFeatures()  # total features list box
        self.manual()
        self.facerecog()
        layout = QVBoxLayout()

        self.b1 = QPushButton("Start")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.state3)  # redirects to the tool function

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('image4.png'))  # bg image
        self.label.setGeometry(0, 0, 400, 300)  # left, top, width, height

        layout.addWidget(self.formGroupBox3)  # redirects to another window
        layout.addWidget(self.b1)  # intitialized button b1(start) onto the main window
        self.setMinimumSize(400, 300)
        self.setLayout(layout)  # the main window
        self.setWindowTitle("Foton")

    # ----------------------------------------------------START--------------------------------------------------------------------------------------
    # ------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------
    def state3(self):
        if self.b1.isChecked():
            self.formGroupBox3.show()
            self.b1.hide()
        else:
            self.formGroupBox3.hide()

    # ----------------------------------------------------FEATURES--------------------------------------------------------------------------------------
    # ------------------------------------------------------WINDOW------------------------------------------------------------------------------------------
    def nextFeatures(self):
        self.formGroupBox3 = QGroupBox("Tools")
        self.btn2 = QPushButton("Image Grouping")
        self.btn2.setCheckable(False)
        self.btn2.toggle()
        self.btn2.clicked.connect(self.state)  # redirects to its function 'state'
        self.btn3 = QPushButton("Edit")
        self.btn3.setCheckable(False)
        self.btn3.toggle()
        self.btn3.clicked.connect(self.state2)  # redirects to its function 'state2'
        self.btn4 = QPushButton("Dataset")
        self.btn4.setCheckable(False)
        self.btn4.toggle()
        self.btn4.clicked.connect(self.state4)  # redirects to its function 'state4'
        self.btn5 = QPushButton("Manual Image Sorting")
        self.btn5.setCheckable(False)
        self.btn5.toggle()
        self.btn5.clicked.connect(self.state5)  # redirects to its function 'state5'
        self.btn6 = QPushButton("Face Identifier")
        self.btn6.setCheckable(False)
        self.btn6.toggle()
        self.btn6.clicked.connect(self.state7)  # redirects to its function 'state5'

        vbox = QVBoxLayout()  # tools window
        self.formGroupBox3.hide()
        self.formGroupBox3.setLayout(vbox)
        vbox.addWidget(self.btn2)
        vbox.addWidget(self.btn3)
        vbox.addWidget(self.btn4)
        vbox.addWidget(self.btn5)
        vbox.addWidget(self.btn6)
        vbox.addStretch(0)


    # ----------------------------------------------------IMAGE GROUPING--------------------------------------------------------------------------------------
    # ------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------
    def state(self):
        if self.btn2.isChecked():
            self.formGroupBox.hide()  # opens another window
        else:
            self.formGroupBox.show()

    # ----------------------------------------------------IMAGE GROUPING-------------------------------------------------------------------------------------
    # ------------------------------------------------------WINDOW------------------------------------------------------------------------------------------
    def createSettings(self):  # image grouping window
        self.formGroupBox = QGroupBox("Settings")
        flayout = QFormLayout()
        self.formGroupBox.hide()
        self.formGroupBox.setLayout(flayout)
        self.btn = QPushButton("Select folder")
        self.btn.clicked.connect(self.selectFolder)  # redirects to select folder function
        self.kmeans = QSpinBox()
        self.kmeans.setRange(2, 15)
        self.kmeans.setValue(2)
        self.sample = QSpinBox()
        self.sample.setRange(32, 256)
        self.sample.setValue(128)
        self.sample.setSingleStep(2)
        self.move = QCheckBox()
        self.size = QCheckBox()
        self.runbtn = QPushButton("Run")
        self.runbtn.clicked.connect(self.run)
        flayout.addRow(self.btn)
        flayout.addRow(QLabel("N. Groups:"), self.kmeans)
        flayout.addRow(QLabel("Resample:"), self.sample)
        flayout.addRow(QLabel("Move:"), self.move)
        flayout.addRow(QLabel("Size:"), self.size)
        flayout.addRow(self.runbtn)

    # SELECT FOLDER FUNCTION#
    def selectFolder(self):
        QFileDialog.FileMode(QFileDialog.Directory)
        self.dir = QFileDialog.getExistingDirectory(self)
        self.btn.setText(self.dir or "Select folder")

    # PROGRESS BUTTONS FUNCTION#
    def disableButton(self):
        self.runbtn.setText("Working...")
        self.runbtn.setEnabled(False)

    def enableButton(self):
        self.runbtn.setText("Run")
        self.runbtn.setEnabled(True)

    def run(self):
        self.disableButton()
        types = ('*.jpg', '*.JPG', '*.png', '*.jpeg')
        imagePaths = []
        folder = self.dir
        if not folder.endswith("/"):
            folder += "/"
        for files in types:
            imagePaths.extend(sorted(glob.glob(folder + files)))
        nimages = len(imagePaths)
        nfolders = int(math.log(self.kmeans.value(), 10)) + 1
        if nimages <= 0:
            QMessageBox.warning(self, "Error", 'No images found!')
            self.enableButton()
            return
        k = K_means(self.kmeans.value(), self.size.isChecked(), self.sample.value())
        k.generate_k_clusters(imagePaths)
        k.rearrange_clusters()
        for i in range(k.k):
            try:
                os.makedirs(folder + str(i + 1).zfill(nfolders))
            except Exception as e:
                print("Folder already exists", e)
        action = shutil.copy
        if self.move.isChecked():
            action = shutil.move
        for i in range(len(k.cluster)):
            action(k.end[i], folder + "/" + str(k.cluster[i] + 1).zfill(nfolders) + "/")
        QMessageBox.information(self, "Done", 'Done!')
        self.enableButton()


    # ----------------------------------------------------EDIT--------------------------------------------------------------------------------------
    # ------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------
    def state2(self):
        if self.btn3.isChecked():
            self.formGroupBox2.hide()
        else:
            self.formGroupBox2.show()

    # ----------------------------------------------------EDIT-------------------------------------------------------------------------------------
    # ------------------------------------------------------WINDOW------------------------------------------------------------------------------------------
    def editSettings(self):
        self.formGroupBox2 = QGroupBox("Edit")
        self.img = QPushButton('Open Image')
        layout2 = QFormLayout()
        hbox_address = QHBoxLayout()
        self.address = QLineEdit()
        hbox_address.addWidget(self.address)
        self.inp = QLineEdit()
        self.img.clicked.connect(self.open)
        hbox_size = QHBoxLayout()
        self.label_width = QLabel('Width :')
        self.label_height = QLabel('Height :')
        self.et_width = QLineEdit()
        self.et_height = QLineEdit()
        hbox_size.addWidget(self.label_width)
        hbox_size.addWidget(self.et_width)
        hbox_size.addWidget(self.label_height)
        hbox_size.addWidget(self.et_height)
        hbox_colorscale = QHBoxLayout()
        self.color_scale = QLabel('Color Scale :')
        self.Grey_scale = QRadioButton('Grey', self)
        self.Hsv = QRadioButton('HSV ', self)
        hbox_colorscale.addWidget(self.color_scale)
        hbox_colorscale.addWidget(self.Grey_scale)
        hbox_colorscale.addWidget(self.Hsv)
        hbox_save = QHBoxLayout()
        self.address_save = QLineEdit()
        hbox_save.addWidget(self.address_save)
        self.btn_save = QPushButton('Save Image')
        self.btn_save.clicked.connect(self.save)
        hbox_save.addWidget(self.btn_save)

        self.img_processed = False
        self.btn_process_img = QPushButton("Process Image")
        self.btn_process_img.clicked.connect(self.getInput)  # redirects to getinput function
        hbox_btn = QHBoxLayout()
        hbox_btn.addWidget(self.btn_process_img)

        layout2.addRow(self.img, self.address)
        layout2.addRow(self.label_height, self.et_height)
        layout2.addRow(self.label_width, self.et_width)
        layout2.addRow(self.color_scale)
        layout2.addRow(self.Grey_scale, self.Hsv)
        layout2.addRow(self.btn_process_img)
        layout2.addRow(self.btn_save)

        self.formGroupBox2.hide()
        self.formGroupBox2.setLayout(layout2)

    # GETINPUT FUNCTION#
    def getInput(self):
        self.req_height = self.et_height.text()
        self.req_width = self.et_width.text()
        if self.req_width != '' and self.req_height != '':
            self.ready = True
            self.img_processed = True
        else:
            self.ready = False

        if self.ready is False:
            QMessageBox.about(self, 'Error', 'Fill parameters to process')
        elif self.address.text() is '':
            QMessageBox.about(self, 'Error', 'Select Image to process')
        else:
            self.req_img = self.process_img(cv2.imread(self.address.text()))
            cv2.imshow("req_img", self.req_img)
        # print(self.req_height,self.req_width)

    # IMAGE PROCESS FUNCTION#
    def process_img(self, imgtoproc):
        if self.Grey_scale.isChecked():
            imgtoproc = cv2.cvtColor(imgtoproc, cv2.COLOR_BGR2GRAY)
        elif self.Hsv.isChecked():
            imgtoproc = cv2.cvtColor(imgtoproc, cv2.COLOR_BGR2HSV)

        return cv2.resize(imgtoproc, (int(self.req_width), int(self.req_height)))

    # OPEN IMAGE FUNCTION#
    def open(self):
        fileName = QFileDialog.getOpenFileName(self, 'openFile')
        self.address.setText(fileName[0])
        self.showImage(fileName[0])
        # print(fileName)

    # SHOWIMAGE FUNCTION#
    def showImage(self, address):
        img = cv2.imread(address)
        cv2.imshow('Yo', img)

    # SAVE IMAGE FUNCTION#
    def save(self):
        if self.img_processed:
            saveFile = QFileDialog.getSaveFileName(self, 'saveFile')
            self.address_save.setText(saveFile[0])
            if saveFile[0] != '':
                cv2.imwrite(str(self.address_save.text()), self.req_img)
        else:
            QMessageBox.about(self, 'Suggestion', 'Do Something')


    # ----------------------------------------------------DATASET COLLECTION-------------------------------------------------------------------------------------
    # --------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------

    def state4(self):
        cam = cv2.VideoCapture(0)
        cv2.namedWindow("test")
        img_counter = 0

        while True:
            ret, frame = cam.read()
            cv2.imshow("test", frame)
            if not ret:
                break
            k = cv2.waitKey(1)

            if k % 256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k % 256 == 32:
                # SPACE pressed
                img_name = "opencv_frame_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1

        cam.release()
        cv2.destroyAllWindows()


    # ----------------------------------------------------MANUAL SORTING-------------------------------------------------------------------------------------
    # ------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------
    def state5(self):
        if self.btn5.isChecked():
            self.formGroupBox5.hide()
        else:
            self.formGroupBox5.show()

    # ----------------------------------------------------MANUAL SORTING-------------------------------------------------------------------------------------
    # ------------------------------------------------------WINDOW------------------------------------------------------------------------------------------
    def manual(self):
        self.formGroupBox5 = QGroupBox("Manual Sorting")
        layout5 = QFormLayout()
        self.btn5 = QPushButton("Start")
        self.label = QLabel('\nInstructions to perform manual image sorting:\n\n • Kindly Press 1 to transfer the image into BRIDE folder\n\n • Kindly Press 2 to transfer the image into GROOM folder')
        self.btn5.setCheckable(False)
        self.btn5.toggle()
        self.btn5.clicked.connect(self.state6)  # redirects to its function 'state6'
        layout5.addRow(self.btn5)
        layout5.addRow(self.label)
        self.formGroupBox5.hide()
        self.formGroupBox5.setLayout(layout5)


    # ----------------------------------------------------MANUAL SORTING-------------------------------------------------------------------------------------
    # ------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------
    def state6(self):
        #exec(open('image_viewer.py').read())
        #import image_viewer
        #image_viewer.main()
        os.system('python image_viewer.py')



    # ----------------------------------------------------FACE IDENTIFIER-------------------------------------------------------------------------------------
    # ------------------------------------------------------FUNCTION------------------------------------------------------------------------------------------
    def state7(self):
        if self.btn6.isChecked():
            self.formGroupBox7.hide()
        else:
            self.formGroupBox7.show()

    # ----------------------------------------------------FACE IDENTIFIER------------------------------------------------------------------------------------
    # ------------------------------------------------------WINDOW------------------------------------------------------------------------------------------
    def facerecog(self):
        self.formGroupBox7 = QGroupBox("Face Identifier")
        layout7 = QFormLayout()
        self.btn7 = QPushButton("Collect New Dataset")
        self.btn7.setCheckable(False)
        self.btn7.toggle()
        self.btn7.clicked.connect(self.datacollect)
        self.btn8 = QPushButton("Train Dataset")
        self.btn8.setCheckable(False)
        self.btn8.toggle()
        self.btn8.clicked.connect(self.datalearning)
        self.btn9 = QPushButton("Identify Face")
        self.btn9.setCheckable(False)
        self.btn9.toggle()
        self.btn9.clicked.connect(self.recognize)
        layout7.addRow(self.btn7)
        layout7.addRow(self.btn8)
        layout7.addRow(self.btn9)
        #layout7.addRow(self.labell)
        self.formGroupBox7.hide()
        self.formGroupBox7.setLayout(layout7)

    #DATACOLLECTION
    def datacollect(self):
        os.system('python datacollecting.py')

    #DATALEARNING
    def datalearning(self):
        os.system('python datalearning.py')

    #TEST
    def recognize(self):
        os.system('python recognizer.py')



def main():
    app = QApplication(sys.argv)
    groupimg = groupImgGUI()
    groupimg.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
