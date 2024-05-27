import os.path
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
from aiogram.types.input_file import BufferedInputFile
import logging
import asyncio
from datetime import datetime


logger_tiktok_chats_generate = logging.getLogger(__name__)


async def tiktok_chats_generate(profile_dict):
    """Функция для генерации картинки чатов тикток с использованием шаблона"""
    if 'username' not in profile_dict or not profile_dict['username']:
        profile_dict['username'] = 'not found'
    if 'profile_name' not in profile_dict or not profile_dict['profile_name']:
        profile_dict['profile_name'] = profile_dict['username']
    try:
        tg_photo_list_objects: list = []
        num_photo_chat = 1
        while num_photo_chat != 4:
            path_inst_chat = f'../searchforphotos/images/tiktok_chat{num_photo_chat}.png'
            #path_inst_chat = f'../images/tiktok_chat1.png'
            background_image_path = os.path.abspath(os.path.join(path_inst_chat))

            face_image_url = profile_dict['link_image']

            background = Image.open(background_image_path)

            response = requests.get(face_image_url)
            face = Image.open(BytesIO(response.content))

            face_size = 64
            face = face.resize((face_size, face_size))

            mask = Image.new('L', (face_size, face_size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + (face_size, face_size), fill=255)

            face.putalpha(mask)
            position = (114, 76)
            background.paste(face, position, mask=face)

            font_path_semibold = os.path.abspath(
                os.path.join('../searchforphotos/images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
            font_proxima_bold = os.path.abspath(
                os.path.join('../searchforphotos/images/fonts/Proxima Nova (1)/proximanova_bold.otf'))

            # font_path_semibold = os.path.abspath(
            #     os.path.join(
            #         '../images/fonts/San Francisco Pro Display (1)/SF-Pro-Display-Semibold.otf'))
            # font_proxima_bold = os.path.abspath(
            #     os.path.join('../images/fonts/Proxima Nova (1)/proximanova_bold.otf'))


            draw = ImageDraw.Draw(background)

            font_size = 26
            font = ImageFont.truetype(font_proxima_bold, font_size)
            text = profile_dict['profile_name']
            if len(text) > 18:
                text = text[:18] + '...'


            bbox = draw.textbbox((0, 0), text, font=font)
            text_position = (196, background.size[1] - 1188)
            text_color = (0, 0, 0)
            draw.text(text_position, text, fill=text_color, font=font)



            now = datetime.now()
            current_time = now.strftime("%H:%M")
            font_size = 26
            font = ImageFont.truetype(font_path_semibold, font_size)
            text = current_time
            text_position = (49, background.size[1] - 1257)
            text_color = (6, 6, 6)
            draw.text(text_position, text, fill=text_color, font=font)

            output = BytesIO()

            num_photo_chat += 1

            #background.save('res_tiktok_chats.png', format='PNG')
            background.save(output, format='PNG')
            output.seek(0)  # Reset buffer position to the beginning

            image_png_file_buffer = BufferedInputFile(output.getvalue(), filename=f"image{num_photo_chat}.png")

            logger_tiktok_chats_generate.info('Картинка сгенерирована')

            tg_photo_list_objects.append(image_png_file_buffer)

        return tg_photo_list_objects
    except Exception:
        logger_tiktok_chats_generate.info('Не удалось сгенерировать фотографии чата тг')
        return None

# say_dict = {'username': 'shantanova.maria', 'profile_name': 'Илон Маск/Elon Musk: SpaceX, Tesla, Solar City', 'link_image': 'https://scontent-fra5-1.xx.fbcdn.net/v/t39.30808-1/381465036_10162828552227506_7562208141319006202_n.jpg?stp=dst-jpg_p480x480&_nc_cat=108&ccb=1-7&_nc_sid=5f2048&_nc_ohc=Chv7QODo1YgAX9VPK4b&_nc_ht=scontent-fra5-1.xx&oh=00_AfBCXJVSjYkEq9_aWAR0N9hivei-fUiDSxPXuRZkM00JnA&oe=65FDC233', 'link_background': 'https://scontent-fra3-2.xx.fbcdn.net/v/t1.6435-9/101557164_10159645279752506_6369118045322870784_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=5f2048&_nc_ohc=y44BV6DmWksAX9VaGw9&_nc_ht=scontent-fra3-2.xx&oh=00_AfD9Vozets0kRAcjluPYLDboJbIcSB639hEXOpEcFY43qQ&oe=6620E13E'}
# #
# if __name__ == '__main__':
#     asyncio.run(tiktok_chats_generate(say_dict))
