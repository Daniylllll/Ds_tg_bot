from aiogram import Dispatcher, Bot, types
from config import *
import disnake
from disnake.ext import commands as commands_ds

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot=bot)

intents = disnake.Intents.all()
bot_ds = commands_ds.Bot(command_prefix="/", intents=intents)


@bot_ds.event
async def on_ready():
    print(f'Logged in as {bot_ds.user.name}')

async def send_ds_mess():
    guild = bot_ds.get_guild(1159239010003193947)
    print(guild)
    channel = guild.get_channel(1160219846571733042)
    print(channel)
    if channel:
        await channel.send("Hello world!!!")


@dp.message_handler(commands=['start'])
async def cd_start(message: types.Message):
    await message.answer("Привет друг!")
    text_for_ds = "Hello from Telegram!!!"
    await send_ds_mess()

async def send_mess_tg():
    await bot.send_message(chat_id=5580704087, text="I'm here!")


@bot_ds.command()
async def start(ctx):
    await ctx.send("hi!")
    await send_ds_mess()
    await send_mess_tg()

if __name__ == '__main__':
    from config import DS_TOKEN
    bot_ds.run(token=DS_TOKEN)
