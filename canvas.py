from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QMouseEvent
from PyQt5.QtCore import Qt

class PixelCanvas(QWidget):
    def __init__(self, rows, cols, pixel_size):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.pixel_size = pixel_size
        self.grid = [[QColor(255, 255, 255) for _ in range(cols)] for _ in range(rows)]  # Grille blanche

        self.selected_color = QColor(0, 0, 0)  # Noir par défaut
        self.setFixedSize(cols * pixel_size, rows * pixel_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        for row in range(self.rows):
            for col in range(self.cols):
                painter.setBrush(self.grid[row][col])
                painter.drawRect(col * self.pixel_size, row * self.pixel_size, self.pixel_size, self.pixel_size)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            x, y = event.position().x() // self.pixel_size, event.position().y() // self.pixel_size
            if 0 <= x < self.cols and 0 <= y < self.rows:
                self.grid[y][x] = self.selected_color
                self.update()  # Redessine la grille

    def set_color(self, color):
        self.selected_color = QColor(color)
