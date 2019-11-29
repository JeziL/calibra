import sys
from calibra_ui import CalibraForm
from fbs_runtime.application_context.PyQt5 import ApplicationContext


class AppContext(ApplicationContext):
    def run(self):
        window = CalibraForm(self)
        window.setWindowTitle("转台校准")
        window.resize(750, 480)
        window.show()
        return self.app.exec_()


if __name__ == "__main__":
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
