from unittest.mock import patch


def foo():
    return input(), input(), input()


def test_function():
    with patch('builtins.input', side_effect=("expected_one", "expected_two", "expected_three", "expected_four")):
        assert foo() == ("expected_one", "expected_two", "expected_three")
        assert input() == "expected_four"