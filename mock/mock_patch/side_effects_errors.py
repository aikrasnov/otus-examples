from unittest.mock import patch


def bar():
    return "Good"


def foo():
    try:
        return bar()
    except TypeError:
        print("TypeError occurs")

def test_function():
    with patch('side_effects_errors.bar', side_effect=TypeError):
        assert foo() is None