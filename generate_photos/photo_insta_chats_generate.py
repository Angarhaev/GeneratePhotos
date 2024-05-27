import os.path
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime


logger_img_inst_chats_generate = logging.getLogger(__name__)


async def insta_chats_generate(profile_dict, active_ago):
    """Функция для генерации картинки чатов инстаграм с использованием шаблона"""
    inst_photo_list_objects: list = []
    num_photo_chat = 1
    while num_photo_chat != 4:
        path_inst_chat = f'../searchforphotos/images/inst_chat{num_photo_chat}.png'
        background_image_path = os.path.abspath(os.path.join(path_inst_chat))

        face_image_url = profile_dict['link_image']

        background = Image.open(background_image_path)

        response = requests.get(face_image_url)
        face = Image.open(BytesIO(response.content))


        face_size = 52
        face = face.resize((face_size, face_size))

        mask = Image.new('L', (face_size, face_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size, face_size), fill=255)


        semicircle_radius = face_size // 5
        semicircle_center = (face_size - semicircle_radius * 0.6, face_size - semicircle_radius * 1.3)
        draw.pieslice([semicircle_center[0] - semicircle_radius, semicircle_center[1] - semicircle_radius, semicircle_center[0] + semicircle_radius, semicircle_center[1] + semicircle_radius], start=0, end=330, fill=0)

        face.putalpha(mask)
        position = (70, 88)
        background.paste(face, position, mask=face)

        font_path_medium = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Medium.otf'))
        font_path_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        font_path_inter_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Inter/static/Inter-SemiBold.ttf'))
        font_path_sf_pro_display = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Light.otf'))

        draw = ImageDraw.Draw(background)

        if profile_dict['profile_name']:
            font_size = 23
            font = ImageFont.truetype(font_path_medium, font_size)
            text = profile_dict['profile_name']
            if len(text) > 26:
                text = text[:26]
            text_position = (134, background.size[1] - 1194)
            text_color = (255, 255, 255)
            draw.text(text_position, text, fill=text_color, font=font)

            font_size = 17
            font_sf_pro = ImageFont.truetype(font_path_sf_pro_display, font_size)
            text = f'Active {active_ago}m ago'
            text_position = (134, background.size[1] - 1162)
            text_color = (164, 164, 164)
            draw.text(text_position, text, fill=text_color, font=font_sf_pro)

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        font_size = 24
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (50, background.size[1] - 1256)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        output = BytesIO()
        # background.save(f'result{num_photo_chat}.png')
        num_photo_chat += 1
        background.save(output, format='PNG')
        output.seek(0)  # Reset buffer position to the beginning

        image_png_file_buffer = BufferedInputFile(output.getvalue(), filename=f"image{num_photo_chat}.png")

        logger_img_inst_chats_generate.info('Картинка сгенерирована')

        inst_photo_list_objects.append(image_png_file_buffer)

    return inst_photo_list_objects

# say_dict = {'username': 'erzhenaj', 'profile_name': 'Eri Dambaeva', 'link_image': 'https://scontent-fra5-2.cdninstagram.com/v/t51.2885-19/280027843_341905847928429_2417817810769814749_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-fra5-2.cdninstagram.com&_nc_cat=109&_nc_ohc=sxlifHIe4GgAX_yXazL&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfDC7S37B3601PTldebzEBnOK4B9wP1_EaldGRjLMRF0jw&oe=65EA1807&_nc_sid=8b3546', 'followers': 448, 'followees': 198, 'posts': 191, 'url': 'https://vk.com/eri_d'}
