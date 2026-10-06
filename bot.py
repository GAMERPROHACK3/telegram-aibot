import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="👋 Привет")],
            [KeyboardButton(text="ℹ️ Информация")]
        ],
        resize_keyboard=True
    )

    await message.answer(
        "Привет! 👋\n\n"
        "Бот успешно запущен.",
        reply_markup=keyboard
    )


@dp.message()
async def message_handler(message: Message):
    if message.text == "👋 Привет":
        await message.answer("Привет! 👋")

    elif message.text == "ℹ️ Информация":
        await message.answer(
            "🤖 Это мой Telegram-бот.\n"
            "Он работает на Python + aiogram."
        )

    else:
        await message.answer(
            "Я получил твоё сообщение:\n\n"
            f"{message.text}"
        )


async def main():
    if not TOKEN:
        raise RuntimeError("Переменная BOT_TOKEN не установлена")

    bot = Bot(TOKEN)

    print("Бот запущен!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
