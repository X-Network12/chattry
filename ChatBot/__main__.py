import os
import importlib
import subprocess

from pyrogram import idle

from ChatBot.modules import ALL_MODULES
from config import WEB_APP  

async def boot():
    await app.start()

    for module in ALL_MODULES:
        importlib.import_module(f"ChatBot.modules.{module}")

    if WEB_APP:
        subprocess.Popen(['python3', 'app.py'])

    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(boot())