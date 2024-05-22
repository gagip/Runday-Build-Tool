import os.path
import sys

import PyQt5.QtWidgets
from dotenv import load_dotenv

from src.gui_manager import GUIManager
from src.qr_manger import BitlyAPI

if __name__ == "__main__":
    if os.path.isfile("qrcode_live.png"):
        os.remove("qrcode_live.png")
    if os.path.isfile("qrcode_test.png"):
        os.remove("qrcode_test.png")

    load_dotenv()

    bitly_api_token = os.getenv("BITLY_API_TOKEN")
    if not bitly_api_token:
        raise ValueError("BITLY_API_TOKEN 환경변수가 설정되어 있지 않습니다.")

    bilty_api = BitlyAPI(bitly_api_token)
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = GUIManager(bilty_api)
    sys.exit(app.exec_())
