# -*- coding: utf-8 -*-


from PyQt4 import QtCore, QtGui


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(660, 653)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 681, 751))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(0, -30, 681, 741))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.textEdit = QtGui.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(130, 100, 471, 71))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(240, 70, 181, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(250, 40, 181, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(0, 220, 671, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 290, 101, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setGeometry(QtCore.QRect(0, 400, 681, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 460, 91, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(130, 180, 111, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 670, 92, 35))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 590, 92, 35))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(150, 250, 451, 141))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(self.groupBox)
        self.listWidget_2.setGeometry(QtCore.QRect(150, 420, 451, 161))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.listView_3 = QtGui.QListView(self.tab_4)
        self.listView_3.setGeometry(QtCore.QRect(0, -10, 671, 541))
        self.listView_3.setObjectName(_fromUtf8("listView_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 540, 92, 35))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox", None))
        self.label_2.setText(_translate("MainWindow", '<html><head/><body><p><span style=" font-size:12pt; font-weight:600;">Enter URL :</span></p></body></html>', None))
        self.label.setText(_translate("MainWindow", '<html><head/><body><p><span style=" font-size:18pt; font-weight:600;">Zillow Scraper</span></p></body></html>', None)
        )
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>URL processing</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p>Scraping Info</p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Start Scraping", None))
        self.pushButton_2.setText(_translate("MainWindow", "Exit", None))
        self.pushButton_3.setText(_translate("MainWindow", "Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 1", None))
        self.pushButton_4.setText(_translate("MainWindow", "Load Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Tab 2", None))


class Timer(QtCore.QObject):
    timeout = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal()

    def __init__(self, parent=None, **kwargs):
        self._maximum = kwargs.pop("maximum", 0)
        _interval = kwargs.pop("interval", 0)
        _timeout = kwargs.pop("timeout", None)
        _finished = kwargs.pop("finished", None)

        if parent is not None:
            kwargs["parent"] = parent
        super(Timer, self).__init__(**kwargs)
        self._counter = 0
        self._timer = QtCore.QTimer(timeout=self._on_timeout)
        self.interval = _interval
        if _timeout:
            self.timeout.connect(_timeout)
        if _finished:
            self.timeout.connect(_finished)

    @QtCore.pyqtSlot()
    def start(self):
        self._timer.start()

    @property
    def interval(self):
        return self._timer.interval()

    @interval.setter
    def interval(self, v):
        self._timer.setInterval(v)

    @property
    def maximum(self):
        return self._maximum

    @maximum.setter
    def maximum(self, v):
        self._maximum = v

    @QtCore.pyqtSlot()
    def _on_timeout(self):
        self.timeout.emit(self._counter)
        self._counter += 1
        if self._counter >= self.maximum:
            self.finished.emit()
            self._timer.stop()


# https://www.riverbankcomputing.com/static/Docs/PyQt4/designer.html#using-the-generated-code
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        t = Timer(self, maximum=500, interval=1000, timeout=self.onTimeout)
        t.start()

    @QtCore.pyqtSlot(int)
    def onTimeout(self, i):
        self.listWidget_2.addItem(str(i))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
