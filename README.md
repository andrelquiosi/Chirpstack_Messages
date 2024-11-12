## Chirpstack Message Sender

This project provides a simple GUI application for sending messages to devices on a Chirpstack network.

![Chirpstack Message Sender](/docs/clear_ui.png "Chirpstack Message Sender")

### Features

* **Login to Chirpstack:** Authenticates with your Chirpstack account using email and password.
* **Message Sending:** Allows you to send messages to multiple devices simultaneously.
* **Port Selection:** Specify the desired port for sending messages.
* **Device EUIs:** Enter a comma-separated list of device EUIs to target.
* **Result Display:** Shows the status of each message sent, including success or failure messages.

### Requirements

* Python 3.12
* PyQt5 (version 5.15.11 or later)
* requests library

Install the required packages using:

```bash
pip install -r requirements.txt
```

### Setup

**Environment Variables:**

* Create a `.env` file in the project root directory.
* Set the `URL` environment variable to the base URL of your Chirpstack instance.

    Example: `.env`
```
URL = http://localhost:8080
```

**Run the Application:**

Execute the `main.py` file:

```bash
python main.py
```

### Usage

1. **Login:** Enter your Chirpstack email and password in the respective fields.
2. **Message:** Type the message you want to send.
3. **Port:** Enter the desired port number.
4. **Device EUIs:** Enter a comma-separated list of device EUIs.
    * Exemple: 000000000, 000000001, 000000002, 000000003
5. **Send Message:** Click the "Send Message" button.
6. **Results:** The results of each message sent will be displayed in the text area below.

![Use Example](/docs/example_usage.png "Use Example")

### Code Structure

* `login_chirpstack.py`: Handles authentication with Chirpstack and retrieves the JWT token.
* `message_ui.py`: Creates the GUI interface for the application.
* `message_prepare.py`: Prepares the message data and headers for sending.
* `send_message.py`: Sends the message to the specified devices using the Chirpstack API.
* `main.py`: Starts the application.

### Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

### License

This project is licensed under the MIT License.

### Future work

Change the code to Build a Desktop Application
