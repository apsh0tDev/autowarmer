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
                seconds = random.uniform(25, 45)
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


async def main():
    #await join_groups("sessions/radiant_glimmer3")
    await interactions("sessions/radiant_glimmer3")

if __name__ == "__main__":
    asyncio.run(main())
