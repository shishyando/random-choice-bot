import aiogram
import config
import handlers
from loader import dp


async def on_startup(dp: aiogram.Dispatcher):
    for admin in config.ADMINS:
        try:
            # await dp.bot.send_message(admin, "Bot started")
            pass

        except Exception as err:
            print(err)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, on_startup=on_startup)
