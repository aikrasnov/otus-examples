import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome


browser = Chrome()
browser.get("https://konflic.github.io/front_example")
browser.maximize_window()

# Сначала проверяем клик по задизейбленой кнопке
dis_btn = browser.find_element_by_id("disabled")
dis_btn.click()

time.sleep(10)  # Для демонстрации

# Проверяем что не видна модалка
WebDriverWait(browser, 3).until_not(EC.visibility_of(browser.find_element_by_id("myModal")))

# Убираем атрибут через js и проверяем
js_code = "$('#disabled')[0].disabled = false;"
browser.execute_script(js_code)
# Показать как передавать элементы в скрипт
# js_code = "arguments[0].disabled = false;"
# browser.execute_script(js_code, browser.find_element_by_id("disabled"))

time.sleep(1)  # Для демонстрации

dis_btn.click()

time.sleep(1)  # Для демонстрации

# Проверяем что видна модалка
WebDriverWait(browser, 3).until(EC.visibility_of(browser.find_element_by_id("myModal")))
