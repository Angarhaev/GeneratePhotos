import asyncio
import instaloader
import re
import logging

logeer_inst = logging.getLogger(__name__)

L = instaloader.Instaloader()


async def extract_username(url):
    pattern = re.compile(r"(?:https?:\/\/)?(?:www\.)?instagram\.com\/([^\/?]+)")
    match = pattern.search(url)
    if match:
        username = match.group(1)
        return username
    else:
        return None


async def insta_info(link):
    try:
        user_name = await extract_username(link)
        if user_name:
            profile = instaloader.Profile.from_username(L.context, user_name)
            info_dict = {
                'username': profile.username,
                'profile_name': profile.full_name,
                'link_image': profile.profile_pic_url,
                'followers': profile.followers,
                'followees': profile.followees,
                'posts': profile.get_posts().count,
                'url': profile.external_url,
            }

            if info_dict['profile_name'] == '':
                info_dict['profile_name'] = info_dict['username']

            logeer_inst.info('Данные из инстаграма получены')
            # print(info_dict)
            return info_dict
        else:
            raise AttributeError
    except AttributeError as exc:
        logeer_inst.info('Данные из инстаграма получить не удалось')
        return None

# if __name__ == '__main__':
#     asyncio.run(insta_info('https://www.instagram.com/erzhenaj/'))