import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import settings

options = Options()
if not settings.DEBUG:
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

driver = webdriver.Chrome(chrome_options=options)
print("Opening soundcloud")
driver.get(settings.SOUNDCLOUD_LANDING_URL)
print("Waiting for page load")
time.sleep(3)
print("Opening trending songs playlist")
driver.find_element_by_xpath(r'//*[@id="content"]/div/div/div[1]/div[2]/div/ul/li[1]/div/div[2]/div[1]/div/div/div[1]').click()
print("Waiting for page load")
time.sleep(2)
print("Starting the playlist")
driver.find_element_by_xpath(r'//*[@id="content"]/div/div/div[1]/div/div[2]/div[2]/div[1]').click()