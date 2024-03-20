import sys
import os
import re
from pytube import YouTube
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setFixedSize(1211, 760)
        MainWindow.setMouseTracking(False)
        # MainWindow.setStyleSheet("background-color: #ffffff;")
        icon = QtGui.QIcon('asset/logo.png')
        MainWindow.setWindowIcon(icon)
        
        # Create the central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Background Image
        background_image = QPixmap("asset/bkk.png")
        background_image = background_image.scaled(1211, 760)
        background_label = QtWidgets.QLabel(self.centralwidget)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0,1211, 760) 

        # Main Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1211, 761))
        self.frame.setAutoFillBackground(False)
        # self.frame.setStyleSheet("background-color: #fff330;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        # text Labels
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(440, 20, 311, 111))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(790, 30, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(160, 40, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(48)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # Widgets...
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(40, 430, 541, 151))
        self.widget.setObjectName("widget")

        #-----------radio button for formate-----------
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 181, 51))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(20, 70, 161, 31))
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        # self.radioButton.setEnabled(False)
        
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(280, 70, 161, 31))
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setEnabled(False)

        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_11 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_11.setGeometry(QtCore.QRect(280, 110, 181, 31))
        self.radioButton_11.setFont(font)
        self.radioButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_11.setEnabled(False)

        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_12 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_12.setGeometry(QtCore.QRect(20, 110, 191, 31))
        self.radioButton_12.setFont(font)
        self.radioButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_12.setObjectName("radioButton_12")
        self.radioButton_12.setEnabled(False)

        # -------radio button for qulaity -----------
        self.widget_5 = QtWidgets.QWidget(self.frame)
        self.widget_5.setGeometry(QtCore.QRect(750, 430, 411, 141))
        self.widget_5.setObjectName("widget_5")
        
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setGeometry(QtCore.QRect(10, 0, 131, 41))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 60, 81, 31))
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_3.setEnabled(False)
        
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 60, 91, 31))
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_4.setObjectName("radioButton_4")

        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_5.setGeometry(QtCore.QRect(220, 100, 91, 31))
        self.radioButton_5.setFont(font)
        self.radioButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_5.setChecked(True)
        
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget_5)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 100, 91, 31))
        self.radioButton_6.setFont(font)
        self.radioButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_6.setEnabled(False)

        #----------entre url -------------------
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setGeometry(QtCore.QRect(40, 130, 1121, 151))
        self.widget_2.setObjectName("widget_2")

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(100, 40, 151, 51))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(12)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(300, 30, 661, 87))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: #ffffff;")
        self.plainTextEdit.setPlaceholderText("Enter Your YouTube Video URL")
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        #-------------directory-------------------
        self.widget_3 = QtWidgets.QWidget(self.frame)
        self.widget_3.setGeometry(QtCore.QRect(40, 290, 1121, 131))
        self.widget_3.setObjectName("widget_3")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(310, 50, 541, 31))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #ffffff;")
        self.lineEdit.setObjectName("lineEdit")
        self.directory = os.path.join(os.path.expanduser("~"), "Downloads")
        self.lineEdit.setText(self.directory)

        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(870, 50, 81, 31))
        self.pushButton.setStyleSheet("background-color: #ffffff;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.change_directory)

        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(110, 40, 141, 41))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        #----------------download button-------------------------
        self.widget_4 = QtWidgets.QWidget(self.frame)
        self.widget_4.setGeometry(QtCore.QRect(340, 640, 481, 101))
        self.widget_4.setObjectName("widget_4")

        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 111, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #ffffff;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.download_videos)

        self.progressBar = QtWidgets.QProgressBar(self.widget_4)
        self.progressBar.setGeometry(QtCore.QRect(110, 60, 251, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "YouTube"))
        self.label_2.setText(_translate("MainWindow", "Video"))
        self.label_3.setText(_translate("MainWindow", "Convert"))
        self.radioButton.setText(_translate("MainWindow", "Video (.mp4)"))
        self.radioButton_2.setText(_translate("MainWindow", "Audio (.mp3)"))
        self.label_4.setText(_translate("MainWindow", "Convert To"))
        self.radioButton_11.setText(_translate("MainWindow", "Audio (.webm)"))
        self.radioButton_12.setText(_translate("MainWindow", "Video (.webm)"))
        self.radioButton_3.setText(_translate("MainWindow", "144p"))
        self.radioButton_4.setText(_translate("MainWindow", "360p"))
        self.label_7.setText(_translate("MainWindow", "Quality"))
        self.radioButton_5.setText(_translate("MainWindow", "720p"))
        self.radioButton_6.setText(_translate("MainWindow", "1080p"))
        self.label_5.setText(_translate("MainWindow", "Enter URL"))
        self.pushButton.setText(_translate("MainWindow", "Change"))
        self.label_6.setText(_translate("MainWindow", "Directory"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))


    def change_directory(self):
        directory = QFileDialog.getExistingDirectory(None, "Select Directory", self.directory, QFileDialog.ShowDirsOnly)
        if directory:
            self.directory = directory
        self.lineEdit.setText(directory)

    def download_videos(self):
        # Get the text from the QPlainTextEdit
        text = self.plainTextEdit.toPlainText()
        # Split the text into separate lines, URLs, or by comma
        urls = re.split(r'[\n, ]+', text)
        
        if not urls:
            QMessageBox.warning(self.centralwidget, "Error", "Please enter valid YouTube video URL(s).")
            return
        # Check if the download directory exists, and create it if it doesn't
        if not os.path.exists(self.directory):
            try:
                os.makedirs(self.directory)
            except OSError as e:
                QMessageBox.critical(self.centralwidget, "Error", f"Failed to create download directory: {str(e)}")
                return
            

        desired_resolution = self.get_selected_quality()
        if desired_resolution is None:
            QMessageBox.warning(self.centralwidget, "Error", "Please select resolution of YouTube video.")
            return
        
        # Download each video
        for url in urls:
            try:
                yt = YouTube(url)
                streams = yt.streams.filter(progressive=True)
                # stream = yt.streams.get_highest_resolution()
                stream = None
                print(streams)
                for s in streams:
                    if s.resolution == desired_resolution:
                        stream = s
                        break
                    
                if stream is not None:
                    # Get the quality of the video
                    quality = stream.resolution or "Unknown"
                    # Construct the file name with quality prefix
                    file_name = f"{quality}_{yt.title}.{stream.subtype}"
                    
                    # Download the video
                    stream.download(output_path=self.directory, filename=re.sub(r'[<>:"/\\|?*]', '_', file_name))

                    QMessageBox.information(self.centralwidget, "Download Complete", "Video downloaded successfully!")
                else:
                    QMessageBox.warning(self.centralwidget, "Resolution Not Available", f"Requested resolution '{desired_resolution}' not available for this video!")
            except Exception as e:
                print(str(e))
                QMessageBox.critical(self.centralwidget, "Error", f"An error occurred: {str(e)}")

    def get_selected_quality(self):
        if self.radioButton_4.isChecked():
            return '360p'
        elif self.radioButton_5.isChecked():
            return '720p'
        else:
            return None



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
