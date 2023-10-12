from aiogram import types
from ds_bot import bot_ds
from tg_bot import dp, bot


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

async def send_mess_tg():
    await bot.send_message(chat_id=5580704087, text="I'm here!")


@bot_ds.command()
async def start(ctx):
    await ctx.send("hi!")
    await send_ds_mess()
    await send_mess_tg()