import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

# Вставьте сюда токен вашего бота от @BotFather
BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"

# Ссылка на ваше веб-приложение (Mini App)
WEB_APP_URL = "https://your-site.com/app" 

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(commands=["start"])
async def cmd_start(message: types.Message):
    # Создаем Inline кнопку с типом web_app
    # Именно web_app открывает приложение. 
    # Telegram сам определит, открывать ли его в Full Screen, 
    # но обычно Inline кнопки открывают его поверх чата (что визуально похоже на фуллскрин или шторку).
    # Чтобы гарантировать максимальное раскрытие, внутри JS кода приложения (который я дал выше) 
    # уже есть вызов tg.expand().
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Открыть Swapka", 
                web_app=WebAppInfo(url=WEB_APP_URL)
            )
        ]
    ])

    await message.answer(
        "👋 Привет! Нажми на кнопку ниже, чтобы открыть приложение.",
        reply_markup=keyboard
    )

# Основная функция запуска
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
