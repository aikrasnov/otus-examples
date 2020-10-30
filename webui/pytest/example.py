from webui.webdriver import Chrome

import pytest
import allure


def get_test_status(request):
    # rep_call не будет, если тест не завершился (например нажили CTRL-C)
    rep_call = getattr(request.node, "rep_call", None)
    status = getattr(rep_call, 'outcome', None)
    # ("failed", "passed", "skipped")
    return status


@pytest.fixture()
def selenium(request):
    driver = Chrome()
    yield driver
    # всегда прикреплять
    allure.attach(driver.current_url, "last url", allure.attachment_type.TEXT)
    allure.attach(driver.get_screenshot_as_png(), "screenshot", allure.attachment_type.PNG)
    # только для упавших
    status = get_test_status(request)
    print(status)
    # if status in ("failed", "passed"):
    #     allure.attach(driver.current_url, "last url", allure.attachment_type.TEXT)
    #     allure.attach(driver.get_screenshot_as_png(), "screenshot", allure.attachment_type.PNG)


def test_foo(selenium):
    selenium.get("https://ya.ru")
