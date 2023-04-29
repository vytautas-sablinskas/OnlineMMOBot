import discord
import sys
import time
from Handlers.FileHandler import FileHandler
from Constants.FilePaths import FilePaths
from Managers.Files.FileManager import FileManager

last_message_time = 0
cooldown_time = 5

def get_response(message: str):
    user_message = message.lower()

    if user_message == 'help':
        return "!continue - Continues bot from pause\n!action - Shows current bot action and start time"

    if user_message == 'continue':
        FileManager.update_bot_status(status_text="continue")
        return "Script was unpaused! Make sure to have verified AFK check"

    if user_message == 'action':
        current_action_message = FileManager.get_current_bot_action()
        return current_action_message

    return "There's no such command"


async def send_message(message, user_message):
    try:
        global last_message_time
        if time.time() - last_message_time < cooldown_time:
            return

        response = get_response(user_message)
        await message.channel.send(response)
        last_message_time = time.time()
    except Exception as e:
        print(e)


def get_client():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    return client

def run_discord_bot(token):
    client = get_client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        user_message = str(message.content)
        if user_message[0] == "!":
            await send_message(message, user_message[1:])

    client.run(token)

if __name__ == "__main__":
    token = sys.argv[1]
    run_discord_bot(token)