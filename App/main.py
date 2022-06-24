from ecocycling import qr

from flask import Flask, request, render_template, url_for, redirect, jsonify
app = Flask(__name__)

import json

with open("Data/Set.json", "r") as setdata:
    set_data = json.load(setdata)

deviceid = set_data["device"]["id"]
devicelocal = set_data["device"]["local"]

@app.route('/', methods=["GET"])
def qr_web():
    if request.method == "GET":
        if request.remote_addr == '127.0.0.1':
            return render_template('main.html')
        else:
            return redirect('http://hana.mireu.xyz')

@app.route('/singin', methods=["POST", "GET"])
def singin():
    if request.method == "POST":
        input_data = request.get_json()
        print(input_data["userid"], input_data["username"], input_data["userimage"])
        return input_data["username"], input_data["userimage"]
    else:
        return redirect('http://hana.mireu.xyz')



if __name__ == '__main__':
    qr.add()
    app.run(host="0.0.0.0", port="80", debug=True)