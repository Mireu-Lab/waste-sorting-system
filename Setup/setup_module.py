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
    device_info_json = json.load(open("Data/Set.json", "r"))

    save_json = open("Data/Set.json", "a")

    if requests.get("http://ip.jsontest.com").json()["ip"] != device_info_json["device"]["ip"]:
        device_info_json["device"]["ip"] = requests.get("http://ip.jsontest.com").json()["ip"]
    
    if token != None:
        device_info_json["device"]["token"] = token
    
    if service_version != None:
        device_info_json["version"]["service"] = ai_version

    if ai_version != None:
        device_info_json["version"]["ai"] = ai_version

    json.dump(device_info_json, save_json, indent=4)
    return "System Info Update processing complete"