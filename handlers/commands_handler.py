from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from keyboards import KeyboardsCreate
from aiogram.enums.parse_mode import ParseMode

router_commands = Router()


@router_commands.message(F.text == '🔐 Example of hack')
async def commands_example(message: Message, keyboards_instance: KeyboardsCreate, state: FSMContext):
    await message.delete()
    markdown_text = f"[Example of hack](https://www.youtube.com/watch?v=KW9L9vIztgU&ab_channel=%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B5%D0%B9)"
    await message.answer(markdown_text, parse_mode=ParseMode.MARKDOWN)


@router_commands.message(F.text == "💞 Reviews")
async def reviews_handler(message: Message, state: FSMContext):
    await message.delete()
    markdown_text = f"[💞 read reviews](https://t.me/reviews_intimates)"
    await message.answer(markdown_text, parse_mode=ParseMode.MARKDOWN)


@router_commands.message(F.text == "📄 Offer")
async def reviews_handler(message: Message, state: FSMContext):
    await message.delete()
    markdown_text = f"[📄 Offer](https://telegra.ph/OFFER-FOR-INFORMATION-SERVICES-03-06)"
    await message.answer(markdown_text, parse_mode=ParseMode.MARKDOWN)


@router_commands.message(F.text == "💡 Support Service")
async def reviews_handler(message: Message, state: FSMContext):
    await message.delete()
    markdown_text = f"[💡 Support Service](t.me/durov)"
    await message.answer(markdown_text, parse_mode=ParseMode.MARKDOWN)
