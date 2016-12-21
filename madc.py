from PyQt4 import QtGui, QtCore
import sys
import serial
import time


class PortSelector(QtGui.QWidget):
    def __init__(self, port):
        super(PortSelector, self).__init__()
        print "opened Port Selection Window"
        self.initGui(port)

    def initGui(self, port):
        self.setWindowTitle("Select A Serial Port")
        self.setWindowIcon(QtGui.QIcon("MadC.png"))
        self.setGeometry(100, 100, 320, 240)

    def test(self):
        return "com7"


class MADC(QtGui.QMainWindow):
    def __init__(self, RES_X, RES_Y, W_TITLE, W_ICON):
        super(MADC, self).__init__()
        print "initialized successfully"
        self.RES_X = RES_X
        self.RES_Y = RES_Y
        self.W_TITLE = W_TITLE
        self.W_ICON = W_ICON
        self.buttons = {
            0: {
                "name": "&Select Port"
            },
            1: {
                "name": "&Open Image"
            },
            2: {
                "name": "&Adjust"
            },
            3: {
                "name": "&Print"
            },
            4: {
                "name": "&Reset"
            },
            5: {
                "name": "&Manual"
            }
        }
        self.port = "gfg"
        self.portselect = PortSelector(self.port)
        self.initGui()

    def initGui(self):
        self.setWindowTitle(self.W_TITLE)
        self.setWindowIcon(QtGui.QIcon(self.W_ICON))
        self.setGeometry(50, 50, self.RES_X, self.RES_Y)

        self.addGuiElements()

        self.show()

    def addGuiElements(self):
        scl = 10

        centralWidget = QtGui.QWidget(self)
        centralWidgetLayout = QtGui.QVBoxLayout()  # Widget layout global
        buttonBarLayout = QtGui.QHBoxLayout()  # Buttons layout

        centralWidget.setLayout(centralWidgetLayout)

        for btn in self.buttons:
            self.buttons[btn]["obj"] = QtGui.QPushButton(self.buttons[btn]["name"], self)
            QtCore.QObject.connect(self.buttons[btn]["obj"], QtCore.SIGNAL('clicked()'), self.button_actions)
            buttonBarLayout.addWidget(self.buttons[btn]["obj"])

        buttonBarLayout.addStretch(1)

        pictureFrame = QtGui.QFrame()
        pictureFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        pictureFrame.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        pixmap = QtGui.QPixmap("MadC.png").scaled(512, 512, QtCore.Qt.KeepAspectRatio)
        picLabel = QtGui.QLabel("Image", self)
        picLabel.setPixmap(pixmap)
        picLayout = QtGui.QVBoxLayout()
        picLayout.addWidget(picLabel)
        pictureFrame.setLayout(picLayout)

        serialFrame = QtGui.QFrame()
        serialFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        serialFrame.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        serialTextBox = QtGui.QLabel("Serial", self)
        serialTextBox.setText("Bla bla bla! Here goes the serial monitor stream!")
        serialLayout = QtGui.QVBoxLayout()
        serialLayout.addWidget(serialTextBox)
        serialFrame.setLayout(serialLayout)

        rawDataFrame = QtGui.QFrame()
        rawDataFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        rawDataFrame.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        rawDataTextBox = QtGui.QLabel("Data", self)
        rawDataTextBox.setText("alb alb alb! Here goes raw data!")
        rawDataLayout = QtGui.QVBoxLayout()
        rawDataLayout.addWidget(rawDataTextBox)
        rawDataFrame.setLayout(rawDataLayout)

        rightSplitter = QtGui.QSplitter(QtCore.Qt.Vertical)
        rightSplitter.addWidget(serialFrame)
        rightSplitter.addWidget(rawDataFrame)
        # rightSplitter.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        mainSplitter = QtGui.QSplitter(QtCore.Qt.Horizontal)
        mainSplitter.addWidget(pictureFrame)
        mainSplitter.addWidget(rightSplitter)

        centralWidgetLayout.addLayout(buttonBarLayout)
        centralWidgetLayout.addWidget(mainSplitter)

        self.setCentralWidget(centralWidget)

    def button_actions(self):
        sender = self.sender()
        action = sender.text()[1:]
        print action
        isportopen = False
        try:
            ser = serial.Serial('COM3')
            isportopen = True
            print ser.is_open
        except:
            print "Could not open port"
        if action == "Select Port":
            print "Please select a valid COM port"
            time.sleep(0.1)
            self.portselect.show()
            print self.port
            self.port = self.portselect.test()
            print self.port
            # ser.write('1')
            pass
        elif action == "Open Image":
            print "Please select an Image to print"
            time.sleep(0.1)
            # ser.write('2')
            pass
        elif action == "Adjust":
            time.sleep(0.1)
            # ser.write('3')
            pass
        elif action == "Print":
            time.sleep(0.1)
            # ser.write('4')
            pass
        elif action == "Reset":
            time.sleep(0.1)
            # ser.write('5')
            pass
        elif action == "Manual":
            time.sleep(0.1)
            # ser.write('6')
            pass
        else:
            print "I don't know how you even reached here!!"
        if isportopen:
            ser.close()


width = 800
height = 600
title = "MadC | Multi Axis Device Control"
icon = "MadC.png"

app = QtGui.QApplication(sys.argv)
instance = MADC(width, height, title, icon)
# x = PortSelector()
sys.exit(app.exec_())
