import disnake
from disnake.ext import commands as commands_ds

intents = disnake.Intents.all()
bot_ds = commands_ds.Bot(command_prefix="/", intents=intents)


@bot_ds.event
async def on_ready():
    print(f'Logged in as {bot_ds.user.name}')
