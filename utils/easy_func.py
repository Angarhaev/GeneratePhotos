import requests
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.states import AlSettings
import re
import logging
from keyboards import KeyboardsCreate
from aiogram.types import InputMediaPhoto
from config_data.config import config_initial


logger_easy = logging.getLogger(__name__)

class EasyFunc:
    @staticmethod
    def custom_message_filter():
        """Кастомный фильтр для проверки существования ссылки"""
        def decorator(func):
            async def wrapped(url_message: Message, state: FSMContext):
                try:
                    response = requests.get(url_message.text)
                    if response.status_code == 200:
                        return await func(url_message, state)
                except Exception:
                    await url_message.answer(f'The page \n\n<b>{url_message.text}</b> \n\ndoes not exist. Try again',
                                             parse_mode='html')
                    await state.set_state(AlSettings.error_link)
            return wrapped
        return decorator

    @staticmethod
    def insta_filter():
        """Кастомный фильтр для ссылки инстаграм"""
        def decorator(func):
            async def wrapped(message: Message, keyboards_instance: KeyboardsCreate, config: config_initial, state: FSMContext):
                try:
                    if message.text == 'www.instagram.com/anny_may/' or message.text == 'https://www.instagram.com/anny_may/':
                        raise Exception('URL из примера')
                    pattern = re.compile(r"(?:https?:\/\/)?(?:www\.)?instagram\.com\/([^\/?]+)", re.IGNORECASE)
                    response = bool(pattern.search(message.text))
                    if response:
                        logger_easy.info('URL соответствует ссылке на instagram')
                        return await func(message, keyboards_instance, config, state)
                    else:
                        raise Exception('URL не соответствует ссылке на instagram')
                except Exception as exc:
                    logger_easy.info(f'Ошибка фильтра {exc}')
                    await message.answer("Try a link to Instagram account", reply_markup=keyboards_instance.keyboard_back)
                    await state.set_state(AlSettings.instagram_link)

            return wrapped

        return decorator

    @staticmethod
    def facebook_filter():
        """Кастомный фильтр для ссылки фэйсбук"""
        def decorator(func):
            async def wrapped(message: Message, keyboards_instance: KeyboardsCreate, config: config_initial, state: FSMContext):
                try:
                    if message.text == 'https://www.facebook.com/anny_may/' or message.text == 'www.facebook.com/anny_may/':
                        raise Exception('URL из примера')
                    pattern = re.compile(r"(?:https?:\/\/)?(?:www\.)?facebook\.com\/([^\/?]+)", re.IGNORECASE)
                    response = bool(pattern.search(message.text))
                    if response:
                        logger_easy.info('URL соответствует ссылке на facebook')
                        return await func(message, keyboards_instance, config, state)
                    else:
                        raise Exception('URL не соответствует ссылке на facebook')
                except Exception as exc:
                    logger_easy.info(f'Ошибка фильтра {exc}')
                    try:
                        await EasyFunc.delete_last_two_messages(message)
                    except Exception:
                        try:
                            await message.delete()
                        except Exception:
                            logger_easy.info('Не удалось удалить сообщения')
                    await message.answer("Try a link to Facebook account",
                                         reply_markup=keyboards_instance.keyboard_back)
                    await state.set_state(AlSettings.facebook_link)

            return wrapped

        return decorator

    @staticmethod
    def tiktok_filter():
        """Кастомный фильтр для ссылки тикток"""

        def decorator(func):
            async def wrapped(message: Message, keyboards_instance: KeyboardsCreate, state: FSMContext):
                try:
                    if message.text == 'https://t.me/anny_may' or message.text == '@anny_may':
                        raise Exception('URL из примера')
                    pattern = r'@(?:\w+)|(?:https?://)?(?:www\.)?tiktok\.com/\w+'
                    matches = re.findall(pattern, message.text)
                    response = False
                    url_tt = message.text
                    username = matches[0]
                    if message.text.startswith('@') or message.text.startswith(
                            'www.tiktok.com') or message.text.startswith(
                            'https://www.tiktok.com') or message.text.startswith('tiktok.com'):
                        url_tt = f'https://www.tiktok.com{username}'
                        response = True
                    if response:
                        logger_easy.info(f'URL соответствует ссылке на tiktok:{url_tt}')
                        return await func(message, keyboards_instance, state)
                    else:
                        raise Exception('URL не соответствует ссылке на tiktok')

                except Exception as exc:
                    logger_easy.info(f'Ошибка фильтра {exc}')
                    await message.answer("Try a link to Telegram account",
                                         reply_markup=keyboards_instance.keyboard_back)
                    await state.set_state(AlSettings.tiktok_link)

            return wrapped

        return decorator

    @staticmethod
    def telegram_filter():
        """Кастомный фильтр для ссылки телеграм"""
        def decorator(func):
            async def wrapped(message: Message, keyboards_instance: KeyboardsCreate, state: FSMContext):
                try:
                    if message.text == 'https://t.me/anny_may' or message.text == '@anny_may':
                        raise Exception('URL из примера')
                    pattern = r"\b(?:https?://)?(?:t\.me/|@)?[a-zA-Z0-9_]+(?:\b|\?[\w=&%]+)?"
                    matches = re.findall(pattern, message.text)
                    response = False
                    url_tg = message.text
                    username = matches[0]
                    if message.text.startswith('@') or message.text.startswith('https://t.me/') or message.text.startswith('https://telegram.me/') or message.text.startswith('t.me/'):
                        url_tg = f'https://t.me/{username}'
                        response = True
                    if response:
                        logger_easy.info(f'URL соответствует ссылке на telegram:{url_tg}', )
                        return await func(message, keyboards_instance, state)
                    else:
                        raise Exception('URL не соответствует ссылке на telegram')

                except Exception as exc:
                    logger_easy.info(f'Ошибка фильтра {exc}')
                    await message.answer("Try a link to TikTok account",
                                         reply_markup=keyboards_instance.keyboard_back)
                    await state.set_state(AlSettings.telegram_link)

            return wrapped

        return decorator

    @staticmethod
    async def media_images(dict_images):
        """Метод возвращающий объект для отправки медиа файлов в одном сообщении"""
        try:
            media = []
            count = 0
            for i_num, i_photo in enumerate(dict_images):
                if i_num != 0 and count < 10:
                    count += 1
                    media.append(InputMediaPhoto(media=i_photo))
            return media
        except Exception as exc:
            logger_easy.exception('Не удалось сформировать файлы для отправки', exc_info=exc)
            return None

    @staticmethod
    async def delete_last_two_messages(message: Message):
        """Метод для удаления двух последних сообщений"""
        try:
            chat_id = message.chat.id
            last_message_id = message.message_id
            before_last_message_id = last_message_id - 1
            await message.bot.delete_message(chat_id, last_message_id)
            await message.bot.delete_message(chat_id, before_last_message_id)
        except Exception as exc:
            logger_easy.info('Не удалось удалить 2 сообщения:', exc)
            return False
