import re
import asyncio
from aiohttp import ClientSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import logging
import multiprocessing

logger_fb_scrap = logging.getLogger(__name__)


async def scrape_url(url, config):
    """Функция для скрапинга имени и фото фэйсбук профиля"""
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=en-US")
    options.add_argument("--incognito")
    options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    stealth(driver, languages=["en-US", "en"], vendor="Google Inc.", platform="Win32",
            webgl_vendor="Intel Inc.", renderer="Intel Iris OpenGL Engine", fix_hairline=True)
    wait = WebDriverWait(driver, 5)

    try:
        async with ClientSession() as session:
            driver.get('https://www.facebook.com/login')
            email = config.LOGIN_FACEBOOK
            password = config.PASSWORD_FACEBOOK

            driver.find_element(By.ID, "email").send_keys(email)
            driver.find_element(By.ID, "pass").send_keys(password)
            driver.find_element(By.NAME, "login").click()

            #Здесь мы ждем, когда будет прогружен данный элемент с таким значением, чтобы дальнейшее открытие ссылки происходило без ошибок
            wait.until(lambda driver: driver.find_element(By.CLASS_NAME,
                                                           "x5yr21d").get_attribute("src") != "")
            logger_fb_scrap.info('Logged in to Facebook successfully')
            driver.get(url)
            page_source = driver.page_source

            page = BeautifulSoup(page_source, 'html.parser')
            username = re.search(r'facebook\.com/([\w\.]+)', url).group(1)
            name = ''

            #В данном элементе содержится имя профиля
            svg_elements = page.select('.x1rg5ohu.x1n2onr6.x3ajldb.x1ja2u2z svg[aria-label]')

            logger_fb_scrap.info('SVG elements inside class obtained')
            for svg in svg_elements:
                aria_label = svg.get('aria-label')
                if aria_label != "Your Profile":
                    name = aria_label

            #фон
            page.get_text()
            img = page.find_all('img')
            img_links = [i_img.get('src') for i_img in img]
            #print(img_links)

            #аватар
            image_tags = page.find_all('image')
            image_links = [img.get('xlink:href') for img in image_tags]
            logger_fb_scrap.info('Ссылки на фото фэйсбук получены')

            scrap_dict = {
                'username': username,
                'profile_name': name,
                'link_image': image_links[1],
                'link_background': img_links[1]
            }
            #print(scrap_dict)

            return scrap_dict

    except TimeoutException as exc:
        logger_fb_scrap.info(f'Не удалось произвести скрапинг фэйсбук: {exc}')
        return None

    finally:
        driver.quit()


def async_process(queue, url, config):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(scrape_url(url, config))
    queue.put(result)
    loop.close()


def main_scrape(url_facebook, config):
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=async_process, args=(queue, url_facebook, config))
    process.start()
    process.join()
    result = queue.get()
    return result

# if __name__ == '__main__':
#     asyncio.run(scrape_url('https://www.facebook.com/shantanova.maria'))
