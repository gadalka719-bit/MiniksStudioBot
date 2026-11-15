import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO, stream=sys.stdout)

bot = Bot(token=9090231137:AAFmDY6EkdrTWgTzkAfrsXuvgtZ58XSzn3I)
dp = Dispatcher(storage=MemoryStorage())

# Главное меню с кнопками
def get_main_menu():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="📥 Скачать видео (Saver + VPN)", callback_data="menu_saver"),
                types.InlineKeyboardButton(text="🎬 ИИ-Помощник по эдитам", callback_data="menu_ai")
            ],
            [
                types.InlineKeyboardButton(text="⚙️ Инструменты эдитера", callback_data="menu_tools")
            ]
        ]
    )
    return keyboard

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Привет, **{message.from_user.first_name}**! 👋\n\n"
        "Это твой личный студийный бот для создания эдитов, скачивания медиа и ИИ-автоматизации.\n"
        "Выбери нужный раздел в меню ниже:",
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

@dp.callback_query(lambda c: c.data.startswith("menu_"))
async def process_menu(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    
    if action == "saver":
        await callback.message.edit_text(
            "📥 **Режим Saver активен**\n\nОтправь мне ссылку на TikTok, YouTube Shorts или Reels, и я скачаю видео без водяных знаков!",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[[types.InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_main")]]
            ),
            parse_mode="Markdown"
        )
    elif action == "ai":
        await callback.message.edit_text(
            "🧠 **ИИ-Редактор эдитов**\n\nНапиши тему или персонажа (например: *эдит по аниме Наруто под phonk*), и я набросаю тебе концепт, тайминги подбивки битов и структуру хуков!",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[[types.InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_main")]]
            ),
            parse_mode="Markdown"
        )
    elif action == "tools":
        await callback.message.edit_text(
            "⚙️ **Инструменты**\n\nЗдесь будут быстрые утилиты (конвертеры, зеркалирование и т.д.).",
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[[types.InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_main")]]
            ),
            parse_mode="Markdown"
        )
    await callback.answer()

@dp.callback_query(lambda c: c.data == "back_to_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Главное меню:",
        reply_markup=get_main_menu()
    )
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())