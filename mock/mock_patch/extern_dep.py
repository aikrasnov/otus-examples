from unittest.mock import patch
from utils.foo import foo_fn


# @patch("utils.bar.bar_fn")  # wrong
@patch("utils.foo.bar_fn", lambda *args: "this is from mock")
def test_foo():
    assert foo_fn() == "this is from mock"