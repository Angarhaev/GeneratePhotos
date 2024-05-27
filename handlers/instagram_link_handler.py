import time
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from generate_photos import insta_photo_generate, insta_chats_generate
from states.states import AlSettings
from keyboards import KeyboardsCreate
import random
from get_data import insta_info
from utils.easy_func import EasyFunc
import logging
from config_data.config import config_initial

logger_instagram_handler = logging.getLogger(__name__)

router_instagram = Router()


@router_instagram.message(StateFilter(AlSettings.instagram_link))
@EasyFunc.insta_filter()
async def insta_handler(message: Message, keyboards_instance: KeyboardsCreate, config: config_initial, state: FSMContext):
    """Хэндлер колеса прогрузки после успешного получения ссылки"""
    logger_instagram_handler.info('Работа по ссылке инстаграм')
    try:
        await EasyFunc.delete_last_two_messages(message)
    except Exception:
        try:
            await message.delete()
        except Exception:
            logger_instagram_handler.info('Не удалось удалить сообщение')
    correspondence = random.randint(12, 20)
    intimate_photos = random.randint(20, 40)
    intimate_videos = random.randint(6, 10)
    active_ago = random.randint(1, 59)
    info_user = None
    photo_file = None
    list_images = None
    media = None
    gg = await message.answer(f'''□□□□□□□□□□ 0%
Sending a request

They're looking for it now: 258''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text=''''🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 2%
Sending a request

They're looking for it now: 298''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text=''''🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 7%
connecting to the database

They're looking for it now: 298''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 14%
connecting to the database

They're looking for it now: 282''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 18%
connecting to the database

They're looking for it now: 282''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩⬜⬜️⬜️⬜️⬜️⬜️⬜️ 25%
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
Connecting with instagram.com

They're looking for it now: 274''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️⬜️⬜️⬜️ 78%
Connecting with instagram.com

They're looking for it now: 274''')
    try:
        info_user = await insta_info(message.text)
    except Exception:
        logger_instagram_handler.info('Не удалось получить данные из инстаграм')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️⬜️⬜️ 85%
Connecting with instagram.com

They're looking for it now: 274''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️⬜️⬜️ 92%
Looking deeper

They're looking for it now: 302''')
    if info_user:
        try:
            list_images = await insta_chats_generate(info_user, active_ago)
            media = await EasyFunc.media_images(list_images)
        except Exception:
            logging.info('Не удалось сгенерировать фотографию')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️🟩⬜️ 97%
Looking deeper

They're looking for it now: 305''')
    if info_user:
        try:
            photo_file = await insta_photo_generate(info_user, correspondence, intimate_photos, intimate_videos, active_ago)
        except Exception:
            logging.info('Не удалось сгенерировать фотографию')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️🟩️🟩 100%
We're finishing up

They're looking for it now: 305''')
    if photo_file and list_images:
        time.sleep(1)
        markdown_text = f"[{info_user['profile_name']}]({message.text})"
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
        await message.answer("Try a link to Instagram account")
        await state.set_state(AlSettings.instagram_link)
