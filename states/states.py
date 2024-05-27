from aiogram.fsm.state import StatesGroup, State


class AlSettings(StatesGroup):
    start = State()
    social = State()
    instagram_link = State()
    facebook_link = State()
    tiktok_link = State()
    telegram_link = State()
    to_pay = State()
    after_pay = State()
    after_pay_crypto = State()
    bill = State()
    error_link = State()
    repeat_pay = State()
    crypto = State()
    default = State()