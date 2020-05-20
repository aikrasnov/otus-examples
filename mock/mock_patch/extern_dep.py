from unittest.mock import patch
from utils.foo import foo_fn



@patch("utils.foo.bar_fn", lambda *args: "this is from mock")
# @patch("os.path", lambda *args: "this is from mock") # wrong
@patch("utils.foo.path", lambda *args: "this is from mock")
# @patch("utils.bar.bar_fn", lambda *args: "this is from mock")  # wrong
def test_foo():
    foo = foo_fn()
    print(foo)
    assert foo == "this is from mock"