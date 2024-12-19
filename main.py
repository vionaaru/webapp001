import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram.types.message import ContentType

API_TOKEN = '7469198396:AAGfhnb-A8l-suGAf23mxRnIECNoxwQwfxM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция для создания inline-клавиатуры с WebApp кнопками
def web_app_keyboard_inline():
    web_app = WebAppInfo(url="https://vionaaru.github.io/webapp001/")  # URL вашего WebApp
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Запустить WebApp", web_app=web_app)]
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

# Обработчик данных, полученных из WebApp
@dp.message(lambda msg: msg.content_type == ContentType.WEB_APP_DATA)
async def answer(web_app_mes: Message):
    print("Получено сообщение от WebApp:", web_app_mes)
    print("Данные:", web_app_mes.web_app_data.data)
    await web_app_mes.answer(
        f"Получены данные из WebApp: {web_app_mes.web_app_data.data}"
    )

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
