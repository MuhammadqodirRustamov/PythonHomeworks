import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

url_link = "https://www.demoblaze.com/"

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options)

driver.get(url_link)
laptops_button = driver.find_elements(By.ID, "itemc")[1]

laptops_button.click()
time.sleep(2)
next_button = driver.find_elements(By.CLASS_NAME, "page-item")[1]
next_button.click()
# time.sleep(1)
laptops = []
laptop_card_blocks = driver.find_elements(By.CLASS_NAME, "card-block")
for card_block in laptop_card_blocks:
    name = card_block.find_element(By.TAG_NAME, "a").text.strip()
    price = card_block.find_element(By.TAG_NAME, "h5").text.strip()
    desc = card_block.find_element(By.TAG_NAME, "P").text.strip()
    laptop_data = {"name": name, "price": price, "description": desc}
    laptops.append(laptop_data)

with open("data.json", "w") as file:
    json.dump(laptops, file, indent=4)