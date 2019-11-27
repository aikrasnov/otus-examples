from unittest.mock import patch


def foo():
    return input(), input(), input()


def test_function():
    with patch('builtins.input', side_effect=("expected_one", "expected_two", "expected_three")) as mock:
        # foo()
        print(dir(mock))
        print("mock.assert_called: ", mock.assert_called)
        print("mock.assert_called_once: ", mock.assert_called_once)
        print("mock.call_count: ", mock.call_count)
        print("mock.called: ", mock.called)
        print("mock.method_calls: ", mock.method_calls)
        assert foo() == ("expected_one", "expected_two", "expected_three")