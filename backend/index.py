import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView

import packages.custom_types as ct

def run() -> None:
    
    str_html_path = "Templates/index.html"
    html_path = ct.Path(str_html_path, check_exists=True)



    # start the window
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setWindowTitle("ElemPy")
    window.setGeometry(0, 0, 800, 600)
    # load the html file
    view = QWebEngineView()

    view.load(QUrl.fromLocalFile(html_path.get_abs_path()))

    window.setCentralWidget(view)
    window.show()
    sys.exit(app.exec_())
