import configparser, csv
import asyncio
import random
from pyrogram import Client

async def add_contacts(account):
    api_id, api_hash = await getVoip(account=account)
    app = Client(account, api_hash=api_hash, api_id=api_id)
    await app.start()
    my_contacts = await app.get_contacts()
    added_accounts = 0
    with open('contact/contacts.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row[0].strip()
            if username == 'username':
                continue
            already_contact = any(c.username == username for c in my_contacts)
            if already_contact:
                print(f"@{username} already in contacts.")
                continue
            if added_accounts >= 10:
                print("Reached account limit")
                break
            
            try:
                await app.add_contact(username, first_name=username)
                print(f"Successfully added @{username}")
                added_accounts += 1
            except Exception as e:
                print(f"Failed to add @{username}: {e}")

            seconds = random.randint(10, 35)
            print(f"Waiting {seconds} seconds...")
            await asyncio.sleep(seconds)

    await app.stop()  

async def getVoip(account):
    acc = configparser.ConfigParser()
    acc.read('data/accounts.data', encoding='UTF-8')
    
    for section in acc.sections():
        if acc.has_option(section, 'username'):
            if acc[section]['username'] == account:
                api_id = acc[section]['api_id']
                api_hash = acc[section]['api_hash']
                return (api_id, api_hash)
    
    raise ValueError(f"Account {account} not found in config file")

asyncio.run(add_contacts("gentle_sunrise_72"))