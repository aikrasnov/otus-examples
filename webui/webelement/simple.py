# не забыть рассказать про поиск элементов локально и удалённо

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

driver.get("https://stackoverflow.com/")

# element_by_id = driver.find_element_by_id("content")
# element_by_xpath = driver.find_element_by_xpath("//a")
# element_by_name = driver.find_element_by_name("description")
# element_by_tag_name = driver.find_element_by_tag_name("meta")
# element_class_name = driver.find_element_by_class_name("home-page")
# element_css_selector = driver.find_element_by_css_selector(".home-page")

# elements_by_id = driver.find_elements_by_id("content")
# elements_by_xpath = driver.find_elements_by_xpath("//a")
# elements_by_name = driver.find_elements_by_name("description")
# elements_by_tag_name = driver.find_elements_by_tag_name("meta")
# elements_class_name = driver.find_elements_by_class_name("home-page")
# elements_css_selector = driver.find_elements_by_css_selector(".home-page")


# print(element_by_id)
# print(element_by_xpath)
# print(type(elements_by_xpath), len(elements_by_xpath))
# print(element_by_name)
# print(element_by_tag_name)
# print(element_class_name)
# print(element_css_selector)
# print('\n')

# element = driver.find_element(By.XPATH, "//a")
# elements = driver.find_elements(By.XPATH, '//a')

# Не забыть показать разницу если элементов нет
# print(element)
# print(type(elements), len(elements))
#
# print('\n')
# for prop in dir(element_by_xpath):
#     print(prop)
#
print(driver.find_element_by_css_selector("a").get_attribute("href"))
print(driver.find_element_by_css_selector("#footer").find_element_by_css_selector("a").get_attribute("href"))


element = driver.find_element_by_css_selector("a")
inner_element = element.find_element_by_css_selector("span")
inner_element.click()

driver.quit()
