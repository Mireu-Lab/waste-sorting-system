import requests
import json

def system_setup():
    device_info = open("Data/Set.json", "w")
    setup_json = {
        "device" : {
            "id" : 1,
            "ip" : requests.get("http://ip.jsontest.com").json()["ip"],
            "token" : None,
            "version" : None
        },

        "ai" : {
            "version" : None
        }
    }
    json.dump(setup_json, device_info, indent=4)
    return "Complete instrument basic setup"

def system_info_update(token=None, ai_version=None):
    device_info = open("Data/Set.json", "a")

    if requests.get("http://ip.jsontest.com").json()["ip"] != device_info["device"]["ip"]:
        device_info["device"]["ip"] = requests.get("http://ip.jsontest.com").json()["ip"]
    
    device_info["device"]["token"] = token
    device_info["device"]["version"] = None
    device_info["ai"]["version"] = ai_version

    json.dump(device_info, device_info)