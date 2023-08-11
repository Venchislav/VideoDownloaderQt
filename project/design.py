
################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(565, 358)
        MainWindow.setMinimumSize(QSize(565, 358))
        MainWindow.setMaximumSize(QSize(565, 358))
        icon = QIcon()
        icon.addFile(u":/files/download-circular-button.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	color: black;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 7px;\n"
"	color: white;\n"
"	background-color: black;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 40, 71, 71))
        self.label.setPixmap(QPixmap(u":/files/youtube.png"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(178, 120, 221, 31))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(142, 200, 291, 22))
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 180, 61, 61))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(40, 40))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 330, 141, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 330, 141, 31))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(450, 330, 131, 31))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(220, 270, 141, 31))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 230, 201, 31))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 160, 61, 31))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 9px;\n"
"}")
        self.pushButton_2.setIconSize(QSize(40, 40))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(300, 160, 61, 31))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 9px;\n"
"}")
        self.pushButton_3.setIconSize(QSize(40, 40))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DownTube", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DOWNLOADER", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video Link:", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"VENCHISLAV", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"2023", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PYTHON", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"V 0.2", None))
        self.label_7.setText("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"720p", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"360p", None))
    # retranslateUi

