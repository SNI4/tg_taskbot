from keyboards.base_reply import base_reply_keyboard
from loader import dp, bot
from aiogram import types

from utils.misc.json_worker import add_user


@dp.callback_query_handler()
async def rules_callback(callback: types.CallbackQuery):
    if callback.data == "accept_rules":
        await add_user(callback.from_user.id)

        await bot.send_message(callback.message.chat.id,
                               'Теперь вы можете пользоваться ботом!', reply_markup=base_reply_keyboard())


