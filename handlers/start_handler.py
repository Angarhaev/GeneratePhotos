from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import StateFilter, CommandStart
from aiogram.fsm.context import FSMContext
from keyboards import KeyboardsCreate
from keyboards import ReplyButtonsCreate
from states.states import AlSettings
from config_data.config import requisites_initial


router = Router()


@router.message(F.text == '/start')
@router.message(StateFilter(None), CommandStart)
async def start_handler(message: Message, keyboards_instance: KeyboardsCreate, requisites: requisites_initial,  state: FSMContext):
    """Стартовый хэндлер при запуске бота. Пользователь получает стартовую gif и клавиатуру для дальнейших действий"""
    reply_kb = await ReplyButtonsCreate.create_reply()
    await message.delete()
    text = ('😈 <b>INTIMATES</b> <i>is a neural network trained to search for photos</i>')
    await message.bot.send_animation(chat_id=message.chat.id,
                                     animation='CgACAgIAAxkBAAMGZfBKm0Jcl5pVy4GWw_UsO5DPfngAAvY_AAIZwnlLrHwvn2FVYog0BA',
                                     caption=text,
                                     parse_mode='html', reply_markup=reply_kb)
    await message.answer('_________________Menu_________________', reply_markup=keyboards_instance.keyboard_start)
    #Использовать для получения id gif, в случае изменения gif. Подставить в "animation"
    # if message.animation:
    #     gif_id = message.animation.file_id
    #     await message.answer(f'ID GIF-изображения: {gif_id}')

    await state.set_state(AlSettings.start)


@router.callback_query(StateFilter(AlSettings.social), F.data == '/back')
async def start_handler(callback: CallbackQuery, keyboards_instance: KeyboardsCreate, state: FSMContext):
    """Стартовый хэндлер. Тоже самое. Активируетя при нажатии кнопки нразад в следующем меню, т.е. ловит колбэк."""
    await callback.message.delete()
    text = ('😈 <b>INTIMATES</b> <i>is a neural network trained to search for photos.</i>')
    await callback.message.answer('_________________Menu_________________:', reply_markup=keyboards_instance.keyboard_start)
    await state.set_state(AlSettings.start)
