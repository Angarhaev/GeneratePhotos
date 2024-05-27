import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass


@dataclass
class ConfigData:
    BOT_TOKEN: str
    FACEBOOK_TOKEN: str
    APP_ID_FACEBOOK: str
    APP_SECRET_FACEBOOK: str
    LOGIN_FACEBOOK: str
    PASSWORD_FACEBOOK: str


@dataclass
class RequisitesData:
    PAYPAL: str
    CASHAPP: str
    PAYSEND: str
    PAYEER: str
    SCRILL: str

    BTC: str
    ETH: str
    USDT: str
    BUSD: str
    USDC: str
    DOGECOIN: str
    SOLANA: str
    ETC: str
    POLKADOT: str


async def load_config() -> ConfigData:
    if not find_dotenv():
        exit('переменные окружения не загружены, так как отсутствует файл .env')
    else:
        load_dotenv()
        return ConfigData(
            BOT_TOKEN=os.getenv('BOT_TOKEN'),
            FACEBOOK_TOKEN=os.getenv('FACEBOOK_TOKEN'),
            APP_ID_FACEBOOK=os.getenv('APP_ID_FACEBOOK'),
            APP_SECRET_FACEBOOK=os.getenv('APP_SECRET_FACEBOOK'),
            LOGIN_FACEBOOK=os.getenv('LOGIN_FACEBOOK'),
            PASSWORD_FACEBOOK=os.getenv('PASSWORD_FACEBOOK')
        )


async def load_requisites() -> RequisitesData:
    if not find_dotenv():
        exit('переменные окружения не загружены, так как отсутствует файл .env')
    else:
        load_dotenv()
        return RequisitesData(
            PAYPAL=os.getenv('PAYPAL'),
            CASHAPP=os.getenv('CASHAPP'),
            PAYSEND=os.getenv('PAYSEND'),
            PAYEER=os.getenv('PAYEER'),
            SCRILL=os.getenv('SCRILL'),

            BTC=os.getenv('BTC'),
            ETH=os.getenv('ETH'),
            USDT=os.getenv('USDT'),
            BUSD=os.getenv('BUSD'),
            USDC=os.getenv('USDC'),
            DOGECOIN=os.getenv('DOGECOIN'),
            SOLANA=os.getenv('SOLANA'),
            ETC=os.getenv('ETC'),
            POLKADOT=os.getenv('POLKADOT'),
            )


async def config_initial():
    config = await load_config()
    return config


async def requisites_initial():
    requisites = await load_requisites()
    return requisites
