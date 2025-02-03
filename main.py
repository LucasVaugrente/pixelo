import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from canvas import PixelCanvas
from ui import ColorPalette

class PixelArtApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pixelo")
        self.setGeometry(100, 100, 500, 500)

        # Conteneur principal
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Ajout du canevas
        self.canvas = PixelCanvas(16, 16, 20)  # Grille 16x16, pixels de 20px
        layout.addWidget(self.canvas)

        self.palette = ColorPalette(self.canvas)
        layout.addLayout(self.palette)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PixelArtApp()
    window.show()
    sys.exit(app.exec())
