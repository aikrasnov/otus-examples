from selenium.webdriver import TouchActions
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('mobileEmulation', {"deviceName": "Nexus 5"})
options.add_experimental_option('w3c', False)
chrome = webdriver.Chrome(desired_capabilities=options.to_capabilities())

chrome.implicitly_wait(20)
chrome.maximize_window()

chrome.get("https://www.kinopoisk.ru/picture/3435927/")

actions = TouchActions(chrome)
slider = chrome.find_element_by_css_selector(".image-slider__slides")
actions.flick_element(slider, xoffset=500, yoffset=0, speed=1000)
actions.flick_element(slider, xoffset=-500, yoffset=0, speed=1000)
actions.flick_element(slider, xoffset=-500, yoffset=0, speed=1000)
actions.flick_element(slider, xoffset=500, yoffset=0, speed=1000)
actions.perform()
# chrome.quit()