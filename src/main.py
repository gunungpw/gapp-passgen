import sys
import random
import string
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QSlider,
    QCheckBox,
    QLabel,
)
from PySide6.QtCore import QTimer
from PySide6.QtCore import Qt


class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("gapp-password-generator")
        self.setGeometry(100, 100, 400, 300)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Password length slider
        self.length_label = QLabel("Password Length: 12")
        self.length_slider = QSlider(Qt.Orientation.Horizontal)
        self.length_slider.TickPosition(QSlider.TickPosition.TicksBelow)
        self.length_slider.setMinimum(6)
        self.length_slider.setMaximum(50)
        self.length_slider.setValue(12)
        self.length_slider.valueChanged.connect(self.update_length_label)
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_slider)

        # Character type checkboxes
        self.uppercase_cb = QCheckBox("Include Uppercase Letters (A-Z)")
        self.lowercase_cb = QCheckBox("Include Lowercase Letters (a-z)")
        self.numbers_cb = QCheckBox("Include Numbers (0-9)")
        self.symbols_cb = QCheckBox("Include Symbols (!@#$%)")
        self.uppercase_cb.setChecked(True)
        self.lowercase_cb.setChecked(True)
        layout.addWidget(self.uppercase_cb)
        layout.addWidget(self.lowercase_cb)
        layout.addWidget(self.numbers_cb)
        layout.addWidget(self.symbols_cb)

        # Password display
        self.password_display = QLineEdit()
        self.password_display.setReadOnly(True)
        self.password_display.setPlaceholderText("Generated password will appear here")
        layout.addWidget(self.password_display)

        # Buttons
        button_layout = QHBoxLayout()
        self.generate_button = QPushButton("Generate Password")
        self.copy_button = QPushButton("Copy to Clipboard")
        self.generate_button.clicked.connect(self.generate_password)
        self.copy_button.clicked.connect(self.copy_password)
        button_layout.addWidget(self.generate_button)
        button_layout.addWidget(self.copy_button)
        layout.addLayout(button_layout)

        # Styling
        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0f0; }
            QLabel { font-size: 14px; }
            QLineEdit { padding: 8px; font-size: 14px; }
            QPushButton {
                padding: 8px;
                font-size: 14px;
                background-color: #4CAF50;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover { background-color: #45a049; }
            QCheckBox { font-size: 14px; }
            QSlider { margin: 10px 0; }
        """)

    def update_length_label(self):
        self.length_label.setText(f"Password Length: {self.length_slider.value()}")

    def generate_password(self):
        length = self.length_slider.value()
        use_uppercase = self.uppercase_cb.isChecked()
        use_lowercase = self.lowercase_cb.isChecked()
        use_numbers = self.numbers_cb.isChecked()
        use_symbols = self.symbols_cb.isChecked()

        # Check if at least one character type is selected
        if not (use_uppercase or use_lowercase or use_numbers or use_symbols):
            self.password_display.setText("Select at least one character type!")
            return

        # Define character sets
        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        # Generate password
        password = "".join(random.choice(characters) for _ in range(length))
        self.password_display.setText(password)

    def copy_password(self):
        password = self.password_display.text()
        if password and "Select" not in password:  # Avoid copying error message
            clipboard = QApplication.clipboard()
            clipboard.setText(password)
            self.copy_button.setText("Copied!")
            self.copy_button.setStyleSheet("background-color: #2196F3; color: white;")
            # Reset button text and style after 1 second
            QTimer.singleShot(1000, lambda: self.copy_button.setText("Copy to Clipboard"))
            QTimer.singleShot(
                1000,
                lambda: self.copy_button.setStyleSheet("background-color: #4CAF50; color: white;"),
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
