import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.edit_version = QLineEdit()
        self.edit_name = QLineEdit()
        self.patch_note = QTextEdit()
        self.button = QPushButton("확인")

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('이름:'), 0, 0)
        grid.addWidget(QLabel('버전:'), 1, 0)
        grid.addWidget(QLabel('적용사항:'), 2, 0)

        grid.addWidget(self.edit_name, 0, 1)
        grid.addWidget(self.edit_version, 1, 1)
        grid.addWidget(self.patch_note, 2, 1)
        grid.addWidget(self.button, 3, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
