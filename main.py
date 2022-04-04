import sys

import PyQt5.QtWidgets

from GUIManager import GUIManager


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    ex = GUIManager()
    sys.exit(app.exec_())
