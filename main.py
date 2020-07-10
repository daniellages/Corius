import discord
from discord.ext import commands
import json

with open("secret.json") as json_file:
    secret = json.load(json_file)

# Start the bot
client = commands.Bot(command_prefix="", case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd)
    print("\u001b[35m##############\n\u001b[36m CORIUS READY\n\u001b[35m##############\u001b[0m")

# Handle errors
@client.event
async def on_command_error(ctx, error):
    if  isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

@client.event
async def on_message(message):
    if message.author.id == secret["authorized_id"] and message.channel.id == secret["channel_id"]:
        await message.channel.send(str(message.author.id))

# Bot Token
try:
    client.run(secret["token"])
except KeyboardInterrupt:
    pass