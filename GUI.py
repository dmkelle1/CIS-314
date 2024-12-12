import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout # type: ignore

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Homework")
        self.resize(250, 100)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Type Hello")
        layout.addWidget(self.input)

        submit_button = QPushButton("Done")
        submit_button.clicked.connect(self.submit_text)
        layout.addWidget(submit_button)

    def submit_text(self):
        text = self.input.text()
        print(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())