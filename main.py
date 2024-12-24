import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, InlineQueryResultArticle, InputTextMessageContent
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

# Обработчик команды /start
@dp.message(Command("start"))
async def start_fun(message: Message):
    await message.answer(
        "Привет! Нажми кнопку ниже, чтобы открыть WebApp:",
        reply_markup=web_app_keyboard_inline()
    )

# Обработчик данных, полученных из WebApp
@dp.message(lambda msg: msg.content_type == ContentType.WEB_APP_DATA)
async def handle_web_app_data(message: Message):
    web_app_data = message.web_app_data.data  # Данные из WebApp
    web_app_query_id = message.web_app_data.query_id  # Уникальный ID запроса
    print(f"Получены данные из WebApp: {web_app_data}")
    print(f"Query ID: {web_app_query_id}")

    # Отправляем ответ через AnswerWebAppQuery
    if web_app_query_id:
        await bot.answer_web_app_query(
            web_app_query_id,
            InlineQueryResultArticle(
                id="1",
                title="Данные получены",
                input_message_content=InputTextMessageContent(
                    f"Данные из WebApp: {web_app_data}"
                )
            )
        )
    else:
        await message.answer("Не удалось обработать данные WebApp.")

# Основная функция
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())