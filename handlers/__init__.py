from .start_handler import router
from .change_social_handler import router_social
from .instagram_link_handler import router_instagram
from .facebook_link_handler import router_facebook
from .telegram_link_handler import router_telegram
from .tiktok_link_handler import router_tiktok
from .pay_handler import router_pay
from .commands_handler import router_commands

routers = (router, router_social, router_instagram, router_facebook, router_telegram, router_tiktok, router_pay, router_commands)