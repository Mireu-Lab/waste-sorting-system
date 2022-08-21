import setup_module as setup_module
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

    response = requests.post('http://api.ecocycling.none-labs.xyz/iot/registration', headers=headers, json=json_data).json()
    
    if response["Code"] == 200:
        setup_module.system_info_update(response["token"])
        return "Token Creation processing complete"
    else:
        return "Token Creation processing failed"

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

    response = requests.post(f'http://api.ecocycling.none-labs.xyz/iot/update/{info["device"]["token"]}', headers=headers, json=json_data).json()
    
    if response["Code"] == 200:
        setup_module.system_info_update(response["token"])
        return "Token Creation processing complete"
    else:
        return "Token Creation processing failed"