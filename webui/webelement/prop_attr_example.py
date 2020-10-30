from selenium import webdriver

chrome = webdriver.Chrome()
chrome.implicitly_wait(5)
chrome.get("https://yandex.ru")

home_tabs = chrome.find_element_by_css_selector("[data-id='market']")

# https://stackoverflow.com/questions/43627340/what-is-the-difference-between-property-and-attribute-in-selenium-webelement
html = home_tabs.get_property("innerHTML")
print(html)

attr = home_tabs.get_attribute("data-bem")
print(attr)

css = home_tabs.value_of_css_property("margin-bottom")
print(css)

chrome.close()