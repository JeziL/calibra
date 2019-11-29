import sys
from PyQt5.QtWidgets import QApplication
from calibra_ui import CalibraForm


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalibraForm()
    window.setWindowTitle("转台校准")
    window.resize(750, 480)
    window.show()
    sys.exit(app.exec_())
