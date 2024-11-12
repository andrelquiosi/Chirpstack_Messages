import requests
from src.message_prepare import message_mount
from src.login_chirpstack import ChirpstackLogin as Login


def send_message_chirpstack(email_input,password_input, message_input, port_input, devices_input):
    user = email_input.text()
    password = password_input.text()
    login = Login(user, password)
    token = login.login()
    port = int(port_input.text())


    message = message_input.text()
    devices = devices_input.text().split(",")

    results = []
    for device in devices:
        headers, url, data = message_mount(device.strip(), message, token, port)
        try:
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                results.append(
                        f"Request successful for device {device}: {response.json()}"
                    )
            else:
                results.append(
                        f"Request failed for device {device}: {response.status_code} {response.text}"
                    )
        except requests.exceptions.RequestException as e:
            results.append(f"Request failed for device {device}: {e}")
    return results