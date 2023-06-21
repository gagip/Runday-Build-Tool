import sys
import os.path

import PyQt5.QtWidgets

from gui_manager import GUIManager


if __name__ == '__main__':
    if os.path.isfile('qrcode_live.png'):
        os.remove('qrcode_live.png')
    if os.path.isfile('qrcode_test.png'):
        os.remove('qrcode_test.png')

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = GUIManager()
    sys.exit(app.exec_())
