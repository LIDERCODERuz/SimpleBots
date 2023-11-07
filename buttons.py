from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton, ReplyKeyboardRemove

home = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='🔎 Qidirish')]
    ],
    resize_keyboard=True, one_time_keyboard=True
)

ads = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="💎 Reklama", url="https://t.me/LIDER_CODERuz")]
    ]
)

remove = ReplyKeyboardRemove()
