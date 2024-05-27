import os.path
import random
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime


logger_img_inst_generate = logging.getLogger(__name__)


async def insta_photo_generate(profile_dict):
    background_image_path = os.path.abspath(os.path.join('../images/inst_main.png'))

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
    draw.pieslice([semicircle_center[0] - semicircle_radius, semicircle_center[1] - semicircle_radius, semicircle_center[0] + semicircle_radius, semicircle_center[1] + semicircle_radius], start=0, end=330, fill=0)


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
        os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Medium.otf'))
    font_path_semibold = os.path.abspath(
        os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
    font_path_inter_semibold = os.path.abspath(
        os.path.join('../images/fonts/Inter/static/Inter-SemiBold.ttf'))
    font_path_sf_pro_display = os.path.abspath(
        os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Light.otf'))

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

        text_position = (new_text_position_x, background.size[1] - 960)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

    if profile_dict['profile_name']:
        font_size = 19
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = profile_dict['profile_name']
        text_position = (118, background.size[1] - 798)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 14
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = profile_dict['profile_name']
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
        num = random.randint(2, 9)
        text = f'Active {num}m ago'
        text_position = (742, background.size[1] - 689)
        text_color = (164, 164, 164)
        draw.text(text_position, text, fill=text_color, font=font_sf_pro)
        text_position = (1095, background.size[1] - 689)
        text_color = (164, 164, 164)
        draw.text(text_position, text, fill=text_color, font=font_sf_pro)
        text_position = (1446, background.size[1] - 689)
        text_color = (164, 164, 164)
        draw.text(text_position, text, fill=text_color, font=font_sf_pro)

    # if profile_dict['posts']:
    #     font_numbers_size = 23
    #     font_numbers = ImageFont.truetype(font_path_semibold, font_numbers_size)
    #     text = str(profile_dict['posts'])
    #     text_position = (272, background.size[1] - 887)
    #     text_color = (255, 255, 255)
    #     draw.text(text_position, text, fill=text_color, font=font_numbers)
    #
    # if profile_dict['followers']:
    #     font_numbers_size = 23
    #     font_numbers = ImageFont.truetype(font_path_semibold, font_numbers_size)
    #     text = str(profile_dict['followers'])
    #     text_position = (365, background.size[1] - 887)
    #     text_color = (255, 255, 255)  # Белый
    #     draw.text(text_position, text, fill=text_color, font=font_numbers)
    #
    # if profile_dict['followees']:
    #     font_numbers_size = 23
    #     font_numbers = ImageFont.truetype(font_path_semibold, font_numbers_size)
    #     text = str(profile_dict['followees'])
    #     text_position = (489, background.size[1] - 887)
    #     text_color = (255, 255, 255)
    #     draw.text(text_position, text, fill=text_color, font=font_numbers)

    now = datetime.now()
    current_time = now.strftime("%H:%M")
    formatted_date = now.strftime("%B, %d, %Y")
    font_size = 21
    font = ImageFont.truetype(font_path_semibold, font_size)
    text = current_time
    text_position = (142, background.size[1] - 1018)
    text_color = (255, 255, 255)
    draw.text(text_position, text, fill=text_color, font=font)

    font_size = 16
    font = ImageFont.truetype(font_path_semibold, font_size)
    text = current_time
    text_position = (692, background.size[1] - 746)
    text_color = (255, 255, 255)
    draw.text(text_position, text, fill=text_color, font=font)
    text_position = (1044, background.size[1] - 746)
    draw.text(text_position, text, fill=text_color, font=font)
    text_position = (1395, background.size[1] - 746)
    draw.text(text_position, text, fill=text_color, font=font)

    font_date_size = 80
    font_date = ImageFont.truetype(font_path_inter_semibold, font_date_size)
    text_position = (668, background.size[1] - 1050)
    text_color = (255, 255, 255)
    draw.text(text_position, formatted_date, fill=text_color, font=font_date)

    font_numbers_size = 49
    font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
    num = random.randint(4, 9)
    text = f'{num} disappearing photos'
    text_position = (719, background.size[1] - 947)
    text_color = (255, 255, 255)
    draw.text(text_position, text, fill=text_color, font=font_numbers)

    font_numbers_size = 49
    font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
    text = f'{num-2} photos found'
    text_position = (719, background.size[1] - 873)
    text_color = (255, 255, 255)
    draw.text(text_position, text, fill=text_color, font=font_numbers)


    background.save('res.png', format='PNG')

say_dict = {'username': 'botoev72', 'profile_name': 'Юрий Ботоев', 'link_image': 'https://scontent-fra5-1.xx.fbcdn.net/v/t31.18172-1/13320748_1768112506734471_6426202032361826869_o.jpg?stp=dst-jpg_p480x480&_nc_cat=108&ccb=1-7&_nc_sid=2b6aad&_nc_ohc=M_y2NZYIn_sAX-xS7vW&_nc_ht=scontent-fra5-1.xx&oh=00_AfDrXfXRHcKaNKlRiGKUTemWMO0vuRqFWcO_QexnwmFmKQ&oe=660ED7FC'}

if __name__ == '__main__':
    asyncio.run(insta_photo_generate(say_dict))