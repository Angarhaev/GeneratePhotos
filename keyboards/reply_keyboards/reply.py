from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils import texts


class ReplyButtonsCreate:
    """Класс для создания кнопок reply клавиатуры"""
    @staticmethod
    async def create_reply():
        """Создание произвольного количества кнопок"""
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🔎 Find materials")],
                [KeyboardButton(text="🔐 Example of hack"), KeyboardButton(text="💞 Reviews")],
                [KeyboardButton(text="💡 Support Service"), KeyboardButton(text="📄 Offer")],
            ],
            input_field_placeholder="send link", resize_keyboard=True)
        return keyboard
