import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums.parse_mode import ParseMode
from aiogram.types import Message
from config_data.config import config_initial, requisites_initial
from handlers import routers
from keyboards import KeyboardsCreate
from middlewares import KeyboardsMiddleware, RequisitesMiddleware, ConfigMiddleware


storage = MemoryStorage()
logger = logging.getLogger(__name__)

log_format = ('%(filename)s:%(lineno)d #%(levelname)-8s'
              '[%(asctime)s] - %(name)s - %(message)s')


async def load() -> None:
    logging.basicConfig(
        level=logging.INFO, format=log_format)

    """Инициализация бота и диспетчера"""
    config = await config_initial()
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=storage)

    for i_router in routers:
        dp.include_router(i_router)


    keyboards_instance = await KeyboardsCreate.initialize()
    dp.message.middleware(KeyboardsMiddleware(keyboards_instance))
    dp.callback_query.middleware(KeyboardsMiddleware(keyboards_instance))

    requisites = await requisites_initial()
    dp.message.middleware(RequisitesMiddleware(requisites))
    dp.callback_query.middleware(RequisitesMiddleware(requisites))

    dp.message.middleware(ConfigMiddleware(config))
    dp.callback_query.middleware(ConfigMiddleware(config))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
