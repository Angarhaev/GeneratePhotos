import os.path
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime


logger_img_fb_generate = logging.getLogger(__name__)


async def facebook_photo_generate(profile_dict, correspondence, intimate_photo, intimate_video):
    """Функция для генерации главной фотографии для фэйсбук"""
    if 'username' not in profile_dict or not profile_dict['username']:
        profile_dict['username'] = 'not found'
    if 'profile_name' not in profile_dict or not profile_dict['profile_name']:
        profile_dict['profile_name'] = profile_dict['username']
    try:
        background_image_path = os.path.abspath(os.path.join('../searchforphotos/images/fb_main.png'))
        #background_image_path = os.path.abspath(os.path.join('../images/fb_main.png'))
        facebook_background_url = profile_dict['link_background']
        face_image_url = profile_dict['link_image']

        background = Image.open(background_image_path)

        response_fb_bg = requests.get(facebook_background_url)
        facebook_background = Image.open(BytesIO(response_fb_bg.content))

        width, height = facebook_background.size
        crop_rectangle = (49, height // 6.5, width, height // 1.2)
        cropped_image = facebook_background.crop(crop_rectangle)

        width, height = 456, 258

        fb_bg = cropped_image.resize((width, height))
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        draw.rectangle((0, 0) + (width, height), fill=255)
        fb_bg.putalpha(mask)
        position = (104, 162)
        background.paste(fb_bg, position, mask=fb_bg)

        response = requests.get(face_image_url)
        face_1 = Image.open(BytesIO(response.content))
        face_2 = face_1

        face_size_1 = 197
        face_1 = face_1.resize((face_size_1, face_size_1))

        mask = Image.new('L', (face_size_1, face_size_1), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_1, face_size_1), fill=255)

        face_1.putalpha(mask)

        border_size = 5
        border_color = (255, 255, 255)
        new_size = (face_size_1 + border_size * 2, face_size_1 + border_size * 2)
        border_image = Image.new('RGBA', new_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(border_image)
        draw.ellipse((0, 0, new_size[0], new_size[1]), fill=(255, 255, 255))
        border_image.paste(face_1, (border_size, border_size), mask=face_1)

        position = (115, 264)
        background.paste(border_image, position, mask=border_image)

        face_size_2 = 31
        face_2 = face_2.resize((face_size_2, face_size_2))
        mask = Image.new('L', (face_size_2, face_size_2), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + (face_size_2, face_size_2), fill=255)

        face_2.putalpha(mask)
        position = (709, 369)
        background.paste(face_2, position, mask=face_2)
        position = (1060, 369)
        background.paste(face_2, position, mask=face_2)
        position = (1411, 369)
        background.paste(face_2, position, mask=face_2)

        font_path_sf_pro_medium = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Medium.otf'))
        font_path_sf_pro_semibold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        font_path_sf_pro_regular= os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Regular.otf'))
        font_path_inter_medium = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/Inter/static/Inter-Medium.ttf'))
        font_path_sf_pro_display_bold = os.path.abspath(
            os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Bold.otf'))

        # font_path_sf_pro_medium = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Medium.otf'))
        # font_path_sf_pro_semibold = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
        # font_path_sf_pro_regular = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Regular.otf'))
        # font_path_inter_medium = os.path.abspath(
        #     os.path.join('../images/fonts/Inter/static/Inter-Medium.ttf'))
        # font_path_sf_pro_display_bold = os.path.abspath(
        #     os.path.join('../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Bold.otf'))

        draw = ImageDraw.Draw(background)

        font_size = 20
        font = ImageFont.truetype(font_path_sf_pro_display_bold, font_size)
        text = profile_dict['username']

        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        area_width = 250
        new_text_position_x = 198 + (area_width - text_width) / 2

        text_position = (new_text_position_x, background.size[1] - 959)
        text_color = (0, 0, 0)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 28
        font = ImageFont.truetype(font_path_sf_pro_display_bold, font_size)
        text = profile_dict['profile_name']

        if len(text) > 28:
            text1 = text[:28]
            text2 = text[28:]
            text2 = text2.lstrip()


            text_position1 = (122, background.size[1] - 595)
            text_position2 = (122, background.size[1] - 595 + 30)

            draw.text(text_position1, text1, fill=text_color, font=font)
            draw.text(text_position2, text2, fill=text_color, font=font)

        else:
            text_position = (122, background.size[1] - 595)
            draw.text(text_position, text, fill=text_color, font=font)

        font_size = 15
        font = ImageFont.truetype(font_path_sf_pro_semibold, font_size)
        text = profile_dict['profile_name']
        if len(text) > 17:
            text = text[:17] + '...'
        text_position = (748, background.size[1] - 705)
        text_color = (253, 253, 253)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1099, background.size[1] - 705)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1450, background.size[1] - 705)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 17
        font = ImageFont.truetype(font_path_sf_pro_regular, font_size)
        text = 'Data not found'  # profile_dict['profile_name']
        text_position = (125, background.size[1] - 532)
        text_color = (94, 94, 94)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 19
        font = ImageFont.truetype(font_path_sf_pro_medium, font_size)
        text = 'Data not found'  # profile_dict['profile_name']
        text_position = (158, background.size[1] - 289)
        text_color = (5, 5, 5)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (158, background.size[1] - 240)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (158, background.size[1] - 193)
        draw.text(text_position, text, fill=text_color, font=font)

        now = datetime.now()
        current_time = now.strftime("%H:%M")
        formatted_date = now.strftime("%B %d, %Y")
        font_size = 19
        font = ImageFont.truetype(font_path_sf_pro_semibold, font_size)
        text = current_time
        text_position = (142, background.size[1] - 1015)
        text_color = (6, 6, 6)
        draw.text(text_position, text, fill=text_color, font=font)

        font_size = 15
        font = ImageFont.truetype(font_path_sf_pro_semibold, font_size)
        text = current_time
        text_position = (692, background.size[1] - 743)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1044, background.size[1] - 743)
        draw.text(text_position, text, fill=text_color, font=font)
        text_position = (1395, background.size[1] - 743)
        draw.text(text_position, text, fill=text_color, font=font)

        font_date_size = 67
        font_date = ImageFont.truetype(font_path_inter_medium, font_date_size)
        text_position = (666, background.size[1] - 1050)
        text_color = (255, 255, 255)
        draw.text(text_position, formatted_date, fill=text_color, font=font_date)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_medium, font_numbers_size)
        num = random.randint(4, 9)
        text = f'{correspondence} correspondence'
        text_position = (719, background.size[1] - 959)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_medium, font_numbers_size)
        text = f'{intimate_photo} intimate photos'
        text_position = (719, background.size[1] - 895)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        font_numbers_size = 40
        font_numbers = ImageFont.truetype(font_path_inter_medium, font_numbers_size)
        text = f'{intimate_video} intimate videos'
        text_position = (719, background.size[1] - 832)
        text_color = (255, 255, 255)
        draw.text(text_position, text, fill=text_color, font=font_numbers)

        #background.save('facebook.png', format='PNG')
        output = BytesIO()

        background.save(output, format='PNG')
        output.seek(0)

        image_png_file_buffer = BufferedInputFile(output.getvalue(), filename="image.png")

        logger_img_fb_generate.info('Картинка сгенерирована')

        return image_png_file_buffer
    except Exception:
        logger_img_fb_generate.info('Не удалось сгенерировать картинку для фэйсбук')
        return None

# say_dict = {'username': 'shantanova.maria', 'profile_name': 'Илон Маск/Elon Musk: SpaceX, Tesla, Solar City', 'link_image': 'https://scontent-fra5-1.xx.fbcdn.net/v/t39.30808-1/381465036_10162828552227506_7562208141319006202_n.jpg?stp=dst-jpg_p480x480&_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_ohc=Chv7QODo1YgAX9VPK4b&_nc_ht=scontent-fra5-1.xx&oh=00_AfBCXJVSjYkEq9_aWAR0N9hivei-fUiDSxPXuRZkM00JnA&oe=65FDC233', 'link_background': 'https://scontent-fra3-2.xx.fbcdn.net/v/t1.6435-9/101557164_10159645279752506_6369118045322870784_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=y44BV6DmWksAX9VaGw9&_nc_ht=scontent-fra3-2.xx&oh=00_AfD9Vozets0kRAcjluPYLDboJbIcSB639hEXOpEcFY43qQ&oe=6620E13E'}
#
# if __name__ == '__main__':
#     asyncio.run(facebook_photo_generate(say_dict, 14, 32, 9))