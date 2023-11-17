from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove
main=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Valyutalar",callback_data='val'),InlineKeyboardButton(text="Ma'lumot olish",callback_data='mal')],
        [InlineKeyboardButton(text="Foydali sahifa",callback_data='fsah'),InlineKeyboardButton(text='Ob-havo',callback_data='kl')]
    ]
)
back=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ortga qaytish',callback_data='ortga')]
    ]
)
knopka=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Botlar',callback_data='bottt'),InlineKeyboardButton(text='Kanallar',callback_data='kanal')],
        [InlineKeyboardButton(text='Saytlar',callback_data='sayt'),InlineKeyboardButton(text='Ortga qaytish',callback_data='backkk')]
    ]
)
back1=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Ortga qaytish',callback_data='orqaga')]
    ]
)
shahar=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Toshkent',callback_data='tosh'),InlineKeyboardButton(text='Samarqand',callback_data='sam'),InlineKeyboardButton(text='Andijon',callback_data='andi')],
        [InlineKeyboardButton(text='Nukus',callback_data='nuk'),InlineKeyboardButton(text='Namangan',callback_data='nam'),InlineKeyboardButton(text='Sirdaryo',callback_data='sir')],
        [InlineKeyboardButton(text='Urganch',callback_data='ur'),InlineKeyboardButton(text='Guliston',callback_data='gul'),InlineKeyboardButton(text='Jizzax',callback_data='jiz')],
        [InlineKeyboardButton(text='Navoiy',callback_data='nav'),InlineKeyboardButton(text='Qo\'ng\'irot',callback_data='qon'),InlineKeyboardButton(text='Shahrisabz',callback_data='sha')],
        [InlineKeyboardButton(text='Termiz',callback_data='tem'),InlineKeyboardButton(text='Qarshi',callback_data='qar'),InlineKeyboardButton(text='Yangi Marg\'ilon',callback_data='yan')]
    ]
)
