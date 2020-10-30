import pytest
import time
import requests
from webui.webdriver import Chrome, ChromeOptions

# python simple_server
# mockserver -serverPort 1080
# docker run jamesdbloom/mockserver:mockserver-5.10.0

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

def test_literal_answer_two(driver):
    requests.put("http://localhost:1080/mockserver/expectation", json={
        "httpRequest": {
            "path": "/books"
        },
        "httpResponse": {
            "body": {
                "type": "JSON",
                "json": '[{"author": "Perovskaya S. L.", "year": "1881", "title": "Regicide"}]'
            }
        }
    })

    # Пояснить откуда взялся домен testapp
    driver.get("http://testapp:8080/books")
    # wait until we done here
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

def test_update_by_template(driver):
    requests.put("http://localhost:1080/mockserver/expectation", json={
        "httpRequest": {
            "path": "/1234"
        },
        "httpForwardTemplate": {
            "template": "return { 'method': 'GET', 'path': '/5678', 'queryStringParameters': { 'predef': ['foobar'] }, 'headers': request.headers }",
            "templateType": "JAVASCRIPT"
        }
    })

    driver.get("http://testapp:8080")
    driver.get("http://testapp:8080/1234")
    # wait until we done here
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

# https://www.mock-server.com/#why-use-mockserver
