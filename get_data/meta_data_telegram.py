import httpx
from bs4 import BeautifulSoup
import logging
import re


logeer_meta_data = logging.getLogger(__name__)


async def telegram_get_data(url: str) -> dict:
    """Асинхронно извлекает данные Open Graph из заданного URL, следуя за перенаправлениями."""
    try:
        async with httpx.AsyncClient(follow_redirects=True) as client:
            username = None
            if url.startswith('@'):
                username = url[1:]

            if url.startswith('https'):
                username_regex = r'https?://t\.me/([a-zA-Z0-9_]+)'
            elif url.startswith('t.me/'):
                username_regex = r't\.me/([a-zA-Z0-9_]+)'
            else:
                username_regex = r'@([a-zA-Z0-9_]+)'

            # Извлечение юзернейма
            match = re.match(username_regex, url)
            if match:
                username = match.group(1)

            url = f"https://t.me/{username}"

            response = await client.get(url)
            response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        og_tags = soup.find_all('meta', property=lambda prop: prop and prop.startswith('og:'))
        #logeer_meta_data.info('Теги:', og_tags)

        og_data = {tag['property']: tag['content'] for tag in og_tags if tag.get('content')}
        #logeer_meta_data.info(f'Данные из метаданных: {og_data}')

        og_title = soup.find('meta', property='og:title')
        og_image = soup.find('meta', property='og:image')
        if og_title and og_image:
            profile_name = og_title['content']
            link_image = og_image['content']
            logeer_meta_data.info('Данные получены через метаданные')
            return {
                'profile_name': profile_name,
                'link_image': link_image,
                'username': username,
                'link_profile': url
            }
        else:
            logeer_meta_data.info('Не удалось получить через метаданные')
            return None
    except httpx.HTTPStatusError as http_err:
        logeer_meta_data.info(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logeer_meta_data.info(f"An error occurred: {err}")

    return {'error': 'An error occurred while retrieving data. Please check the link and try again'}
