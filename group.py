import asyncio
import random
from pyrogram import Client
from groups.groups import groups
from pyrogram.enums import ChatType

async def join_groups(account):
    async with Client(account) as app:
        try:
            await app.get_me()
            for group in groups:
                seconds = random.uniform(25, 360)
                try:
                    await app.join_chat(str(group))
                except Exception as e:
                    print(e)
                await asyncio.sleep(seconds)
        except Exception as e:
            print(f"Couldn't access account")

async def interactions(account):
    async with Client(account) as app:
        emojis = ['👍','❤️','🔥','🎉','🤩','😁','🥰','🤯','👏']
        group_names = await get_group_ids(app)
        #random_group = random.choice(group_names)
        for group in group_names:
            print(f"Getting chat from {group}")
            chat = await app.get_chat(str(group))
            print(chat.id)
            chat_history = app.get_chat_history(chat.id)
            async for message in chat_history:
                if (not message.service):
                    
                    random_emoji = random.choice(emojis)
                    seconds = random.uniform(5, 15)
                    
                    try:
                        await app.send_reaction(
                            chat_id=chat.id,
                            message_id=message.id,
                            emoji=random_emoji
                        )
                        await asyncio.sleep(seconds)
                    except Exception as e:
                        print(f"Couldn't react to message {message.id}: {e}")
            await asyncio.sleep(30)


async def get_group_ids(account):
            groups = []
            async for dialog in account.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    if dialog.chat.title != f"DealArchitects'_Blueprints":
                        groups.append(str(dialog.chat.username))
            return(groups)

async def join_single_group(account, group):
    await account.join_chat(group)

async def get_a_random_group():
    return random.choice(groups)

async def join_a_random_group(account):
    joined_groups = []
    async for dialog in account.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            if dialog.chat.title != "DealArchitects'_Blueprints":
                if dialog.chat.username:
                    joined_groups.append(dialog.chat.username)

    max_attempts = 5
    attempt = 0
    
    while attempt < max_attempts:
        random_group = await get_a_random_group()
        
        if not random_group:
            print("No random group available")
            return False
            
        if random_group not in joined_groups:
            try:
                await join_single_group(account=account, group=random_group)
                print(f"Successfully joined: {random_group}")
                return True
            except Exception as e:
                print(f"Failed to join {random_group}: {e}")
                attempt += 1
                await asyncio.sleep(5)
        else:
            print(f"Already in group: {random_group}")
            attempt += 1
            continue
    
    print(f"Failed to join a new group after {max_attempts} attempts")
    return False

async def main():
    #await join_groups("sessions/radiant_glimmer3")
    await interactions("sessions/radiant_glimmer3")

if __name__ == "__main__":
    asyncio.run(main())
