from selenium import webdriver
import time

# NoSuchElementException -- элемент никогда не было на странице
# StaleElementReferenceException -- элемент был, но пропал
# ElementNotInteractableException -- элемент “выключен”, не кликаблен
# ElementClickInterceptedException -- другой элемент по ошибке получил клик
# InvalidSelectorException -- “кривой” локатор

chrome = webdriver.Chrome()

chrome.implicitly_wait(1)

chrome.get("https://www.kinopoisk.ru/")

# InvalidSelectorException
# chrome.find_element_by_css_selector("//*[@class]")

# NoSuchElementException
# chrome.find_element_by_css_selector(".foo .bar")

# StaleElementReferenceException
# element = chrome.find_element_by_css_selector("a")
# print(element)
# chrome.refresh()
# element = chrome.find_element_by_css_selector("a")
# print(element)
# element.click()

# ElementClickInterceptedException
chrome.execute_script("arguments[0].scrollIntoView()", chrome.find_element_by_xpath('//*[contains(text(), "Вакансии")]'))
chrome.find_element_by_css_selector('[alt="КиноПоиск"]').click()
time.sleep(5)
chrome.find_element_by_xpath('//*[contains(text(), "Вакансии")]').click()
