from aiogram import Bot, Dispatcher, types, executor
import logging

API_TOKEN = '7547663858:AAGvWooLHRxpJ08z3jDO0FnJZvQEj8tUNT0'

# Logging setup
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start command
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply(
        "مرحبًا بك في MiniApp! اختر خيارًا: \n1. Play\n2. Join Community",
        reply_markup=main_menu()
    )

# Main menu keyboard
def main_menu():
    keyboard = types.InlineKeyboardMarkup()
    play_button = types.InlineKeyboardButton(text="Play", callback_data="play")
    community_button = types.InlineKeyboardButton(text="Join Community", url="https://t.me/YourCommunityLink")
    keyboard.add(play_button, community_button)
    return keyboard

# Handle Play button
@dp.callback_query_handler(lambda call: call.data == "play")
async def handle_play(call: types.CallbackQuery):
    await call.message.answer(
        "جاري فتح اللعبة...",
        reply_markup=types.InlineKeyboardMarkup().add(
            types.InlineKeyboardButton(
                text="فتح الصفحة",
                url="https://your-hosted-miniapp-link.com"
            )
        )
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
