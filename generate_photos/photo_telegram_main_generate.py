import os.path
import random
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime


logger_img_tg_generate = logging.getLogger(__name__)


async def telegram_photo_generate(profile_dict, correspondence, intimate_photo, intimate_video):
    if 'username' not in profile_dict or not profile_dict['username']:
        profile_dict['username'] = 'not found'
    if 'profile_name' not in profile_dict or not profile_dict['profile_name']:
        profile_dict['profile_name'] = profile_dict['username']

    try:

        background_image_path = os.path.abspath(os.path.join('../searchforphotos/images/telegram_main.png'))
        #background_image_path = os.path.abspath(os.path.join('../images/telegram_main.png'))

        face_image_url = profile_dict['link_image']

        background = Image.open(background_image_path)

        response = requests.get(face_image_url)
        face_1 = Image.open(BytesIO(response.content))
        face_2 = face_1

        face_size_1 = 109
        face_size_2 = 33
        face_1 = face_1.resize((face_size_1, face_size_1))
        face_2 = face_2.resize((face_size_2, face_size_2))

        mask = Image.new('L', (face_size_1, face_size_1), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_1, face_size_1), fill=255)

        face_1.putalpha(mask)

        mask = Image.new('L', (face_size_2, face_size_2), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_2, face_size_2), fill=255)

        position = (277, 130)
        background.paste(face_1, position, mask=face_1)

        face_2.putalpha(mask)
        position = (959, 366)
        background.paste(face_2, position, mask=face_2)
        position = (1310, 366)
        background.paste(face_2, position, mask=face_2)
        position = (1661, 366)
        background.paste(face_2, position, mask=face_2)

        font_path_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        font_path_regular = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Regular.otf'))
        font_path_inter_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Inter/static/Inter-SemiBold.ttf'))

        # font_path_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        # font_path_regular = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Regular.otf'))
        # font_path_inter_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/Inter/static/Inter-SemiBold.ttf'))


        draw = ImageDraw.Draw(background)

        font_size = 20
        font = ImageFont.truetype(font_path_regular, font_size)
        text = f"@{profile_dict['username']}"
        text_position = (140, background.size[1] - 619)
        text_color = (85, 135, 198)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 28
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = profile_dict['profile_name']
        if len(text) > 26:
            text = text[:26]
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 250
        new_text_position_x = 205 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 830)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 14
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = profile_dict['profile_name']
        if len(text) > 26:
            text = text[:26]
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 150
        new_text_position_x = 754 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 707)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        new_text_position_x = 1105 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 707)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        new_text_position_x = 1457 + (area_width - text_width) / 2
        text_position = (new_text_position_x, background.size[1] - 707)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        formatted_date = now.strftime("%B %d, %Y")
        font_size = 20
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (143, background.size[1] - 1009)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 15
        font = ImageFont.truetype(font_path_semibold, font_size)
        text = current_time
        text_position = (694, background.size[1] - 744)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1046, background.size[1] - 744)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1397, background.size[1] - 744)
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
        text_position = (719, background.size[1] - 968)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
        text = f'{intimate_photo} intimate photos'
        text_position = (719, background.size[1] - 903)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_semibold, font_numbers_size)
        text = f'{intimate_video} intimate videos'
        text_position = (719, background.size[1] - 840)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        #background.save('telegram.png', format='PNG')

        logger_img_tg_generate.info('Картинка сгенерирована')

        output = BytesIO()

        background.save(output, format='PNG')
        output.seek(0)

        image_png_file_buffer = BufferedInputFile(output.getvalue(), filename="image.png")

        logger_img_tg_generate.info('Картинка сгенерирована')

        return image_png_file_buffer

    except Exception:
        logger_img_tg_generate.info('Не удалось сгенерировать фото телеграм')
        return None

# say_dict = {'username': 'shantanova.maria', 'profile_name': 'Илон Маск/Elon Musk: SpaceX, Tesla, Solar City', 'link_image': 'https://scontent-fra5-1.xx.fbcdn.net/v/t39.30808-1/381465036_10162828552227506_7562208141319006202_n.jpg?stp=dst-jpg_p480x480&_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_ohc=Chv7QODo1YgAX9VPK4b&_nc_ht=scontent-fra5-1.xx&oh=00_AfBCXJVSjYkEq9_aWAR0N9hivei-fUiDSxPXuRZkM00JnA&oe=65FDC233', 'link_background': 'https://scontent-fra3-2.xx.fbcdn.net/v/t1.6435-9/101557164_10159645279752506_6369118045322870784_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=y44BV6DmWksAX9VaGw9&_nc_ht=scontent-fra3-2.xx&oh=00_AfD9Vozets0kRAcjluPYLDboJbIcSB639hEXOpEcFY43qQ&oe=6620E13E'}
#
# if __name__ == '__main__':
#     asyncio.run(telegram_photo_generate(say_dict, 14, 32, 9))