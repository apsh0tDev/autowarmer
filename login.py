import os, configparser
import asyncio
from pyrogram import Client

async def login():
    account_name = input("Enter the name of the account: ")
    api_id = input("Enter your API_ID: ")
    api_hash = input("Enter your API_HASH: ")

    sessions_dir = "sessions"
    os.makedirs(sessions_dir, exist_ok=True)

    account = Client(
        name=os.path.join(sessions_dir, account_name),
        api_id=api_id,
        api_hash=api_hash
    )

    try:
        account.start()
        acc = account.get_me()
        print(f"Successfully logged in as {acc.first_name}")

    except Exception as e:
        print(f"Login failed: {e}")

def addAccountToList():
    cpass = configparser.RawConfigParser()
    cpass.read('data/accounts.data', encoding="UTF-8")
    



asyncio.run(login())