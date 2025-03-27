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
        await account.start()
        acc = await account.get_me()
        await addAccountToList(API_ID=api_id, API_HASH=api_hash, account=acc)

    except Exception as e:
        print(f"Login failed: {e}")

async def addAccountToList(API_ID, API_HASH, account):

    try:
        voiplen = 0
        voiplen = await readVoips()
        config = configparser.ConfigParser()
        config['credential'+str(voiplen+1)] = {
            'username' : account.username,
            'name' : str(account.first_name) + str(account.last_name),
            'id' : account.id,
            'api_id' : API_ID,
            'api_hash' : API_HASH,
            'restricted' : account.is_restricted,
            'in_usage' : True   
        }
        if voiplen == 0:
            method = 'w'
        else:
            method = 'a'
        with open('data/accounts.data', method, encoding='UTF-8') as accountsfile:
            config.write(accountsfile)
            print(f"Account successfully logged as: {account.username}")
    except Exception as e:
        print(f"Account config failed: {e}")
        
async def readVoips():
    config = configparser.ConfigParser()
    config.read('data/accounts.data', encoding='UTF-8')
    return len(config.sections())

asyncio.run(login())