import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow
from pygame import mixer
from design import Ui_MainWindow
import PySide6
from pytube import YouTube


class DT(QMainWindow):
    def __init__(self):
        super(DT, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.download_video)
        self.ui.pushButton_2.clicked.connect(self.get_res)
        self.ui.pushButton_3.clicked.connect(self.get_res)

    def get_res(self):
        d = self.sender()
        self.res = d.text()
        print(self.res)

    def download_video(self):
        youtubeObject = YouTube(self.ui.lineEdit.text())
        youtubeObject = youtubeObject.streams.get_by_resolution(self.res)
        try:
            youtubeObject.download('D:\DownTubeVids')
        except:
            self.ui.label_7.setText('ERR')
        self.ui.label_7.setText('DONE')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DT()
    window.show()

    sys.exit(app.exec())
