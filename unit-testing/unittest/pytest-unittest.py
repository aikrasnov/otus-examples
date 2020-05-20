import unittest
import pytest


@pytest.fixture(scope="class")
def db_class(request):
    class DummyDB(object):
        pass
    # set a class attribute on the invoking test context
    request.cls.db = DummyDB()


@pytest.mark.usefixtures("db_class")
class MyTest(unittest.TestCase):

    def setUp(self) -> None:
        self.foo = "bar"

    def tearDown(self) -> None:
        print("teardown")

    def test_method1(self):
        print(self.foo)
        assert hasattr(self, "db")
        assert 0, self.db   # fail for demo purposes

    def test_method2(self):
        assert 0, self.db   # fail for demo purposes