from aiogram import types
from keyboards.start_rules_inline import create_rules_keyboard
from loader import dp
from utils.misc.json_worker import validate_user


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if await validate_user(str(message.from_user.id)) is False:
        await message.answer("Для продолжения, согласитесь с правилами: (rules)", reply_markup=create_rules_keyboard())
    else:
        await message.reply('Вы уже согласились с правилами.')
