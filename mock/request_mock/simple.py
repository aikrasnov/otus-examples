import pytest
import requests
import requests_mock


def foo():
    return requests.get("https://ya.ru")


@pytest.fixture
def mock():
    with requests_mock.Mocker() as mock_instance:
        yield mock_instance


def test_foo():
    # https://requests-mock.readthedocs.io/en/latest/matching.html
    # mock.get("https://ya.ru", status_code = 500)
    # mock.post("https://go.mail.ru", status_code=400)
    response = foo()
    assert response.status_code == 500