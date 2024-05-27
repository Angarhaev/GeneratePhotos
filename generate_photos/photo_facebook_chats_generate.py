import os.path
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime


logger_fb_chats_generate = logging.getLogger(__name__)


async def fb_chats_generate(profile_dict):
    """Функция для генерации картинки чатов фэйсбук с использованием шаблона"""
    if 'username' not in profile_dict or not profile_dict['username']:
        profile_dict['username'] = 'not found'
    if 'profile_name' not in profile_dict or not profile_dict['profile_name']:
        profile_dict['profile_name'] = profile_dict['username']
    try:
        fb_photo_list_objects: list = []
        num_photo_chat = 1
        while num_photo_chat != 4:
            path_inst_chat = f'../searchforphotos/images/fb_notif_{num_photo_chat}.png'
            background_image_path = os.path.abspath(os.path.join(path_inst_chat))

            face_image_url = profile_dict['link_image']

            background = Image.open(background_image_path)

            response = requests.get(face_image_url)
            face = Image.open(BytesIO(response.content))


            face_size = 54
            face = face.resize((face_size, face_size))

            mask = Image.new('L', (face_size, face_size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + (face_size, face_size), fill=255)

            face.putalpha(mask)
            position = (77, 80)
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

            font_size = 26
            font = ImageFont.truetype(font_path_semibold, font_size)
            text = profile_dict['profile_name']
            if len(text) > 17:
                text = text[:17] + '...'
            text_position = (147, background.size[1] - 1193)
            text_color = (255, 255, 255)
            draw.text(text_position, text, fill=text_color, font=font)



            now = datetime.now()
            current_time = now.strftime("%H:%M")
            font_size = 25
            font = ImageFont.truetype(font_path_semibold, font_size)
            text = current_time
            text_position = (49, background.size[1] - 1255)
            text_color = (255, 255, 255)
            draw.text(text_position, text, fill=text_color, font=font)

            output = BytesIO()
            num_photo_chat += 1

            #background.save('res.png', format='PNG')
            background.save(output, format='PNG')
            output.seek(0)  # Reset buffer position to the beginning

            image_png_file_buffer = BufferedInputFile(output.getvalue(), filename=f"image{num_photo_chat}.png")

            logger_fb_chats_generate.info('Картинка сгенерирована')

            fb_photo_list_objects.append(image_png_file_buffer)

        return fb_photo_list_objects
    except Exception:
        return None

# say_dict = {'username': 'shantanova.maria', 'profile_name': 'Maria Shantanova', 'link_image': 'https://scontent-fra5-1.xx.fbcdn.net/v/t39.30808-1/381465036_10162828552227506_7562208141319006202_n.jpg?stp=dst-jpg_p480x480&_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_ohc=Chv7QODo1YgAX9VPK4b&_nc_ht=scontent-fra5-1.xx&oh=00_AfBCXJVSjYkEq9_aWAR0N9hivei-fUiDSxPXuRZkM00JnA&oe=65FDC233', 'link_background': 'https://scontent-fra3-2.xx.fbcdn.net/v/t1.6435-9/101557164_10159645279752506_6369118045322870784_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=y44BV6DmWksAX9VaGw9&_nc_ht=scontent-fra3-2.xx&oh=00_AfD9Vozets0kRAcjluPYLDboJbIcSB639hEXOpEcFY43qQ&oe=6620E13E'}
#
# if __name__ == '__main__':
#     asyncio.run(fb_chats_generate(say_dict))