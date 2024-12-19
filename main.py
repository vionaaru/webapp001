import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

API_TOKEN = '7469198396:AAGfhnb-A8l-suGAf23mxRnIECNoxwQwfxM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция для создания обычной клавиатуры с webapp кнопками
def web_app_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    web_app_test = WebAppInfo(url="https://weather.nsu.ru")
    web_app_game = WebAppInfo(url="https://llmaccess3.grabsdigital.com")
    one_button = KeyboardButton(text="Тестовая страница", web_app=web_app_test)
    two_button = KeyboardButton(text="Эбигейл", web_app=web_app_game)
    keyboard.add(one_button, two_button)
    return keyboard

# Функция для создания inline-клавиатуры с webapp кнопками
def web_app_keyboard_inline():
    keyboard = InlineKeyboardMarkup(row_width=1)
    web_app = WebAppInfo(url="https://llmaccess3.grabsdigital.com")
    inline_button = InlineKeyboardButton(text="Веб Эбигейл", web_app=web_app)
    keyboard.add(inline_button)
    return keyboard

# Обработчик команды /start
@dp.message(Command("start"))
async def start_fun(message: Message):
    await message.answer(
        "Привет, я бот для проверки Telegram WebApps! 🖥\n"
        "Страницы можно запустить, нажав на кнопки.",
        reply_markup=web_app_keyboard()
    )

# Обработчик команды /inline
@dp.message(Command("inline"))
async def inline_fun(message: Message):
    await message.answer(
        "Вот inline-клавиатура для запуска WebApp:",
        reply_markup=web_app_keyboard_inline()
    )

# Обработчик любых текстовых сообщений
@dp.message()
async def new_mes(message: Message):
    await start_fun(message)

# Обработчик данных, полученных из web-app
@dp.message(content_types={"web_app_data"})
async def answer(web_app_mes: Message):
    print(web_app_mes)  # Вся информация о сообщении
    print(web_app_mes.web_app_data.data)  # Конкретные данные, отправленные из WebApp
    await web_app_mes.answer(
        f"Получили информацию из веб-приложения: {web_app_mes.web_app_data.data}"
    )

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
