import random
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QApplication


class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.hello = ["Hallo Welt", "你好，世界",
                      "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QPushButton("Click me!")
        self.text = QLabel("Hello World")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))
        # self.repaint()  # macOS fix


if __name__ == "__main__":
    app = QApplication([])

    widget = MyWidget()
    widget.show()

    sys.exit(app.exec_())
