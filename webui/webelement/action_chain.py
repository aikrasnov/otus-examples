import random

from selenium.webdriver import ActionChains
from selenium import webdriver

chrome = webdriver.Chrome()

chrome.implicitly_wait(20)
chrome.maximize_window()

# Открываем страницу и закрываем поп-ап
chrome.get("https://sketch.io/sketchpad/en/")
chrome.find_element_by_css_selector(".welcome-message > .close-button").click()

# Получаем облассть в которой можно рисовать
draw_area = chrome.find_element_by_tag_name("sketch-viewport")

# Создаем объект ActionChains в который будем записывать наши действия
actions = ActionChains(chrome)

# Меняем кисть на карандаш
chrome.find_element_by_css_selector("grid-view-trigger").click()
chrome.find_element_by_xpath("//grid-title[text()='Pencil']").click()


# Наполняем actions 10 разными действиями
for i in range(20):
    # Определяем случайные координаты по x и y
    random_x = random.randint(300, 700)
    random_y = random.randint(300, 700)
    # Нажимаем на кнопку мыши в этих координатах и не отпускаем
    actions.move_to_element_with_offset(draw_area, random_x, random_y).click_and_hold()
    # Определяем случайные величины для смешения курсора от текущей точки
    offset_x = random.randint(-150, 200)
    offset_y = random.randint(-200, 150)
    # Выполняем движение мышью на заданное количество пикселей и отпускаем
    actions.move_by_offset(offset_x, offset_y).release()

# Выполняем все накопленные в цикле for действия начиная с первого
actions.perform()