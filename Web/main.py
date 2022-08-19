from ecocycling import qr

from flask import Flask, request, render_template, redirect, jsonify
import webbrowser

app = Flask(__name__)

@app.route('/', methods=["GET"])
def qr_web():
    return render_template('login.html')

@app.route('/error', methods=["GET"])
def error_web():
    return render_template('error.html')

@app.route('/userinfo', methods=["GET"])
def signin_web():
    name = request.args.get("username")
    image = request.args.get("userimage")    
    return render_template('userinfo.html', username=name, userimage=image)

if __name__ == '__main__':
    qr.add()
    app.run(host="0.0.0.0", port="80", debug=True)
    webbrowser.open("http://127.0.0.1/")
