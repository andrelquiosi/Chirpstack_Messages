from src.message_ui import ChirpstackMessageSender
import sys
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    sender = ChirpstackMessageSender()
    sender.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
