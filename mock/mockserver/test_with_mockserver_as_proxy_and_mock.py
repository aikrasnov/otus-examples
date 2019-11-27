import pytest
import time
import requests
from selenium.webdriver import Chrome, ChromeOptions

# python simple_server
# mockserver -serverPort 1080

@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.add_argument("--proxy-server=http://localhost:1080")
    driver = Chrome(options=options)
    yield driver
    driver.quit()


def test_literal_answer(driver):
    requests.put("http://localhost:1080/mockserver/expectation", json={
        "httpRequest": {
            "path": "/"
        },
        "httpResponse": {
            "body": "Hello from MockServer!"
        }
    })

    # Пояснить откуда взялся домен testapp
    driver.get("http://testapp:8080")
    # wait until we done here
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

def test_update_by_template(driver):
    requests.put("http://localhost:1080/mockserver/expectation", json={
        "httpRequest": {
            "path": "/123"
        },
        "httpForwardTemplate": {
            "template": "return { 'method': 'GET', 'path': '/456', 'queryStringParameters': { 'predef': ['foobar'] }, 'headers': request.headers }",
            "templateType": "JAVASCRIPT"
        }
    })

    driver.get("http://testapp:8080")
    # wait until we done here
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass