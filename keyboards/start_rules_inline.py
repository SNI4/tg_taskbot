from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_rules_keyboard() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(row_width=1)

    ib1 = InlineKeyboardButton(text="✅",
                               callback_data="accept_rules"
                               )

    return ikb.add(ib1)
