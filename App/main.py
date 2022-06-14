from ecocycling import qr

from flask import Flask
from flask import render_template

app = Flask(__name__)

import json

with open("Data/Set.json", "r") as setdata:
    set_data = json.load(setdata)

deviceid = set_data["device"]["id"]
devicelocal = set_data["device"]["local"]

@app.route('/')
def qr_web():
    return render_template(
        'main.html', 
        image_file=f"{deviceid}-{devicelocal}.png"
    )

if __name__ == '__main__':
    qr.add()
    app.run(host="0.0.0.0", port="80", debug=True)