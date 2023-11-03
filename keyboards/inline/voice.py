from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



voice = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text="🎙 Audio tinglash", callback_data="voice"),
    ]
    ]
)

