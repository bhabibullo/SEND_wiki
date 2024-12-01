import logging
import wikipedia
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

API_TOKEN = 'Your_bot_token'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

wikipedia.set_lang('uz')

@dp.message(Command(commands=['start', 'help']))
async def send_welcome(message: types.Message):
    await message.reply("Wikipedia botiga xush kelibsiz!")


@dp.message(F.text) 
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except Exception:
        await message.answer("Bu mavzuga oid maqola yo'q")

if __name__ == '__main__':
    import asyncio

    asyncio.run(dp.start_polling(bot))
