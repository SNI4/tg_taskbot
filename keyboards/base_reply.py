from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def base_reply_keyboard() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    ib1 = KeyboardButton(text="Мои строки")
    ib2 = KeyboardButton(text="Добавить строку")
    ib3 = KeyboardButton(text="Проверить баланс")

    return ikb.add(ib1).row(ib2, ib3)
