import logging
from aiogram import Dispatcher, types, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from buttons import home, remove, ads
from states import step
import wikipedia
wikipedia.set_lang('uz')


logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN, parse_mode="html")
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"], state='*')
async def start_page(message: types.Message):
    await message.answer(f"🤓 <b>Assalomu alaykum, men wikipediyadan maqolalar topib beruvchi botman!</b>", reply_markup=home)

@dp.message_handler(text="🔎 Qidirish", state='*')
async def search_page(message: types.Message):
    await message.answer(f"🔎 <b>Qidirayotgan maqolangiz nomini yozib yuboring...</b>", reply_markup=remove)
    await step.search.set()

@dp.message_handler(state=step.search)
async def result_page(message: types.Message):
    try:
        await bot.send_chat_action(message.chat.id, action=types.ChatActions.TYPING)
        result = wikipedia.summary(message.text)
        await message.answer(f"📖 <b>Maqola topildi...</b>\n\n{result}", reply_markup=home)
        await step.first()
    except:
        await message.answer(f"😔 <b>Maqola topilmadi, boshqa nom bilan izlab ko'ring!</b>", reply_markup=ads)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
