import requests
import asyncio
import re
import logging


logger_tik_tok_generate = logging.getLogger(__name__)


async def get_user_data_tiktok(url_tiktok):
    try:
        username = None
        if url_tiktok.startswith('@'):
            url_tiktok = f"https://tiktok.com/{url_tiktok}"

        if url_tiktok.startswith('https'):
            username_regex = r'https?://(?:www\.)?tiktok\.com/@([a-zA-Z0-9_.]+)'
        elif url_tiktok.startswith('www.tiktok.com/'):
            username_regex = r'www\.tiktok\.com/@([a-zA-Z0-9_.]+)'
        else:
            username_regex = r'@([a-zA-Z0-9_.]+)'

        # Извлечение юзернейма
        match = re.match(username_regex, url_tiktok)
        if match:
            username = f'@{match.group(1)}'

        url = f"https://tiktok.livecounts.io/user/data/{username}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Referer": "https://tokcount.com/",
            "Origin": "https://tokcount.com"
        }

        dates = requests.get(url, headers=headers)

        user_id = dates.json().get("userId")

        url = f"https://tiktok.livecounts.io/user/stats/{user_id}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Referer": "https://tokcount.com/",
            "Origin": "https://tokcount.com"
        }

        response = requests.get(url, headers=headers)

        info_user: dict = {
            'profile_name': dates.json()['username'],
            'username': username,
            'link_image': dates.json()['avatar'],
            'followers': response.json()['followerCount'],
            'followees': response.json()['followingCount'],
            'likeCount': response.json()['likeCount'],
            'link_profile': url_tiktok
        }

        print(info_user)

        return info_user
    except Exception:
        logger_tik_tok_generate.info('Не удалось извлечь данные тикток')

# if __name__ == '__main__':
#     asyncio.run(get_user_data_tiktok('www.tiktok.com/@alek.andr'))
