import requests
import json

device_info = open("Data/Set.json", "w")

setup_json = {
    "id" : 1,
    "ip" : requests.get("http://ip.jsontest.com").json()["ip"],
    "token" : None,
    "version" : 1
}

json.dump(setup_json, device_info)