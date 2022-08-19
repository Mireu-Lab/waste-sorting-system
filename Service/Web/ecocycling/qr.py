from datetime import datetime
from pytz import timezone

import qrcode
import json

device_info = open("Data/Set.json", "r")
token = json.load(device_info)["token"]

qr = qrcode.QRCode(
    version=4,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=20,
    border=1
)

def add():    
    qr.add_data(token)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(f"App/static/main.png")
    
    print("QR CODR ADD CLRAR")