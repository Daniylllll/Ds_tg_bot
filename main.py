import logging
import multiprocessing
import disnake
from aiogram import Dispatcher, Bot, executor, types
from disnake.ext import commands as commands_ds

from config import *

logging.basicConfig(level=logging.DEBUG)

bot = Bot(TG_TOKEN)
dp = Dispatcher(bot=bot)

intents = disnake.Intents.default()
bot_ds = commands_ds.Bot(command_prefix="/", intents=intents)


@bot_ds.event
async def on_ready():
    print(f'Logged in as {bot_ds.user.name}')


@dp.message_handler(commands=['start'])
async def cd_start(message: types.Message):
    await message.answer("Привет друг!")
    text_for_ds = "Hello from Telegram!!!"
    await send_ds_mess()


async def send_ds_mess():
    channel = bot_ds.get_channel(1160219846571733042)
    print(channel)
    if channel:
        await channel.send("Hello world!!!")


async def send_mess():
    await bot.send_message(chat_id=5580704087, text="I'm here!")


@bot_ds.command()
async def start(ctx):
    await ctx.send("hi!")
    await send_ds_mess()
    await send_mess()


def run_ds_bot():
    bot_ds.run(token=DS_TOKEN)


def run_tg_bot():
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=run_tg_bot)
    process2 = multiprocessing.Process(target=run_ds_bot)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
