import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class YouTubeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini YouTube App")
        self.setGeometry(100, 100, 1200, 800)

        layout = QVBoxLayout()

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Buscar en YouTube...")
        self.search_bar.returnPressed.connect(self.buscar)

        self.button = QPushButton("Buscar")
        self.button.clicked.connect(self.buscar)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.youtube.com"))

        layout.addWidget(self.search_bar)
        layout.addWidget(self.button)
        layout.addWidget(self.browser)

        self.setLayout(layout)

    def buscar(self):
        query = self.search_bar.text()
        url = f"https://www.youtube.com/results?search_query={query}"
        self.browser.setUrl(QUrl(url))

app = QApplication(sys.argv)
window = YouTubeApp()
window.show()
sys.exit(app.exec_())