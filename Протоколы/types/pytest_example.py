import pytest
import typing
from selenium.webdriver import Remote


class FooPage:
    pass

class BarPage:
    pass

class BarChildPage(BarPage):
    pass


T = typing.TypeVar("T")
P = typing.TypeVar("P", bound=BarPage)


class SimpleTestClass:

    @pytest.fixture
    def driver(self):
        pass

    def page_factory(self, page_class: typing.Type[P]) -> P:
        return page_class()

    def foo_test(self, driver):
        driver.save_screenshot()

    def foo_test_typed(self, driver: Remote):
        driver.get("foobar")

    def page_factory_example_test(self):
        page_foo = self.page_factory(FooPage)
        page_bar = self.page_factory(BarPage)
        page_bar_child = self.page_factory(BarChildPage)
