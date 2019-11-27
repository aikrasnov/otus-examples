from unittest.mock import patch

def foo():
    return input()

@patch("builtins.input", lambda *args: "string")
def test_foo():
    assert foo() == "string"