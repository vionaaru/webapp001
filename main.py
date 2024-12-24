import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.types.message import ContentType
from environs import Env

env = Env()
env.read_env()

API_TOKEN = env.str("TG_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Клавиатура с inline-кнопкой для WebApp
def web_app_inline_keyboard():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть WebApp", web_app=web_app)]
        ]
    )

# Клавиатура с обычной кнопкой для WebApp
def web_app_reply_keyboard():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Открыть WebApp", web_app=web_app)]
        ],
        resize_keyboard=True
    )

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Нажмите кнопку ниже для открытия WebApp:", reply_markup=web_app_inline_keyboard())
    await message.answer("Или воспользуйтесь обычной кнопкой:", reply_markup=web_app_reply_keyboard())

# Обработчик данных из WebApp
@dp.message(lambda msg: msg.content_type == ContentType.WEB_APP_DATA)
async def handle_web_app_data(message: Message):
    try:
        data = message.web_app_data.data
        await message.answer(f"Получены данные из WebApp: {data}")
        print(f"Получены данные из WebApp: {data}")
    except Exception as e:
        await message.answer("Ошибка при обработке данных WebApp")
        print(f"Ошибка: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
