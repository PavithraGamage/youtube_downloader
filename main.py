# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yt_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import images_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from pytube import YouTube
import validators
import os


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(771, 347)
        main_window.setMinimumSize(QtCore.QSize(771, 347))
        main_window.setMaximumSize(QtCore.QSize(771, 347))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image_pfx/icons8-youtube-70.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        main_window.setWindowIcon(icon)
        main_window.setWhatsThis("Hello Hello")

        # title
        self.label = QtWidgets.QLabel(main_window)
        self.label.setGeometry(QtCore.QRect(60, 40, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # line
        self.line = QtWidgets.QFrame(main_window)
        self.line.setGeometry(QtCore.QRect(60, 100, 631, 20))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # URL input
        self.youtube_url = QtWidgets.QPlainTextEdit(main_window)
        self.youtube_url.setGeometry(QtCore.QRect(80, 150, 601, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        self.youtube_url.setFont(font)
        self.youtube_url.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.youtube_url.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard | QtCore.Qt.LinksAccessibleByMouse | QtCore.Qt.TextBrowserInteraction | QtCore.Qt.TextEditable | QtCore.Qt.TextEditorInteraction | QtCore.Qt.TextSelectableByKeyboard | QtCore.Qt.TextSelectableByMouse)
        self.youtube_url.setPlaceholderText("Place your URL here")
        self.youtube_url.setObjectName("youtube_url")

        # download btn
        self.download_btn = QtWidgets.QPushButton(main_window)
        self.download_btn.setGeometry(QtCore.QRect(300, 250, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.download_btn.setFont(font)
        self.download_btn.setObjectName("download_btn")

        # version label
        self.label_2 = QtWidgets.QLabel(main_window)
        self.label_2.setGeometry(QtCore.QRect(710, 310, 41, 16))
        self.label_2.setObjectName("label_2")

        # youtube icon
        self.label_3 = QtWidgets.QLabel(main_window)
        self.label_3.setGeometry(QtCore.QRect(630, 30, 71, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/image_pfx/icons8-youtube-70.png"))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)
        main_window.setTabOrder(self.youtube_url, self.download_btn)

        # clicked function
        def clicked():

            # check errors for validations
            error = 0

            # check empty
            url_check = self.youtube_url.toPlainText()

            if not url_check and error == 0:

                # set error to one
                error = 1

                # message declare
                msg = QtWidgets.QMessageBox()

                # message box icon
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/image_pfx/icons8-youtube-70.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg.setWindowIcon(icon)

                # message box icon
                msg.setIcon(QtWidgets.QMessageBox.Information)

                # message window title
                msg.setWindowTitle("Information")

                # message box information
                msg.setText("YouTube URL can not be empty")

                # message box buttons
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # message box execute
                msg.exec_()

            # validate url
            if not validators.url(url_check) and error == 0:

                # set error to one
                error = 1

                # message declare
                msg = QtWidgets.QMessageBox()

                # message box icon
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/image_pfx/icons8-youtube-70.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg.setWindowIcon(icon)

                # message box icon
                msg.setIcon(QtWidgets.QMessageBox.Information)

                # message window title
                msg.setWindowTitle("Information")

                # message box information
                msg.setText("Please use valid url")

                # message box buttons
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # message box execute
                msg.exec_()

            # find YouTube
            find = url_check.find("youtube.com")
            if find != 12 and error == 0:

                # set error to one
                error = 1

                # message declare
                msg = QtWidgets.QMessageBox()

                # message box icon
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(":/image_pfx/icons8-youtube-70.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
                msg.setWindowIcon(icon)

                # message box icon
                msg.setIcon(QtWidgets.QMessageBox.Information)

                # message window title
                msg.setWindowTitle("Information")

                # message box information
                msg.setText("The URL does not belongs to YouTube")

                # message box buttons
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

                # message box execute
                msg.exec_()

            if error == 0:

                # input url capture
                url = YouTube(self.youtube_url.toPlainText())

                # video title
                title = url.title
                print(title)

                # video thumbnail
                thumbnail = url.thumbnail_url
                print(thumbnail)

                # get os username
                username = os.getlogin()

                # stream mode current 720p
                stream = url.streams.get_by_itag(22)

                # file download path
                path = "C:/Users/" + username + "/Documents/YouTube/"

                # start downloading
                stream.download(path)

                # open file location
                os.system('start C:/Users/' + username + '/Documents/YouTube/')

        # button action
        self.download_btn.clicked.connect(clicked)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "YouTube Downloader"))
        self.label.setText(_translate("main_window", "Youtube Downloader"))
        self.download_btn.setText(_translate("main_window", "Download"))
        self.label_2.setText(_translate("main_window", "v 1.0"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QDialog()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
