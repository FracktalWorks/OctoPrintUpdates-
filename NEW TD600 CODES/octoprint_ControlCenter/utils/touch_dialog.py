from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class TouchDialog(QWidget):
    def __init__(self, parent, text, on_close=None):
        super().__init__(parent)
        self.on_close = on_close
        self.setGeometry(0, 0, parent.width(), parent.height())
        self.setStyleSheet("background-color: rgba(0,0,0,180);")

        # Center box
        box = QWidget(self)
        box.setFixedSize(400, 250)
        box.move((self.width() - 400) // 2, (self.height() - 250) // 2)
        box.setStyleSheet("background-color: #282828; border-radius: 10px;")

        layout = QVBoxLayout(box)
        layout.setContentsMargins(20, 20, 20, 20)

        # Message
        label = QLabel(text)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Gotham", 12))
        label.setStyleSheet("color: white; background: transparent;")
        layout.addWidget(label)

        # OK Button
        btn = QPushButton("OK")
        btn.setFixedHeight(60)
        btn.setFont(QFont("Gotham", 14))
        btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 8px;
            }
        """)
        btn.clicked.connect(self.close_dialog)
        layout.addWidget(btn)

        self.show()
        self.raise_()

    def close_dialog(self):
        if self.on_close:
            self.on_close()
        self.hide()
        self.deleteLater()


def WarningOk(parent, text, **kwargs):
    dialog = TouchDialog(parent, text)
    return dialog
