from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QMouseEvent, QResizeEvent, QWheelEvent
from PyQt6.QtCore import Qt

class PixelCanvas(QWidget):
    def __init__(self, rows, cols, pixel_size):
        super().__init__()
        self.rows = rows
        self.cols = cols

        self.pixel_size = pixel_size
        self.min_pixel_size = 5
        self.max_pixel_size = 100

        self.grid = [[QColor(255, 255, 255, 255) for _ in range(cols)] for _ in range(rows)]

        self.selected_color = QColor(0, 0, 0)
        self.drawing = False

        self.show_grid = True

        self.offset_x = 0
        self.offset_y = 0

    def paintEvent(self, event):
        painter = QPainter(self)
        self.update_offsets()

        for row in range(self.rows):
            for col in range(self.cols):
                painter.setBrush(self.grid[row][col])
                x = self.offset_x + col * self.pixel_size
                y = self.offset_y + row * self.pixel_size
                painter.fillRect(x, y, self.pixel_size, self.pixel_size, self.grid[row][col])

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

    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        if delta > 0:
            self.pixel_size = min(self.pixel_size + 2, self.max_pixel_size)  # Zoom in
        else:
            self.pixel_size = max(self.pixel_size - 2, self.min_pixel_size)  # Zoom out

        self.update()  # Redessiner après le zoom

    def paint_pixel(self, x, y):
        col = (x - self.offset_x) // self.pixel_size
        row = (y - self.offset_y) // self.pixel_size

        if 0 <= col < self.cols and 0 <= row < self.rows:
            self.grid[int(row)][int(col)] = self.selected_color
            self.update()

    def set_color(self, color):
        self.selected_color = QColor(color)

    def update_offsets(self):
        canvas_width = self.cols * self.pixel_size
        canvas_height = self.rows * self.pixel_size

        self.offset_x = (self.width() - canvas_width) // 2
        self.offset_y = (self.height() - canvas_height) // 2

    def resizeEvent(self, event: QResizeEvent):
        self.update()

    def clear_canvas(self):
        self.grid = [[QColor(255, 255, 255, 255) for _ in range(self.cols)] for _ in range(self.rows)]
        self.update()
