from datetime import datetime
from pytz import timezone

import qrcode
import requests

device_ip = requests.get("http://ip.jsontest.com").json()["ip"]

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=20,
    border=1
)

def add():    
    qr.add_data([device_ip])
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(f"App/static/main.png")
    
    print("QR CODR ADD CLRAR")