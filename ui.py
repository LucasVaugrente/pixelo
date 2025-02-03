from PyQt5.QtWidgets import QPushButton, QHBoxLayout, QColorDialog

class ColorPalette(QHBoxLayout):
    def __init__(self, canvas):
        super().__init__()
        self.canvas = canvas
        self.colors = ["#000000", "#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff", "#ffffff"]

        for color in self.colors:
            btn = QPushButton()
            btn.setStyleSheet(f"background-color: {color};")
            btn.setFixedSize(30, 30)
            btn.clicked.connect(lambda checked, c=color: self.canvas.set_color(c))
            self.addWidget(btn)

        # Bouton pour choisir une couleur personnalisée
        color_picker = QPushButton("🎨")
        color_picker.setFixedSize(40, 30)
        color_picker.clicked.connect(self.pick_color)
        self.addWidget(color_picker)

    def pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_color(color.name())
