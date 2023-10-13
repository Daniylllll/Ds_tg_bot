import discord
from aiogram import Dispatcher, Bot, types
from config import *
import disnake
from discord.ext import commands as commands_ds
from database import *

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot=bot)

# intents = discord.Intents.all()
# bot_ds = commands_ds.Bot(command_prefix="/", intents=intents)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def send_ds_mess(self):
        print(list(self.guilds))

client = MyClient(intents=discord.Intents.all())

async def on_startup(_):
    await db_start()


# @bot_ds.event
# async def on_ready():
#     print(f'Logged in as {bot_ds.user.name}')

# async def send_ds_mess():
#     print(list(bot_ds.guilds))
    # mess_info = await get_mess(0)
    # print(mess_info)
    # for data in mess_info:
    #     print(data[1])
    #     guild = bot_ds.get_channel(data[1])
    #     print(guild)
    # channel = guild.get_channel(1160219846571733042)
    # print(channel)
    # if channel:
    #     await channel.send("Hello world!!!")


@dp.message_handler(commands=['start'])
async def cd_start(message: types.Message):
    await message.answer("Привет друг!")
    text_for_ds = "Hello from Telegram!!!"
    await update_mess("Hello world!!!", 1160219846571733042)
    await client.send_ds_mess()

async def send_mess_tg():
    await bot.send_message(chat_id=5580704087, text="I'm here!")


# @bot_ds.command()
# async def start(ctx):
#     await ctx.send("hi!")
#     await send_ds_mess()
#     await send_mess_tg()

if __name__ == '__main__':
    from config import DS_TOKEN
    client.run(DS_TOKEN)
