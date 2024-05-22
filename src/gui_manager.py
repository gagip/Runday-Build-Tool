from PyQt5.QtGui import *
from PyQt5.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QTextBrowser, QTextEdit, QVBoxLayout,
                             QWidget)

from src.qr_manger import BitlyAPI, QRCodeAPI


class GUIManager(QWidget):
    """UI 관련 컴포넌트 배치 및 이벤트 관리 클래스"""

    def __init__(self, bitly_api: BitlyAPI):
        super().__init__()
        self.bitly_api = bitly_api
        self._qrcodeAPI = None

        self.edit_version = QLineEdit()
        self.live_cdn = QLineEdit()
        self.test_cdn = QLineEdit()
        self.patch_note = QTextEdit()
        self.note = QTextEdit()
        self.submit_button = QPushButton("제출")
        self.result_dialog = MyApp()
        self.result_dialog.hide()
        self.live_qrcode_dialog = QRCodeDialog("라이브", "qrcode_live.png")
        self.live_qrcode_dialog.hide()
        self.test_qrcode_dialog = QRCodeDialog("테스트", "qrcode_test.png")
        self.test_qrcode_dialog.hide()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        # label
        grid.addWidget(QLabel("버전:"), 0, 0)
        grid.addWidget(QLabel("라이브 서버 CDN:"), 1, 0)
        grid.addWidget(QLabel("테스트 서버 CDN:"), 2, 0)
        grid.addWidget(QLabel("적용사항:"), 3, 0)
        grid.addWidget(QLabel("참고사항:"), 4, 0)
        # input
        grid.addWidget(self.edit_version, 0, 1)
        grid.addWidget(self.live_cdn, 1, 1)
        grid.addWidget(self.test_cdn, 2, 1)
        grid.addWidget(self.patch_note, 3, 1)
        grid.addWidget(self.note, 4, 1)
        grid.addWidget(self.submit_button, 5, 1)
        # handler
        self.submit_button.clicked.connect(self.submit)
        # window
        self.setWindowTitle("QGridLayout")
        self.setGeometry(200, 200, 800, 700)
        self.show()

    def submit(self):
        """입력한 내용에 맞춰 결과 화면 출력"""
        self.toString()
        self.result_dialog.show()

    def toString(self):
        dialog = self.result_dialog
        version = self.edit_version.text()
        live_cdn = self.live_cdn.text()
        test_cdn = self.test_cdn.text()
        patch_note = self.patch_note.toPlainText()
        note = self.note.toPlainText()

        dialog.clear_text()
        dialog.set_title(f"[Runday] AOS QA 빌드 파일 공유 - {version}")
        dialog.append_text(
            f"안녕하세요 손찬우입니다. 이번 버전 {version} QA 빌드 공유드립니다."
        )
        dialog.append_text("\n\n")
        dialog.append_text("■ 다운로드 링크")
        if live_cdn.strip() != "":
            live_cdn_url = self.shorten_url(live_cdn, True)
            dialog.append_text(f"\t- 라이브 서버: {live_cdn_url}")
            self.live_qrcode_dialog.show()
            dialog.append_text("\n\n")
        if test_cdn.strip() != "":
            test_cdn_url = self.shorten_url(test_cdn, False)
            dialog.append_text(f"\t- 테스트 서버: {test_cdn_url}")
            self.test_qrcode_dialog.show()
        dialog.append_text("\n\n")
        if patch_note.strip() != "":
            dialog.append_text("■ 적용사항")
            dialog.append_text(patch_note)
            dialog.append_text("\n\n")
        if note.strip() != "":
            dialog.append_text("■ 참고사항")
            dialog.append_text(note)
            dialog.append_text("\n\n")
        dialog.append_text("감사합니다.")
        dialog.append_text("손찬우 드림")

    def shorten_url(self, url, is_live: bool):
        shorten_url = self.bitly_api.shorten_url(url)
        if not shorten_url:
            return url

        self.qrcodeAPI.create_qrcode(
            url,
            "qrcode_live.png" if is_live else "qrcode_test.png",
            self.updateQRImage,
        )
        return shorten_url

    def updateQRImage(self):
        self.live_qrcode_dialog.updateImage()
        self.test_qrcode_dialog.updateImage()

    @property
    def qrcodeAPI(self):
        if self._qrcodeAPI is None:
            self._qrcodeAPI = QRCodeAPI()
        return self._qrcodeAPI


class QRCodeDialog(QWidget):
    def __init__(self, title, fileName):
        super().__init__()
        self.qPixmapVar = QPixmap()
        self.fileName = fileName
        self.image_label = QLabel()
        self.image_label.setPixmap(self.qPixmapVar)
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        self.setLayout(vbox)

        self.setWindowTitle(title)
        self.show()

    def updateImage(self):
        self.qPixmapVar.load(self.fileName)
        self.image_label.setPixmap(self.qPixmapVar)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()

        self.tb = QTextBrowser()
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton("Clear")
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle("QTextBrowser")
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def set_title(self, title):
        self.le.setText(title)

    def append_text(self, text):
        self.tb.append(text)

    def clear_text(self):
        self.tb.clear()
