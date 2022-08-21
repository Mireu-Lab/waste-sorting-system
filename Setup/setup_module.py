import requests
import json

def system_setup():
    device_info = open("Data/Set.json", "w")
    setup_json = {
        "device" : {
            "id" : 1,
            "ip" : requests.get("http://ip.jsontest.com").json()["ip"],
            "token" : None,
        },

        "version" : {
            "service" : "0.0.1",
            "ai" : None,
        },
    }
    json.dump(setup_json, device_info, indent=4)
    return "Complete instrument basic setup"

def system_info_update(token=None, service_version=None, ai_version=None):
    device_info = open("Data/Set.json", "a")

    if requests.get("http://ip.jsontest.com").json()["ip"] != device_info["device"]["ip"]:
        device_info["device"]["ip"] = requests.get("http://ip.jsontest.com").json()["ip"]
    
    if token != None:
        device_info["device"]["token"] = token
    
    if service_version != None:
        device_info["version"]["service"] = ai_version

    if ai_version != None:
        device_info["version"]["ai"] = ai_version

    json.dump(device_info, device_info)