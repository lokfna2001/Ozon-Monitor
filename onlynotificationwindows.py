from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from time import sleep
import plyer


options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
#options.add_argument("--headles") # добавьте эту строку, если хотите чтобы браузер запускался без визуальной части.

while True:
    check_page = input("Вставьте ссылку на нужный товар."+"\n")
    if str(check_page).startswith('https://www.ozon.ru/'):
        while True:
            gg = random.choice(list(open('proxy.txt')))
            options.add_argument('--proxy-server=%s' % gg)
            try:
                browser = webdriver.Chrome("chromedriver.exe",
                                               options=options)
                browser.get(check_page)
                browser.find_element_by_xpath("//*[text()='Добавить в корзину']").is_enabled()
                sleep(5)
                product_name = browser.find_element_by_css_selector('h1.b3a8').text
                info = (product_name[:40] + '..') if len(product_name) > 40 else product_name
                full_url = str(browser.current_url)
                plyer.notification.notify(message='Доступен для покупки, ссылка в консоли.',
                                          app_name='govnochecker',
                                          title=info)
                print(full_url)
                sleep(600)
            except:
                sleep(10)
                browser.quit()
    else:
        print("Неверная ссылка.")
        break
        continue





