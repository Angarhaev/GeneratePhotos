import os.path
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime
from math import floor


logger_img_tiktok_generate = logging.getLogger(__name__)


async def tiktok_photo_generate(profile_dict, correspondence, intimate_photos, intimate_videos):
    if 'username' not in profile_dict or not profile_dict['username']:
        profile_dict['username'] = 'not found'
    if 'profile_name' not in profile_dict or not profile_dict['profile_name']:
        profile_dict['profile_name'] = profile_dict['username']
    try:
        background_image_path = os.path.abspath(os.path.join('../searchforphotos/images/tiktok_main1.png'))
        #background_image_path = os.path.abspath(os.path.join('../images/tiktok_main1.png'))

        face_image_url = profile_dict['link_image']

        background = Image.open(background_image_path)

        response = requests.get(face_image_url)
        face_1 = Image.open(BytesIO(response.content))
        face_2 = face_1

        face_size_1 = 108
        face_size_2 = 34
        face_1 = face_1.resize((face_size_1, face_size_1))
        face_2 = face_2.resize((face_size_2, face_size_2))

        mask = Image.new('L', (face_size_1, face_size_1), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_1, face_size_1), fill=255)

        face_1.putalpha(mask)

        mask = Image.new('L', (face_size_2, face_size_2), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_2, face_size_2), fill=255)

        position = (278, 178)
        background.paste(face_1, position, mask=face_1)

        face_2.putalpha(mask)
        position = (730, 372)
        background.paste(face_2, position, mask=face_2)
        position = (1081, 372)
        background.paste(face_2, position, mask=face_2)
        position = (1432, 372)
        background.paste(face_2, position, mask=face_2)


        font_path_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        font_path_inter_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Inter/static/Inter-SemiBold.ttf'))
        font_path_inter_regular = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Inter/static/Inter-Regular.ttf'))
        font_proxima_bold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Proxima Nova (1)/proximanova_bold.otf'))
        font_proxima_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Proxima Nova (1)/ofont.ru_Proxima Nova.ttf'))

        #
        # font_path_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        # font_path_inter_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/Inter/static/Inter-SemiBold.ttf'))
        # font_path_inter_regular = os.path.abspath(
        #     os.path.join('../images/fonts/Inter/static/Inter-Regular.ttf'))
        # font_proxima_bold = os.path.abspath(
        #     os.path.join('../images/fonts/Proxima Nova (1)/proximanova_bold.otf'))
        # font_proxima_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/Proxima Nova (1)/ofont.ru_Proxima Nova.ttf'))


        draw = ImageDraw.Draw(background)


        font_size = 20
        font = ImageFont.truetype(font_proxima_bold, font_size)
        text = profile_dict['profile_name']

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 251
        new_text_position_x = 195 + (area_width - text_width) / 2

        text_position = (new_text_position_x, background.size[1] - 959)
        text_color = (0, 0, 0)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 19
        font = ImageFont.truetype(font_proxima_semibold, font_size)
        text = profile_dict['username']

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 227
        new_text_position_x = 217 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 784)
        text_color = (0, 0, 0)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 14
        font = ImageFont.truetype(font_proxima_bold, font_size)
        text = profile_dict['profile_name']
        if len(text) > 25:
            text = text[:25] + '...'
        text_position = (775, background.size[1] - 700)
        text_color = (0, 0, 0)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1127, background.size[1] - 700)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1478, background.size[1] - 700)
        draw.text(text_position, text, fill=text_color, font=font)

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        formatted_date = now.strftime("%B %d, %Y")
        font_size = 19
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (142, background.size[1] - 1007)
        text_color = (6, 6, 6)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 14
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (693, background.size[1] - 739)
        text_color = (6, 6, 6)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1044, background.size[1] - 739)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1395, background.size[1] - 739)
        draw.text(text_position, text, fill=text_color, font=font)

        font_date_size = 67
        font_date = ImageFont.truetype(font_path_inter_semibold, font_date_size)
        text_position = (668, background.size[1] - 1050)
        text_color = (255, 255, 255)
        draw.text(text_position, formatted_date, fill=text_color, font=font_date)


        font_numbers_size = 18
        font_numbers = ImageFont.truetype(font_proxima_bold, font_numbers_size)

        likes = int(profile_dict['likeCount'])

        if likes >= 1000000000:
            formatted_posts = floor(likes / 100000000) / 10
            text = "{:.1f}B".format(formatted_posts)
        elif likes >= 1000000:
            formatted_posts = floor(likes / 100000) / 10
            text = "{:.1f}M".format(formatted_posts)
        elif likes >= 100000:
            text = f"{round(likes / 1000)}K"
        elif likes >= 10000:
            formatted_posts = floor(likes / 100) / 10
            text = "{:.1f}K".format(formatted_posts)
        else:  # В остальных случаях
            text = str(likes)

        text_color = (0, 0, 0)
        bbox = draw.textbbox((0, 0), text, font=font_numbers)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 50
        new_text_position_x = 408 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 744)
        draw.text(text_position, text, fill=text_color, font=font_numbers)


        followers = int(profile_dict['followers'])

        if followers >= 1000000000:
            formatted_posts = floor(followers / 100000000) / 10
            text = "{:.1f}B".format(formatted_posts)
        elif followers >= 1000000:
            formatted_posts = floor(followers / 100000) / 10
            text = "{:.1f}M".format(formatted_posts)
        elif followers >= 100000:
            text = f"{round(followers / 1000)}K"
        elif followers >= 10000:
            formatted_posts = floor(followers / 100) / 10
            text = "{:.1f}K".format(formatted_posts)
        else:  # В остальных случаях
            text = str(followers)

        bbox = draw.textbbox((0, 0), text, font=font_numbers)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 50
        new_text_position_x = 306 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 744)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        followees = int(profile_dict['followees'])

        if followees >= 1000000:
            formatted_posts = floor(followees / 100000) / 10
            text = "{:.1f}M".format(formatted_posts)
        elif followees >= 100000:
            text = f"{round(followees / 1000)}K"
        elif followees >= 10000:
            formatted_posts = floor(followees / 100) / 10
            text = "{:.1f}K".format(formatted_posts)
        else:  # В остальных случаях
            text = str(followees)

        bbox = draw.textbbox((0, 0), text, font=font_numbers)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 50
        new_text_position_x = 205 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 744)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 41
        font_numbers = ImageFont.truetype(font_path_inter_regular, font_numbers_size)
        text = f'{correspondence} correspondence'
        text_position = (719, background.size[1] - 962)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers = ImageFont.truetype(font_path_inter_regular, font_numbers_size)
        text = f'{intimate_photos} intimate photos'
        text_position = (719, background.size[1] - 899)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers = ImageFont.truetype(font_path_inter_regular, font_numbers_size)
        text = f'{intimate_videos} intimate videos'
        text_position = (719, background.size[1] - 831)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        #background.save("tiktok_main.png", format='PNG')

        output = BytesIO()
        background.save(output, format='PNG')
        output.seek(0)

        image_png_file_buffer = BufferedInputFile(output.getvalue(), filename="image.png")

        logger_img_tiktok_generate.info('Картинка сгенерирована')

        return image_png_file_buffer
    except Exception:
        logger_img_tiktok_generate.info('Не удалось сгенерировать тикток фото')


# say_dict = {'profile_name': 'Alexandr', 'username': 'alek.andr', 'link_image': 'https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/dfa23fc652ab71aa3efcbeb82133a38a.jpeg?lk3s=a5d48078&x-expires=1711206000&amp;x-signature=4eLEcd5yFCjJmE8GyRUHccNGPww%3D', 'followers': 523400005, 'followees': 10256000, 'likeCount': 1500000000, 'url': 'https://tiktok.com/@alek.andr'}
#
#
# if __name__ == '__main__':
#     asyncio.run(tiktok_photo_generate(say_dict, 32, 23, 7))
