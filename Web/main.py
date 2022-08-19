from ecocycling import qr

from flask import Flask, request, render_template, redirect, jsonify

app = Flask(__name__)

@app.route('/', methods=["GET"])
def qr_web():
    return render_template('login.html')

@app.route('/userinfo', methods=["GET"])
def signin_web():
    name = request.args.get("username")
    image = request.args.get("userimage")    
    return render_template('userinfo.html', username=name, userimage=image)

if __name__ == '__main__':
    qr.add()
    app.run(host="0.0.0.0", port="80", debug=True)
