# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stackover.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time

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
        MainWindow.resize(634, 435)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(60, 160, 491, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 92, 35))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 120, 101, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 30, 411, 51))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 634, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "start", None))
        self.label.setText(_translate("MainWindow", "function output", None))


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


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        t = Timer(self, maximum=500, interval=1000, timeout=self.testfuc)
        self.pushButton.clicked.connect(t.start)

    def testfuc(self, i):
        name = self.textEdit.toPlainText()
        self.listWidget.addItem(("%s %d") % (name, i))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
