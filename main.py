import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout
from canvas import PixelCanvas
from ui import ColorPalette

class PixelArtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixelo")
        self.showMaximized()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.canvas = PixelCanvas(32, 32, 20)
        layout.addWidget(self.canvas)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.canvas.clear_canvas)

        button_layout = QHBoxLayout()
        button_layout.addWidget(clear_button)

        self.palette = ColorPalette(self.canvas)
        # layout.addLayout(self.palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixelArtApp()
    window.show()
    sys.exit(app.exec())
