from token_module import token_setup, token_update
from ai_module import ai_update, ai_setup
from setup_module import system_setup

import schedule
import requests

from datetime import datetime
import time
import os

def service_error():
    requests.get('http://localhost:18099/error/503')

def service_run():
    requests.get('http://localhost:18099/error/200')

print(f"[{datetime.now()}] = Setup Program\n\n")
   
async def ai_updates():
    print(f"[{datetime.now()}] = Regular AI Updates Processing done / {ai_update()}")

# AI 머신러닝 모델 업데이트 스케줄
schedule.every(1).day.at("04:10").do(ai_updates)

async def token_updates():
    print(f"[{datetime.now()}] = Regular Token Updates Processing done / {token_update()}")

def service_restart():
    os.system("sudo systemctl restart serviceAPI_service")
    os.system("sudo systemctl restart FrontWeb_service")

# 정기 점검 스케줄
schedule.every().day.at("04:10").do(service_error)
schedule.every().day.at("04:15").do(token_updates)
schedule.every().day.at("04:30").do(service_restart)
schedule.every().day.at("04:30").do(service_run)

while True:
    schedule.run_pending()
    time.sleep(1)