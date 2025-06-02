import sys
import random
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QTimer

class MouseTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Week 3 - (Abdul Aqil Murtadho - F1D022029)")
        self.setGeometry(100, 100, 700, 500)

        self.label = QLabel("x: 0, y: 0", self)
        self.label.setStyleSheet("font-size: 20px;")
        self.label.adjustSize()
        self.label.move(50, 50)

        self.setMouseTracking(True)
        self.label.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()
        self.label.setText(f"x: {x}, y: {y}")
        self.label.adjustSize()

        if self.label.geometry().contains(event.pos()):
            self.move_label()

    def move_label(self):
        max_x = self.width() - self.label.width()
        max_y = self.height() - self.label.height()
        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)
        self.label.move(new_x, new_y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MouseTracker()
    window.show()
    sys.exit(app.exec_())
