from unittest.mock import patch


def expected_values():
    for item in ["expected_one", "expected_two", "expected_three"]:
        yield item

exp_gen = expected_values()


def foo():
    one = input()
    two = input()
    three = input()
    return one, two, three


@patch('builtins.input', lambda *args: next(exp_gen))
def test_function():
    assert foo() == ("expected_one", "expected_two", "expected_three")