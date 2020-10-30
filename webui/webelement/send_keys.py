import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()

chrome.implicitly_wait(5)
chrome.get("https://konflic.github.io/front_example/")

input_field = chrome.find_element_by_id("inp")

input_field.send_keys("Hello, my dear friend!")

time.sleep(1)

input_field.clear()

SPEED = 0.5
time.sleep(SPEED)

# //*[@contains(text(), 'button text')]
# <button qa-id='button'></button>
# //div[@class='foo']/div[3]/span[2]

input_field.send_keys("-=[ ]=-")

# Не забыть рассказать про сочетания клавиш
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.ARROW_LEFT)
time.sleep(SPEED)
input_field.send_keys(Keys.SPACE)
time.sleep(SPEED)
input_field.send_keys("COBRA")

for _ in range(len(input_field.text)):
    time.sleep(SPEED)
    input_field.send_keys(Keys.BACKSPACE)

input_field.send_keys("SELENIUM")