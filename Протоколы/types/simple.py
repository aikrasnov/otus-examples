from collections import defaultdict


class Foo:
    bar = 1


def get_string_length(string):
    return len(string)


without_type = get_string_length("foo_bar")
without_type_broken_1 = get_string_length(123)
without_type_broken_2 = get_string_length(defaultdict)


def get_string_length_typed(string: str) -> int:
    return len(string)


typed_type = get_string_length_typed("foo_bar")
typed_type_broken_1 = get_string_length_typed(123)
typed_type_broken_2 = get_string_length_typed(defaultdict)


def get_bar_of_foo_typed(foo_instance: Foo) -> int:
    return foo_instance.bar
