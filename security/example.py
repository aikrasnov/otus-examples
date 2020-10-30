from webui.webdriver import Chrome


driver = Chrome()
driver.get("https://yandex.ru")
driver.execute_script("console.warn('foobar')")
logs = driver.get_log('browser')
driver.quit()


assert len(logs) > 0, "Нет логов!"
for log in logs:
    value = log.pop("message", "")
    assert not "foobar" in value, f"foobar в консоли: «{value}»"


