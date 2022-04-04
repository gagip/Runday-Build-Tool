from PyQt5.QtWidgets import (QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt


class GUIManager(QWidget):
    """UI 관련 컴포넌트 배치 및 이벤트 관리 클래스"""
    edit_name = QLineEdit()
    edit_version = QLineEdit()
    note = QTextEdit()
    submit_button = QPushButton("제출")

    def __init__(self):
        super().__init__()
        self.result_dialog = ResultWidget()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('이름:'), 0, 0)
        grid.addWidget(QLabel('버전:'), 1, 0)
        grid.addWidget(QLabel('적용사항:'), 2, 0)
        grid.addWidget(QLabel('참고사항:'), 3, 0)

        grid.addWidget(self.edit_name, 0, 1)
        grid.addWidget(self.edit_version, 1, 1)
        grid.addWidget(self.patch_note, 2, 1)
        grid.addWidget(self.note, 3, 1)
        grid.addWidget(self.submit_button, 4, 1)

        self.submit_button.clicked.connect(self.toString)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(200, 200, 800, 700)
        self.show()

    def toString(self):
        name = self.edit_name.text()
        version = self.edit_version.text()
        patch_note = self.patch_note.toPlainText()
        note = self.note.toPlainText()

        print('제목')
        print(f'[Runday] AOS QA 빌드 파일 공유 - {version}')
        print('내용')
        print(f'안녕하세요 {name}입니다.')
        self.result_dialog.show()


class ResultWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.getTitle("제목"))
        layout.addWidget(self.getContent("dddddsssssdddddddddddddddddddddddddddddddddddddddddd"))

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)

    def getTitle(self, title):
        label = QLabel(title, self)
        label.setAlignment(Qt.AlignVCenter)

        font = label.font()
        font.setPointSize(12)
        font.setBold(True)
        label.setFont(font)
        return label

    def getContent(self, content):
        label = QLabel(content, self)
        label.setAlignment(Qt.AlignVCenter)
        return label
