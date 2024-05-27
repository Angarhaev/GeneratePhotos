from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from generate_photos import insta_photo_generate
from states.states import AlSettings
from keyboards import KeyboardsCreate
import random
from get_data import insta_info
from get_data.meta_data_telegram import telegram_get_data


"""Инициализация роутера"""
router_social = Router()


@router_social.message(F.text == '🔎 Find materials')
async def social(message: Message, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер, срабатывающий при нажатии кнопки Search Photos"""
    await message.delete()
    await message.answer('Choose the social net for hacking:'
                                  '\n By using the bot you agree with the offer to provide information services', reply_markup=keyboards_instance.keyboard_social)
    await state.set_state(AlSettings.social)


@router_social.callback_query(StateFilter(AlSettings.instagram_link, AlSettings.facebook_link,
                                          AlSettings.telegram_link, AlSettings.tiktok_link), F.data == '/back')
@router_social.callback_query(F.data == '/search_photos')
async def social(callback: CallbackQuery, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер, срабатывающий при нажатии кнопки Search Photos"""
    await callback.message.delete()
    await callback.message.answer('Choose the social net for hacking:'
                                  '\n By using the bot you agree with the offer to provide information services', reply_markup=keyboards_instance.keyboard_social)
    await state.set_state(AlSettings.social)


@router_social.callback_query(F.data == '/instagram')
async def send_link(callback: CallbackQuery, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер для отправки инстаграм ссылки"""
    await callback.message.delete()
    await callback.message.answer("Send a link to Instagram account", reply_markup=keyboards_instance.keyboard_back)
    await state.set_state(AlSettings.instagram_link)


@router_social.callback_query(F.data == '/facebook')
async def send_link(callback: CallbackQuery, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер для отправки facebook ссылки"""
    await callback.message.delete()
    await callback.message.answer("Send a link to Facebook account", reply_markup=keyboards_instance.keyboard_back)
    await state.set_state(AlSettings.facebook_link)


@router_social.callback_query(F.data == '/tiktok')
async def send_link(callback: CallbackQuery, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер для отправки tiktok ссылки"""
    await callback.message.delete()
    await callback.message.answer("Send a link to TikTok account", reply_markup=keyboards_instance.keyboard_back)
    await state.set_state(AlSettings.tiktok_link)


@router_social.callback_query(F.data == '/telegram')
async def send_link(callback: CallbackQuery, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер для отправки telegram ссылки"""

    await callback.message.delete()
    await callback.message.answer("Send a link to Telegram account", reply_markup=keyboards_instance.keyboard_back)
    await state.set_state(AlSettings.telegram_link)
