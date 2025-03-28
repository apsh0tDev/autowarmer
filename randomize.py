import asyncio
import random
from pyrogram import Client
from group import join_a_random_group
from conversation import convo
from datetime import datetime, timedelta

async def random_actions(account, duration_minutes=30):
    """Randomly perform actions for a specified duration"""
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    actions = [join_a_random_group, random_chat]
    
    print(f"Starting random actions for {duration_minutes} minutes...")
    
    while datetime.now() < end_time:
        try:
            # Randomly select an action
            action = random.choice(actions)
            
            # Execute the selected action
            if action == join_a_random_group:
                await join_a_random_group(account)
            else:
                await random_chat(account)
            
            # Random delay between actions (30-120 seconds)
            delay = random.uniform(30, 120)
            print(f"Next action in {delay:.1f} seconds...")
            await asyncio.sleep(delay)
            
        except Exception as e:
            print(f"Action failed: {e}")
            await asyncio.sleep(30)  # Wait before retrying
    
    print("Session completed")


async def random_chat(mainAccount):
    second_account = await random_acc(account=mainAccount)
    async with Client(mainAccount) as x_app, Client(f"sessions/{second_account}") as y_app:
        await convo(x_app, y_app)


async def random_acc(account):
    contacts = [contact.username for contact in await account.get_contacts() if contact.username]
    return(random.choice(contacts))

async def main():
    await random_actions("sessions/gentle_sunrise_72")

if __name__ == "__main__":
    asyncio.run(main())