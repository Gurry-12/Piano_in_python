from PyQt5 import QtCore, QtWidgets
import playsound
from threading import Thread
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 245)
        self.mw  = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.c4 = QtWidgets.QPushButton(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(20, 30, 41, 181))
        self.c4.setStyleSheet("#c4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#c4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.c4.setText("")
        self.c4.setObjectName("c4")
        self.d4 = QtWidgets.QPushButton(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(60, 30, 41, 181))
        self.d4.setStyleSheet("#d4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#d4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.d4.setText("")
        self.d4.setObjectName("d4")
        self.c40 = QtWidgets.QPushButton(self.centralwidget)
        self.c40.setGeometry(QtCore.QRect(40, 30, 31, 111))
        self.c40.setStyleSheet("#c40{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#c40:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.c40.setText("")
        self.c40.setObjectName("c40")
        self.d40 = QtWidgets.QPushButton(self.centralwidget)
        self.d40.setGeometry(QtCore.QRect(80, 30, 31, 111))
        self.d40.setStyleSheet("#d40{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#d40:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.d40.setText("")
        self.d40.setObjectName("d40")
        self.e4 = QtWidgets.QPushButton(self.centralwidget)
        self.e4.setGeometry(QtCore.QRect(100, 30, 41, 181))
        self.e4.setStyleSheet("#e4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#e4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.e4.setText("")
        self.e4.setObjectName("e4")
        self.f4 = QtWidgets.QPushButton(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(140, 30, 41, 181))
        self.f4.setStyleSheet("#f4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#f4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.f4.setText("")
        self.f4.setObjectName("f4")
        self.g4 = QtWidgets.QPushButton(self.centralwidget)
        self.g4.setGeometry(QtCore.QRect(180, 30, 41, 181))
        self.g4.setStyleSheet("#g4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#g4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.g4.setText("")
        self.g4.setObjectName("g4")
        self.a4 = QtWidgets.QPushButton(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(220, 30, 41, 181))
        self.a4.setStyleSheet("#a4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#a4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.a4.setText("")
        self.a4.setObjectName("a4")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(260, 30, 41, 181))
        self.b4.setStyleSheet("#b4{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#b4:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.c5 = QtWidgets.QPushButton(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(300, 30, 41, 181))
        self.c5.setStyleSheet("#c5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#c5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.c5.setText("")
        self.c5.setObjectName("c5")
        self.d5 = QtWidgets.QPushButton(self.centralwidget)
        self.d5.setGeometry(QtCore.QRect(340, 30, 41, 181))
        self.d5.setStyleSheet("#d5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#d5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.d5.setText("")
        self.d5.setObjectName("d5")
        self.a5 = QtWidgets.QPushButton(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(500, 30, 41, 181))
        self.a5.setStyleSheet("#a5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#a5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.a5.setText("")
        self.a5.setObjectName("a5")
        self.e5 = QtWidgets.QPushButton(self.centralwidget)
        self.e5.setGeometry(QtCore.QRect(380, 30, 41, 181))
        self.e5.setStyleSheet("#e5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#e5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.e5.setText("")
        self.e5.setObjectName("e5")
        self.g5 = QtWidgets.QPushButton(self.centralwidget)
        self.g5.setGeometry(QtCore.QRect(460, 30, 41, 181))
        self.g5.setStyleSheet("#g5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#g5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.g5.setText("")
        self.g5.setObjectName("g5")
        self.f5 = QtWidgets.QPushButton(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(420, 30, 41, 181))
        self.f5.setStyleSheet("#f5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#f5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.f5.setText("")
        self.f5.setObjectName("f5")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(540, 30, 41, 181))
        self.b5.setStyleSheet("#b5{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#b5:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.c6 = QtWidgets.QPushButton(self.centralwidget)
        self.c6.setGeometry(QtCore.QRect(580, 30, 41, 181))
        self.c6.setStyleSheet("#c6{\n"
	"background-color: rgb(242, 242, 242);\n"
	"background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"\n"
	"\n"
	"#c6:pressed{\n"
	"background-color: rgb(250, 250, 250);\n"
	"\n"
	"}")
        self.c6.setText("")
        self.c6.setObjectName("c6")
        self.f40 = QtWidgets.QPushButton(self.centralwidget)
        self.f40.setGeometry(QtCore.QRect(160, 30, 31, 111))
        self.f40.setStyleSheet("#f40{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#f40:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.f40.setText("")
        self.f40.setObjectName("f40")
        self.g40 = QtWidgets.QPushButton(self.centralwidget)
        self.g40.setGeometry(QtCore.QRect(200, 30, 31, 111))
        self.g40.setStyleSheet("#g40{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#g40:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.g40.setText("")
        self.g40.setObjectName("g40")
        self.a40 = QtWidgets.QPushButton(self.centralwidget)
        self.a40.setGeometry(QtCore.QRect(240, 30, 31, 111))
        self.a40.setStyleSheet("#a40{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#a40:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.a40.setText("")
        self.a40.setObjectName("a40")
        self.c50 = QtWidgets.QPushButton(self.centralwidget)
        self.c50.setGeometry(QtCore.QRect(320, 30, 31, 111))
        self.c50.setStyleSheet("#c50{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#c50:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.c50.setText("")
        self.c50.setObjectName("c50")
        self.d50 = QtWidgets.QPushButton(self.centralwidget)
        self.d50.setGeometry(QtCore.QRect(360, 30, 31, 111))
        self.d50.setStyleSheet("#d50{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#d50:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.d50.setText("")
        self.d50.setObjectName("d50")
        self.f50 = QtWidgets.QPushButton(self.centralwidget)
        self.f50.setGeometry(QtCore.QRect(440, 30, 31, 111))
        self.f50.setStyleSheet("#f50{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#f50:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.f50.setText("")
        self.f50.setObjectName("f50")
        self.g50 = QtWidgets.QPushButton(self.centralwidget)
        self.g50.setGeometry(QtCore.QRect(480, 30, 31, 111))
        self.g50.setStyleSheet("#g50{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#g50:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.g50.setText("")
        self.g50.setObjectName("g50")
        self.a50 = QtWidgets.QPushButton(self.centralwidget)
        self.a50.setGeometry(QtCore.QRect(520, 30, 31, 111))
        self.a50.setStyleSheet("#a50{\n"
	"background-color: rgb(0, 0, 0);\n"
	"background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
	"}\n"
	"#a50:pressed{\n"
	"background-color: rgb(0, 0, 0);\n"
	"\n"
	"    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
	"\n"
	"}\n"
	"")
        self.a50.setText("")
        self.a50.setObjectName("a50")
        self.c4.raise_()
        self.d4.raise_()
        self.c40.raise_()
        self.e4.raise_()
        self.f4.raise_()
        self.d40.raise_()
        self.g4.raise_()
        self.a4.raise_()
        self.b4.raise_()
        self.c5.raise_()
        self.d5.raise_()
        self.a5.raise_()
        self.e5.raise_()
        self.g5.raise_()
        self.f5.raise_()
        self.b5.raise_()
        self.c6.raise_()
        self.f40.raise_()
        self.g40.raise_()
        self.a40.raise_()
        self.c50.raise_()
        self.d50.raise_()
        self.f50.raise_()
        self.g50.raise_()
        self.a50.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.th = {}
        self.c4.clicked.connect(self.run_threads)
        self.d4.clicked.connect(self.run_threads)
        self.e4.clicked.connect(self.run_threads)
        self.f4.clicked.connect(self.run_threads)
        self.g4.clicked.connect(self.run_threads) 
        self.a4.clicked.connect(self.run_threads) 
        self.b4.clicked.connect(self.run_threads) 
        self.c5.clicked.connect(self.run_threads) 
        self.d5.clicked.connect(self.run_threads) 
        self.e5.clicked.connect(self.run_threads) 
        self.f5.clicked.connect(self.run_threads)
        self.g5.clicked.connect(self.run_threads) 
        self.a5.clicked.connect(self.run_threads) 
        self.b5.clicked.connect(self.run_threads) 
        self.c6.clicked.connect(self.run_threads) 

        self.c40.clicked.connect(self.run_threads) 
        self.c50.clicked.connect(self.run_threads) 
        self.d40.clicked.connect(self.run_threads) 
        self.d50.clicked.connect(self.run_threads) 
        self.f40.clicked.connect(self.run_threads) 
        self.f50.clicked.connect(self.run_threads) 
        self.g40.clicked.connect(self.run_threads) 
        self.g50.clicked.connect(self.run_threads) 
        self.a40.clicked.connect(self.run_threads) 
        self.a50.clicked.connect(self.run_threads)
    def play_notes(self,notePath):
        playsound.playsound(notePath,False)
        # print(notePath)
    def run_threads(self):
        self.th[self.mw.sender().objectName()] = Thread(target = self.play_notes, args = ('Piano_Python\\Sounds\\'+'{}.wav'.format(self.mw.sender().objectName()),)) 
        self.th[self.mw.sender().objectName()].start()
        self.th[self.mw.sender().objectName()].join()
		
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Piano"))
        self.c4.setShortcut(_translate("MainWindow", "q"))
        self.c40.setShortcut(_translate("MainWindow", "2"))
        self.d4.setShortcut(_translate("MainWindow", "w"))
        self.d40.setShortcut(_translate("MainWindow", "3"))
        self.e4.setShortcut(_translate("MainWindow", "e"))
        self.f4.setShortcut(_translate("MainWindow", "r"))
        self.f40.setShortcut(_translate("MainWindow", "5"))
        self.g4.setShortcut(_translate("MainWindow", "t"))
        self.g40.setShortcut(_translate("MainWindow", "6"))
        self.a4.setShortcut(_translate("MainWindow", "y"))
        self.a40.setShortcut(_translate("MainWindow", "7"))
        self.b4.setShortcut(_translate("MainWindow", "u"))
        self.c5.setShortcut(_translate("MainWindow", "c"))
        self.d5.setShortcut(_translate("MainWindow", "v"))
        self.e5.setShortcut(_translate("MainWindow", "b"))
        self.f5.setShortcut(_translate("MainWindow", "n"))
        self.g5.setShortcut(_translate("MainWindow", "m"))
        self.a5.setShortcut(_translate("MainWindow", ","))
        self.b5.setShortcut(_translate("MainWindow", "."))
        self.c6.setShortcut(_translate("MainWindow", "/"))
        self.c50.setShortcut(_translate("MainWindow", "f"))
        self.d50.setShortcut(_translate("MainWindow", "g"))
        self.f50.setShortcut(_translate("MainWindow", "j"))
        self.g50.setShortcut(_translate("MainWindow", "k"))
        self.a50.setShortcut(_translate("MainWindow", "l"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())