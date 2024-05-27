import os.path
import random
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime
from math import floor

logger_img_inst_generate = logging.getLogger(__name__)


async def insta_photo_generate(profile_dict, correspondence, intimate_photos, intimate_video, active_ago):
    """Функция для генерации главной картинки инстаграм с использованием шаблона"""
    if 'username' not in profile_dict or not profile_dict['username']:
        profile_dict['username'] = 'not found'
    if 'profile_name' not in profile_dict or not profile_dict['profile_name']:
        profile_dict['profile_name'] = profile_dict['username']
    try:
        background_image_path = os.path.abspath(os.path.join('../searchforphotos/images/inst_main.png'))
        # background_image_path = os.path.abspath(os.path.join('../images/inst_main.png'))
        face_image_url = profile_dict['link_image']

        background = Image.open(background_image_path)

        response = requests.get(face_image_url)
        face_1 = Image.open(BytesIO(response.content))
        face_2 = face_1

        face_size_1 = 103
        face_size_2 = 29
        face_1 = face_1.resize((face_size_1, face_size_1))
        face_2 = face_2.resize((face_size_2, face_size_2))

        mask = Image.new('L', (face_size_1, face_size_1), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_1, face_size_1), fill=255)

        face_1.putalpha(mask)

        mask = Image.new('L', (face_size_2, face_size_2), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_2, face_size_2), fill=255)

        semicircle_radius = face_size_2 // 5
        semicircle_center = (face_size_2 - semicircle_radius * 0.6, face_size_2 - semicircle_radius * 1.3)
        draw.pieslice([semicircle_center[0] - semicircle_radius, semicircle_center[1] - semicircle_radius,
                       semicircle_center[0] + semicircle_radius, semicircle_center[1] + semicircle_radius], start=0,
                      end=330, fill=0)

        position = (117, 166)
        background.paste(face_1, position, mask=face_1)

        face_2.putalpha(mask)
        position = (704, 373)
        background.paste(face_2, position, mask=face_2)
        position = (1055, 373)
        background.paste(face_2, position, mask=face_2)
        position = (1406, 373)
        background.paste(face_2, position, mask=face_2)

        font_path_medium = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Medium.otf'))
        font_path_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        font_path_inter_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Inter/static/Inter-SemiBold.ttf'))
        font_path_sf_pro_display = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Light.otf'))

        # font_path_medium = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Medium.otf'))
        # font_path_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        # font_path_inter_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/Inter/static/Inter-SemiBold.ttf'))
        # font_path_sf_pro_display = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Light.otf'))

        draw = ImageDraw.Draw(background)

        if profile_dict['username']:
            font_size = 20
            font = ImageFont.truetype(font_path_medium, font_size)
            text = profile_dict['username']

            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            area_width = 250
            new_text_position_x = 198 + (area_width - text_width) / 2

            text_position = (new_text_position_x, background.size[1] - 957)
            text_color = (255, 255, 255)
            draw.text(text_position, text, fill=text_color, font=font)

        if profile_dict['profile_name']:
            font_size = 19
            font = ImageFont.truetype(font_path_semibold, font_size)
            text = profile_dict['profile_name']
            text_position = (118, background.size[1] - 799)
            text_color = (255, 255, 255)
            draw.text(text_position, text, fill=text_color, font=font)

            font_size = 13
            font = ImageFont.truetype(font_path_semibold, font_size)
            text = profile_dict['profile_name']
            if len(text) > 25:
                text = text[:25]
            text_position = (743, background.size[1] - 707)
            text_color = (250, 250, 250)
            draw.text(text_position, text, fill=text_color, font=font)
            text_position = (1095, background.size[1] - 707)
            text_color = (250, 250, 250)
            draw.text(text_position, text, fill=text_color, font=font)
            text_position = (1446, background.size[1] - 707)
            text_color = (250, 250, 250)
            draw.text(text_position, text, fill=text_color, font=font)

            font_size = 11
            font_sf_pro = ImageFont.truetype(font_path_sf_pro_display, font_size)
            text = f'Active {active_ago}m ago'
            text_position = (742, background.size[1] - 691)
            text_color = (164, 164, 164)
            draw.text(text_position, text, fill=text_color, font=font_sf_pro)
            text_position = (1095, background.size[1] - 691)
            text_color = (164, 164, 164)
            draw.text(text_position, text, fill=text_color, font=font_sf_pro)
            text_position = (1446, background.size[1] - 691)
            text_color = (164, 164, 164)
            draw.text(text_position, text, fill=text_color, font=font_sf_pro)

        if profile_dict['posts']:
            font_numbers_size = 23
            font_numbers = ImageFont.truetype(font_path_semibold, font_numbers_size)

            posts = int(profile_dict['posts'])

            if posts >= 1000000:
                formatted_posts = floor(posts / 100000) / 10
                text = "{:.1f}M".format(formatted_posts)
            elif posts >= 100000:
                text = f"{round(posts / 1000)}K"
            elif posts >= 10000:
                formatted_posts = floor(posts / 100) / 10
                text = "{:.1f}K".format(formatted_posts)
            else:  # В остальных случаях
                text = str(posts)

            text_color = (255, 255, 255)
            bbox = draw.textbbox((0, 0), text, font=font_numbers)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            area_width = 50
            new_text_position_x = 267 + (area_width - text_width) / 2
            text_position = (new_text_position_x, background.size[1] - 887)
            draw.text(text_position, text, fill=text_color, font=font_numbers)

        if profile_dict['followers']:
            font_numbers_size = 23
            font_numbers = ImageFont.truetype(font_path_semibold, font_numbers_size)
            followers = int(profile_dict['followers'])

            if followers >= 1000000:
                formatted_posts = floor(followers / 100000) / 10
                text = "{:.1f}M".format(formatted_posts)
            elif followers >= 100000:
                text = f"{round(followers / 1000)}K"
            elif followers >= 10000:
                formatted_posts = floor(followers / 100) / 10
                text = "{:.1f}K".format(formatted_posts)
            else:  # В остальных случаях
                text = str(followers)

            text_color = (255, 255, 255)
            bbox = draw.textbbox((0, 0), text, font=font_numbers)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            area_width = 50
            new_text_position_x = 369 + (area_width - text_width) / 2
            text_position = (new_text_position_x, background.size[1] - 887)
            draw.text(text_position, text, fill=text_color, font=font_numbers)


        if profile_dict['followees']:
            font_numbers_size = 23
            font_numbers = ImageFont.truetype(font_path_semibold, font_numbers_size)
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

            text_color = (255, 255, 255)
            bbox = draw.textbbox((0, 0), text, font=font_numbers)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            area_width = 50
            new_text_position_x = 484 + (area_width - text_width) / 2
            text_position = (new_text_position_x, background.size[1] - 887)
            draw.text(text_position, text, fill=text_color, font=font_numbers)

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        formatted_date = now.strftime("%B %d, %Y")
        font_size = 21
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (138, background.size[1] - 1017)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 16
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (689, background.size[1] - 746)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1041, background.size[1] - 746)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1391, background.size[1] - 746)
        draw.text(text_position, text, fill=text_color, font=font)

        font_date_size = 67
        font_date = ImageFont.truetype(font_path_inter_semibold, font_date_size)
        text_position = (666, background.size[1] - 1050)
        text_color = (255, 255, 255)
        draw.text(text_position, formatted_date, fill=text_color, font=font_date)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
        num = random.randint(4, 9)
        text = f'{correspondence} correspondence'
        text_position = (719, background.size[1] - 959)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
        text = f'{intimate_photos} intimate photos'
        text_position = (719, background.size[1] - 896)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
        text = f'{intimate_video} intimate videos'
        text_position = (719, background.size[1] - 833)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        # background.save('res.png', format='PNG')

        output = BytesIO()

        background.save(output, format='PNG')
        output.seek(0)

        image_png_file_buffer = BufferedInputFile(output.getvalue(), filename="image.png")

        logger_img_inst_generate.info('Картинка сгенерирована')

        return image_png_file_buffer
    except Exception:
        logger_img_inst_generate.info('Не удалось сгенерировать фото инстаграм')
        return None

# say_dict = {'followees':  '324', 'followers':  '39709002', 'posts':  '853', 'username': 'shantanova.maria', 'profile_name': 'Илон Маск/Elon Musk: SpaceX, Tesla, Solar City', 'link_image': 'https://scontent-fra5-1.xx.fbcdn.net/v/t39.30808-1/381465036_10162828552227506_7562208141319006202_n.jpg?stp=dst-jpg_p480x480&_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_ohc=Chv7QODo1YgAX9VPK4b&_nc_ht=scontent-fra5-1.xx&oh=00_AfBCXJVSjYkEq9_aWAR0N9hivei-fUiDSxPXuRZkM00JnA&oe=65FDC233', 'link_background': 'https://scontent-fra3-2.xx.fbcdn.net/v/t1.6435-9/101557164_10159645279752506_6369118045322870784_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=y44BV6DmWksAX9VaGw9&_nc_ht=scontent-fra3-2.xx&oh=00_AfD9Vozets0kRAcjluPYLDboJbIcSB639hEXOpEcFY43qQ&oe=6620E13E'}
#
# if __name__ == '__main__':
#     asyncio.run(insta_photo_generate(say_dict, 14, 32, 9))
