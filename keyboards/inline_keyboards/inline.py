from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils import texts
import logging

logger_create_inline = logging.getLogger(__name__)


class ButtonsCreate:
    """Класс для создания кнопок"""
    @staticmethod
    async def create_one(button_one: dict[str, int: str, int], button_back: dict[str, int: str, int] = None,
                         width: int = 1):
        """Метод для создания одинокой произвольной кнопки с возможностью наличия
           кнопки "Назад" при явном указании"""
        one_button_keyboard: InlineKeyboardBuilder = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = []

        for key, button in button_one.items():
            buttons.append(InlineKeyboardButton(text=button, callback_data=key))

        one_button_keyboard.row(*buttons, width=width)

        kb_button_back = await ButtonsCreate.button_back_add(button_back)
        if kb_button_back:
            one_button_keyboard.row(kb_button_back, width=width)

        return one_button_keyboard.as_markup()

    @staticmethod
    async def button_back_add(button_back: dict[str, int: str, int]):
        """Метод кнопки дополнительной кнопки "Назад" для клавиатуры"""
        if button_back:
            for key, button in button_back.items():
                kb_button_back = InlineKeyboardButton(text=button, callback_data=key)
                return kb_button_back
        else:
            return None

    @staticmethod
    async def create_inline_keyboard(width: int, buttons_dict: dict[str, int: str, int],
                                     button_back: dict[str, int: str, int] = None):
        """Метод для создания произвольного количества кнопок с возможностью наличия
        кнопки "Назад" при явном указании"""
        menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = []
        for key, button in buttons_dict.items():
            buttons.append(InlineKeyboardButton(text=button, callback_data=key))

        menu.row(*buttons, width=width)

        kb_button_back = await ButtonsCreate.button_back_add(button_back)
        if kb_button_back:
            menu.row(kb_button_back)

        return menu.as_markup()

    @staticmethod
    async def create_pay_keyboard(buttons_dict: dict[str, int: str, int],
                                  button_back: dict[str, int: str, int] = None):
        """Метод для создания произвольного количества кнопок с возможностью наличия
        кнопки "Назад" при явном указании"""
        logger_create_inline.info('Создаем кнопки для оплаты')
        menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
        buttons_1_in_line: list[InlineKeyboardButton] = []
        for key, button in buttons_dict.items():
            if key != '/reviews' and key != '/instruction':
                buttons_1_in_line.append(InlineKeyboardButton(text=button, callback_data=key))

        menu.row(*buttons_1_in_line, width=1)

        buttons_2_in_line: list[InlineKeyboardButton] = []
        for key, button in buttons_dict.items():
            if key == '/reviews':
                buttons_2_in_line.append(
                    InlineKeyboardButton(text=button, callback_data=key, url='https://t.me/reviews_intimates'))
            elif key == '/instruction':
                buttons_2_in_line.append(InlineKeyboardButton(text=button, callback_data=key,
                                                              url='https://www.youtube.com/watch?v=KW9L9vIztgU&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9'))
        menu.row(*buttons_2_in_line, width=2)

        kb_button_back = await ButtonsCreate.button_back_add(button_back)
        if kb_button_back:
            menu.row(kb_button_back)

        return menu.as_markup()

    @staticmethod
    async def create_start_keyboard(buttons_dict: dict[str, int: str, int],
                                    button_back: dict[str, int: str, int] = None):
        """Метод для создания произвольного количества кнопок с возможностью наличия
        кнопки "Назад" при явном указании"""
        logger_create_inline.info('Создаем кнопки для оплаты')
        menu: InlineKeyboardBuilder = InlineKeyboardBuilder()
        buttons_1_in_line: list[InlineKeyboardButton] = []
        for key, button in buttons_dict.items():
            if key == '/search_photos':
                buttons_1_in_line.append(InlineKeyboardButton(text=button, callback_data=key))

        menu.row(*buttons_1_in_line, width=1)

        buttons_2_in_line: list[InlineKeyboardButton] = []
        for key, button in buttons_dict.items():
            if key == '/reviews':
                buttons_2_in_line.append(
                    InlineKeyboardButton(text=button, callback_data=key, url='https://t.me/reviews_intimates'))
            elif key == '/instruction':
                buttons_2_in_line.append(InlineKeyboardButton(text=button, callback_data=key,
                                                              url='https://www.youtube.com/watch?v=KW9L9vIztgU&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9'))
            elif key == '/support':
                buttons_2_in_line.append(InlineKeyboardButton(text=button, callback_data=key, url='www.t.me/durov'))
            elif key == '/offer':
                buttons_2_in_line.append(InlineKeyboardButton(text=button, callback_data=key, url='https://telegra.ph/OFFER-FOR-INFORMATION-SERVICES-03-06'))
        menu.row(*buttons_2_in_line, width=2)

        kb_button_back = await ButtonsCreate.button_back_add(button_back)
        if kb_button_back:
            menu.row(kb_button_back)

        return menu.as_markup()




class KeyboardsCreate:
    """Класс для создания клавиатур для модуля search_settings"""
    def __init__(self):
        logger_create_inline.info("Инициализированы переменные клаиватуры")
        self.keyboard_back = None
        self.keyboard_start = None
        self.keyboard_social = None
        self.keyboard_payment = None
        self.keyboard_currency = None
        self.keyboard_crypto = None

    @classmethod
    async def initialize(cls):
        logger_create_inline.info("Созданы инстансы клавиатуры")
        instance = cls()
        instance.keyboard_back = await instance.create_keyboard_back()
        instance.keyboard_start = await instance.create_start()
        instance.keyboard_social = await instance.create_social()
        instance.keyboard_payment = await instance.create_payment()
        instance.keyboard_currency = await instance.create_select_currency()
        instance.keyboard_crypto = await instance.create_select_crypto()

        return instance

    @staticmethod
    async def create_keyboard_back():
        """Метод для создания клавиатуры, состоящей из кнопки back"""
        keyboard_back = await ButtonsCreate.create_one(button_one=texts.back, button_back=None)
        return keyboard_back

    @staticmethod
    async def create_start():
        """Метод для создания клавиатуры стартового меню"""
        keyboard_start = await ButtonsCreate.create_start_keyboard(buttons_dict=texts.menu_start)
        return keyboard_start

    @staticmethod
    async def create_social():
        """Метод для создания клавиатуры выбора социальной сети"""
        keyboard_social = await ButtonsCreate.create_inline_keyboard(width=1, buttons_dict=texts.menu_social,
                                                                     button_back=texts.back)
        return keyboard_social

    @staticmethod
    async def create_payment():
        """Метод создания клаиватуры для оплаты"""
        logger_create_inline.info('Инициализировано создание клавиатуры для оплаты')
        keyboard_payment = await ButtonsCreate.create_pay_keyboard(buttons_dict=texts.menu_payment)
        return keyboard_payment

    @staticmethod
    async def create_select_currency():
        """Метод создания клавиатуры выбора валюты оплаты"""
        logger_create_inline.info('Инициализировано создание клавиатуры для выбора валюты')
        keyboard_currency = await ButtonsCreate.create_inline_keyboard(width=1, buttons_dict=texts.menu_currency,
                                                                       button_back=texts.back)

        return keyboard_currency

    @staticmethod
    async def create_select_crypto():
        """Метод создания клавиатуры выбора криптовалюты"""
        logger_create_inline.info('Инициализировано создание клавиатуры для выбора валюты')
        keyboard_crypto = await ButtonsCreate.create_inline_keyboard(width=1, buttons_dict=texts.menu_crypto,
                                                                       button_back=texts.back)

        return keyboard_crypto

