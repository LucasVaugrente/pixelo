from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QMouseEvent
from PyQt6.QtCore import Qt

class PixelCanvas(QWidget):
    def __init__(self, rows, cols, pixel_size):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.pixel_size = pixel_size
        self.grid = [[QColor(255, 255, 255, 127) for _ in range(cols)] for _ in range(rows)]

        self.selected_color = QColor(0, 0, 0)
        self.drawing = False

        self.setFixedSize(cols * pixel_size, rows * pixel_size)

    def paintEvent(self, event):
        painter = QPainter(self)
        for row in range(self.rows):
            for col in range(self.cols):
                painter.setBrush(self.grid[row][col])
                painter.drawRect(col * self.pixel_size, row * self.pixel_size, self.pixel_size, self.pixel_size)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            self.paint_pixel(event.position().x(), event.position().y())

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.paint_pixel(event.position().x(), event.position().y())

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False

    def paint_pixel(self, x, y):
        col, row = x // self.pixel_size, y // self.pixel_size
        if 0 <= col < self.cols and 0 <= row < self.rows:
            self.grid[int(row)][int(col)] = self.selected_color
            self.update()

    def set_color(self, color):
        self.selected_color = QColor(color)