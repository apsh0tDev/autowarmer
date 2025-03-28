import asyncio
import random
from pyrogram import Client
from convo.convos import chat_conversations

async def convo(accountOne, accountTwo):
    
        try:
            x, y = await asyncio.gather(
                accountOne.get_me(),
                accountTwo.get_me()
            )
            print(f"Both accounts connected successfully!")
            #get the random conversation from chat_conversations dict
            random_convo = await get_random_convo()
            for message in random_convo['messages']:
                if message['user'] == 'X':
                    send_reaction = random.choice([True, False])
                    if send_reaction:
                        await rand_reaction(accountOne, y.username)
                    await accountOne.send_message(y.username, message['message'])
                elif message['user'] == 'Y':
                    send_reaction = random.choice([True, False])
                    if send_reaction:
                        await rand_reaction(accountTwo, x.username)
                    await accountTwo.send_message(x.username, message['message'])

                seconds = random.randrange(4,35)
                await asyncio.sleep(seconds)

        except Exception as e:
            print(f"Error connecting accounts: {e}")
    
async def get_random_convo():
    i = random.randrange(-1, len(chat_conversations))
    return chat_conversations[i]

async def rand_reaction(sender, receiver):
    emojis = ['👍','👎','❤️','🔥','🎉','🤩','😱','😁','😢','🥰','🤯','🤔','👏']
    try:
        chat = await sender.get_chat(receiver)
        ids = []
        
        # Properly handle async generator
        async for message in sender.get_chat_history(chat.id, limit=20):  # Added limit
            if message.from_user and not message.from_user.is_self:
                ids.append(message.id)
        
        if ids:  # Only react if we found messages
            rand_msg = random.choice(ids)
            rand_emoji = random.choice(emojis)
            await sender.send_reaction(chat.id, rand_msg, rand_emoji)
            
    except Exception as e:
        print(f"Error sending reaction: {e}")

async def main():
    await convo("sessions/radiant_glimmer3", "sessions/gentle_sunrise_72")
    #await get_random_convo()

if __name__ == "__main__":
    asyncio.run(main())
