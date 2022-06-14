from datetime import datetime
from pytz import timezone

import qrcode
import hashlib
import json

with open("Data/Set.json", "r") as setdata:
    set_data = json.load(setdata)

device_id = set_data["device"]["id"]
device_zone = set_data["device"]["zone"]
device_local = set_data["device"]["local"]

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=4,
    border=1
)

def add():
    time = datetime.now(timezone(device_zone)).strftime('%Y/%m/%d-%H:%M:%S')
    
    qr.add_data({"device_id" : device_id})
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")
    qr_img.save(f"App/static/{device_id}-{device_local}.png")
    
    print(f"QR CODR ADD CLRAR : {time}")