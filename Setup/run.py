from token_module import token_setup, token_update
from ai_module import ai_update, ai_setup
from setup_module import system_setup

from datetime import datetime

print(f"[{datetime.now()}] = Setup Start Processing")
print(f"[{datetime.now()}] = {system_setup()}")
print(f"[{datetime.now()}] = {token_setup()}")
print(f"[{datetime.now()}] = {ai_setup()}")
print(f"[{datetime.now()}] = Setup Processing done\n\n")