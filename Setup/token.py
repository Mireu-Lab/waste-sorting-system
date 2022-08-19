import setup
import requests
import json

def token_setup():
    device_info = open("Data/Set.json", "r")
    info = json.load(device_info)

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'device_id': info["device"]["id"],
        'ip': info["device"]["ip"],
        'version': info["device"]["version"],
    }

    response = requests.post('http://127.0.0.1:8080/iot/registration', headers=headers, json=json_data).json()
    
    if response["Code"] == 200:
        setup.system_info_update(response["token"])
    else:
        pass

def token_update():
    device_info = open("Data/Set.json", "r")
    info = json.load(device_info)

    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'device_id': info["device"]["id"],
        'ip': info["device"]["ip"],
        'version': info["device"]["version"],
    }

    response = requests.post(f'http://127.0.0.1:8080/iot/update/{info["device"]["token"]}', headers=headers, json=json_data).json()
    
    if response["Code"] == 200:
        setup.system_info_update(response["token"])
    else:
        pass