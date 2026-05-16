import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = '8771897953:AAESHn9hpF9HHItO3TLe3wxU58SPRVvKGqo'


dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, Scalingo!")


@dp.message()
async def echo_start_handler(message: Message) -> None:
    try:

        await message.send_copy(chat_id=message.chat.id)
    except TypeError:

        await message.answer(*"Nice try!")


async def main() -> None:

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=PerseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
