import discord

def get_response(message: str):
    user_message = message.lower()
    if user_message == 'continue':
        with open('shared_variable.txt', 'w') as f:
            f.seek(0)
            f.truncate()
            f.write("continue")
            
        return "Script was unpaused! Make sure to have verified AFK check"

    if user_message == 'status':
        with open('status.txt', 'r') as f:
            status_message = f.read()
            return status_message

    return "There's no such command"

async def send_message(message, user_message):
    try:
        response = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA5ODE4MDIxMjA3Nzg5NTY5Mw.G72ldH.Vx9B9yGBRi0NyNmpB_Zpmd6CwZmdB8jrZTKzo8'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

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

    client.run(TOKEN)

run_discord_bot()