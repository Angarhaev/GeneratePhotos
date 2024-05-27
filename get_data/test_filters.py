import re

url_tiktok = 'www.tiktok.com/@milanka_nekrasova.0'

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
    print(username)