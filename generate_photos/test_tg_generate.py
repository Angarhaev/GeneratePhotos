import os
import requests
import cv2
import numpy as np
from PIL import Image, ImageDraw
from io import BytesIO

# Путь к фоновому изображению
background_image_path = os.path.abspath(os.path.join('../images/tiktok_main_example.png'))

# URL изображения лица
face_image_url = 'https://p16-sign-sg.tiktokcdn.com/aweme/720x720/tos-alisg-avt-0068/dfa23fc652ab71aa3efcbeb82133a38a.jpeg?lk3s=a5d48078&x-expires=1711206000&amp;x-signature=4eLEcd5yFCjJmE8GyRUHccNGPww%3D'

# Загрузка фонового изображения
background = cv2.imread(background_image_path)

# Загрузка изображения лица
response = requests.get(face_image_url)
face_1 = Image.open(BytesIO(response.content))

# Преобразование изображения лица в массив NumPy
face_1 = np.array(face_1)

# Размеры лица
face_size_1 = 108

# Создание маски для определения формы круглой картинки
mask = Image.new('L', (face_size_1, face_size_1), 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + (face_size_1, face_size_1), fill=255)

# Преобразование маски в массив NumPy
mask_np = np.array(mask)

# Применение размытия к маске
blurred_mask = cv2.GaussianBlur(mask_np, (15, 15), 0)

# Преобразование фонового изображения в формат с альфа-каналом
background = cv2.cvtColor(background, cv2.COLOR_BGR2BGRA)

# Применение маски к альфа-каналу
background[:, :, 3] = blurred_mask

# Позиция для вставки лица на фоновое изображение
position = (278, 178)

# Преобразование фонового изображения в объект PIL.Image
background_pil = Image.fromarray(cv2.cvtColor(background, cv2.COLOR_BGRA2RGBA))

# Вставка лица на фоновое изображение
face_1_pil = Image.fromarray(face_1)
background_pil.paste(face_1_pil, position, mask=face_1_pil)

# Преобразование результата обратно в массив NumPy для сохранения с OpenCV
result_image = cv2.cvtColor(np.array(background_pil), cv2.COLOR_RGBA2BGRA)

# Путь для сохранения результата
output_path = "output_image.png"

# Сохранение результата
cv2.imwrite(output_path, result_image)