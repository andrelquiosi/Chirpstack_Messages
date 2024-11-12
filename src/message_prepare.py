import os
import base64
def message_mount(devices, message, token, port: int):
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Grpc-Metadata-Authorization": f"Bearer {token}",
    }

    url = f"{os.getenv('URL')}/api/devices/{devices}/queue"
    data = {
        "deviceQueueItem": {
            "data": f"{encode_message_data_base64(message)}",
            "devEUI": f"{devices}",
            "fPort": port,
        }
    }

    return headers, url, data

def encode_message_data_base64(message):
    encoded_message = base64.b64encode(message.encode()).decode()
    return encoded_message
