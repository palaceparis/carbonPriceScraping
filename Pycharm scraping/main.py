import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import datetime as dt
import pandas as pd
from bs4 import BeautifulSoup

# Opening the connection and grabbing the page
my_url = 'https://www.hbets.cn'
driver = webdriver.Firefox()
driver.get(my_url)

action = ActionChains(driver)
element = driver.find_element(By.CSS_SELECTOR, '#container1')
loc = element.location
size = element.size

dictionary = {}
dictionary[date] = details
action.move_to_element_with_offset(element, 311, 0).perform()
details = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div/div[2]').text
if details !='':
    date = dt.datetime.strptime(details[:10], "%Y-%m-%d")
else:
    dictionary[date] = details

# The order is important, date and details.

date_string = "10 May, 2017"
limit = dt.datetime.strptime(date_string, "%d %B, %Y")
pace = -1

while True:
    action.move_by_offset(pace, 0).perform()
    details = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[1]/div/div[2]').text
    date = dt.datetime.strptime(details[:10], "%Y-%M-%d")

    if date < limit:
        break

    if details != '':
        date = dt.datetime.strptime(details[:10], "%Y-%m-%d")
        dictionary[date] = details

driver.quit()

df = pd.DataFrame.from_dict(dictionary, orient='index')

df.to_excel(r"/Users/tonygong/Downloads/HB.xlsx", index=True)
