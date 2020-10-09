import pytest


@pytest.fixture()
def foo():
    print('do something on setup\n')
    yield
    print('do something on teardown\n')