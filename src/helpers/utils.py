# help you to read the JSON file and provide you the JSON data.

import json

def def_payload_auth():
    # To read the auth.json file data and return
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_header():
    headers = {
        "Content-Type": "application/json"
    }