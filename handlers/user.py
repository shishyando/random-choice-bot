from aiogram import types
from aiogram.dispatcher.filters import Command

from config import VARIANT_NUM, VARIANT_LEN, MESSAGE_LEN
from loader import dp


@dp.message_handler(Command(["start", "help"]))
async def provide_info(message: types.Message):
    chat_id = message.chat.id
    info = "Things to know:\n" \
           "This is an inline bot, just type @rnd_choice_bot in any chat to see an example\n" \
           "Separator used: <code>' '</code>\n" \
           f"Each variant length limit is {VARIANT_LEN}\n" \
           f"Total amount of variants shown is &#8804; {VARIANT_NUM}\n" \
           f"Total message length limit is {MESSAGE_LEN}"
    await dp.bot.send_message(chat_id, info)
