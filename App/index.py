from flask import Flask, request, render_template, redirect, jsonify
from flask_cors import CORS

from time import sleep

api = Flask(__name__)
CORS(api)

userid = None
username = None
userimage = None

@api.route("/")
def main_web():
    return redirect("http://www.mireu.xyz")

@api.route("/signin/input", methods=["POST    global userid, username, userimage"])
def signin_input():
    global userid, username, userimage
    input_data = request.get_json()
    userid = input_data["userid"]
    username = input_data["username"]
    userimage = input_data["userimage"]
    # return {"USERNAME" : username, "MESSAGE" : "CLEAR"}
    print({"USERNAME" : username, "MESSAGE" : "CLEAR"})
    return {"USERNAME" : username, "MESSAGE" : "CLEAR"}

@api.route("/signin/upload", methods=["GET"])
def signin_upload():
    global userid, username, userimage
    return jsonify([username, userimage])

if __name__ == '__main__':
    api.run(host="0.0.0.0", port="18099", debug=True)
