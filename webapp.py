from  aiogram import Bot, Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo

bot=Bot("7848260523:AAExCesoYa-AGgFJRiJfBKemm20SizNAg7E")
dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup=types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Try your luck",web_app=WebAppInfo(url="https://roulette-simulator-iojb.vercel.app/")))
    await message.answer("Hey, my friend!\nIf you want to play our roulette,you need to click on the button 'Try your luck' ",reply_markup=markup)
executor.start_polling(dp)
