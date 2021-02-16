from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
import pyshorteners
from time import sleep
import plyer




vk_login = ""
vk_password = ""
login_page = "https://vk.com/" # не менять
ls_page = "https://vk.com/ibelyaev2001" # на чью страницу отправлять сообщение
options = Options()
options.add_argument("window-size=1400,800")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome("chromedriver.exe",
                           options=options)


check_page = input("Вставьте ссылку на товар." + "\n")
if str(check_page).startswith('https://www.ozon.ru/'):
    while True:
        try:
            browser.get(check_page)
            browser.find_element_by_xpath("//*[text()='Добавить в корзину']").is_enabled()
            sleep(5)
            full_url = str(browser.current_url)
            product_name = browser.find_element_by_css_selector('h1.b3a8').text
            info = (product_name[:40] + '..') if len(product_name) > 40 else product_name
            plyer.notification.notify(message=full_url,
                                          app_name='govnochecker',
                                          title=info)
            browser.get(login_page)
            sleep(5)
            try:
                browser.find_element_by_id("index_email").is_enabled()
                phonereg = browser.find_element_by_id("index_email")
                phonereg.send_keys(vk_login)
                passreg = browser.find_element_by_id("index_pass")
                passreg.send_keys(vk_password)
                sleep(1)
                nomy = browser.find_element_by_id("index_expire")
                nomy.click()
                sleep(2)
                enterlog = browser.find_element_by_id("index_login_button")
                enterlog.click()
                sleep(4)
                browser.get(ls_page)
                post = browser.find_element_by_id("profile_message_send")
                post.click()
                sleep(2)
                spost = browser.find_element_by_id("mail_box_editable")
                send_post = browser.find_element_by_id("mail_box_send")
                s = pyshorteners.Shortener()
                b = s.tinyurl.short(full_url)
                spost.send_keys("PS5 "+b)
                send_post.click()
                sleep(600)
            except:
                browser.get(ls_page)
                post = browser.find_element_by_id("profile_message_send")
                post.click()
                sleep(2)
                spost = browser.find_element_by_id("mail_box_editable")
                send_post = browser.find_element_by_id("mail_box_send")
                s = pyshorteners.Shortener()
                b = s.tinyurl.short(full_url)
                spost.send_keys("PS5 " + b)
                send_post.click()
                sleep(600)
        except:
            sleep(random.randint(1 , 10))
            browser.refresh()
else:
    print("Неверная ссылка.")
    browser.quit()



