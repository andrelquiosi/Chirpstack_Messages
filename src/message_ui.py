from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
)
from src.send_message import send_message_chirpstack


class ChirpstackMessageSender(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.message_label = QLabel("Message:")
        self.message_input = QLineEdit()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        self.port_label = QLabel("Port:")
        self.port_input = QLineEdit()
        layout.addWidget(self.port_label)
        layout.addWidget(self.port_input)

        self.devices_label = QLabel("Device EUIs (comma-separated):")
        self.devices_input = QLineEdit()
        layout.addWidget(self.devices_label)
        layout.addWidget(self.devices_input)

        self.send_button = QPushButton("Send Message")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        self.setWindowTitle("Chirpstack Message Sender")
        self.setGeometry(300, 300, 400, 400)

    def send_message(self):
        self.result_text.setText(
            "\n".join(
                send_message_chirpstack(
                    self.email_input,
                    self.password_input,
                    self.message_input,
                    self.port_input,
                    self.devices_input,
                )
            )
        )
