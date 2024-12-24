import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, InlineQueryResultArticle, InputTextMessageContent, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.types.message import ContentType

from environs import Env
# Загружаем переменные окружения
env = Env()
env.read_env()

TG_TOKEN = env.str("TG_TOKEN")

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()

# Функция для создания inline-клавиатуры с WebApp кнопками
def web_app_keyboard_inline():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Запустить WebApp", web_app=web_app)]
        ]
    )
    return keyboard

# Функция для создания обычной клавиатуры с WebApp кнопкой
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
        "Привет! Нажми одну из кнопок ниже, чтобы открыть WebApp:",
        reply_markup=web_app_keyboard_inline()
    )
    await message.answer(
        "Либо воспользуйтесь обычной кнопкой:",
        reply_markup=web_app_keyboard()
    )

# Обработчик данных, полученных из WebApp
@dp.message(lambda msg: msg.content_type == ContentType.WEB_APP_DATA)
async def handle_web_app_data(message: Message):
    web_app_data = message.web_app_data.data
    print(f"Получены данные: {web_app_data}")
    await message.answer(f"Получены данные из WebApp: {web_app_data}")

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
