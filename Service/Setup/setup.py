import Services.App.version as version
import requests
import json

def system_setup():
    device_info = open("Data/Set.json", "w")
    setup_json = {
        "device" : {
            "id" : 1,
            "ip" : requests.get("http://ip.jsontest.com").json()["ip"],
            "token" : None,
            "version" : version.__version__
        }
    }
    json.dump(setup_json, device_info, indent=4)
    return 0

def system_info_update(token=None):
    device_info = open("Data/Set.json", "a")

    device_info["device"]["ip"] = requests.get("http://ip.jsontest.com").json()["ip"]
    device_info["device"]["token"] = token
    device_info["device"]["version"] = version.__version__

    json.dump(device_info, device_info)
    return 0

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
        system_info_update(response["token"])
    else:
        pass

print(version.__version__)

# system_setup()
# token_setup()