import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types.message import ContentType

API_TOKEN = '7469198396:AAGfhnb-A8l-suGAf23mxRnIECNoxwQwfxM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция для создания обычной клавиатуры с WebApp кнопками
def web_app_keyboard():
    web_app_game = WebAppInfo(url="https://vionaaru.github.io/webapp001")
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Запустить WebApp", web_app=web_app_game)],
        ],
        resize_keyboard=True
    )
    return keyboard

# Функция для создания inline-клавиатуры с WebApp кнопками
def web_app_keyboard_inline():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Запустить Inline WebApp", web_app=web_app)]
        ]
    )
    return keyboard

# Обработчик команды /start
@dp.message(Command("start"))
async def start_fun(message: Message):
    await message.answer(
        "Привет! Нажми кнопку ниже, чтобы открыть WebApp:",
        reply_markup=web_app_keyboard_inline()
    )

# Обработчик команды /inline
@dp.message(Command("inline"))
async def inline_fun(message: Message):
    await message.answer(
        "Вот inline-клавиатура для запуска WebApp:",
        reply_markup=web_app_keyboard()
    )

# Обработчик данных, полученных из WebApp
@dp.message(lambda msg: msg.content_type == ContentType.WEB_APP_DATA)
async def answer(web_app_mes: Message):
    print(web_app_mes)  # Вся информация о сообщении
    print(web_app_mes.web_app_data.data)  # Конкретные данные, отправленные из WebApp
    await web_app_mes.answer(
        f"Получены данные из WebApp: {web_app_mes.web_app_data.data}"
    )

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())