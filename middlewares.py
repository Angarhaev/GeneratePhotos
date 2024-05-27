from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
from keyboards import KeyboardsCreate
from config_data.config import requisites_initial, config_initial


class KeyboardsMiddleware(BaseMiddleware):
    def __init__(self, keyboards_instance: KeyboardsCreate) -> None:
        self.keyboards_instance = keyboards_instance

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data['keyboards_instance'] = self.keyboards_instance
        return await handler(event, data)


class RequisitesMiddleware(BaseMiddleware):
    def __init__(self, requisites: requisites_initial()) -> None:
        self.requisites = requisites

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data['requisites'] = self.requisites
        return await handler(event, data)


class ConfigMiddleware(BaseMiddleware):
    def __init__(self, config: config_initial()) -> None:
        self.config = config

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data['config'] = self.config
        return await handler(event, data)

