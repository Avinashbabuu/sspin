from aiogram import types, Dispatcher
from utils.db import update_user_balance, get_user_balance
import config

async def add_balance(message: types.Message):
    if message.from_user.id != config.ADMIN_ID:
        return
    try:
        _, user_id, amount = message.text.split()
        new_balance = update_user_balance(user_id, int(amount))
        await message.answer(f"✅ Updated balance: ₹{new_balance}")
    except:
        await message.answer("❌ Usage: /addbal USER_ID AMOUNT")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(add_balance, commands=["addbal"])