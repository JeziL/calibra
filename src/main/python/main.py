import sys
from calibra_ui import CalibraForm
from fbs_runtime.application_context.PyQt5 import ApplicationContext


if __name__ == "__main__":
    appctxt = ApplicationContext()
    window = CalibraForm()
    window.setWindowTitle("转台校准")
    window.resize(750, 480)
    window.show()
    exit_code = appctxt.app.exec_()
    sys.exit(exit_code)
