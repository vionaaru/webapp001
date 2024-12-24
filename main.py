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

# Inline-клавиатура с WebApp
def web_app_keyboard_inline():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Запустить WebApp", web_app=web_app)]
        ]
    )
    return keyboard

# Обычная клавиатура с WebApp
def web_app_keyboard():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Открыть WebApp", web_app=web_app)]
        ],
        resize_keyboard=True
    )
    return keyboard

# Обработчик команды /start
@dp.message(Command("start"))
async def start_fun(message: Message):
    await message.answer(
        "Привет! Нажми inline кнопку ниже, чтобы открыть WebApp:",
        reply_markup=web_app_keyboard_inline()
    )
    await message.answer(
        "Либо воспользуйтесь обычной кнопкой:",
        reply_markup=web_app_keyboard()
    )

# Обработчик данных из WebApp
@dp.message(lambda msg: msg.content_type == ContentType.WEB_APP_DATA)
async def handle_web_app_data(message: Message):
    try:
        web_app_data = message.web_app_data.data
        await message.answer(f"Получены данные из WebApp: {web_app_data}")
        print(f"Получены данные из WebApp: {web_app_data}")
    except Exception as e:
        print(f"Ошибка при обработке данных WebApp: {e}")
        await message.answer("Произошла ошибка при обработке данных")

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
