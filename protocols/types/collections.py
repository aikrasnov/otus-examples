from typing import List, Dict, Tuple

class Foo:
    pass

list_of_foo: List[Foo] = [Foo(), Foo(), Foo(), Foo()]
list_of_foo_error: List[Foo] = [1, 2, 3, 4, 5]

# Не забыть рассказать про TypedDict https://www.python.org/dev/peps/pep-0589/
typed_dict: Dict[str, int] = {"bar": 1}
typed_dict_error: Dict[str, int] = {1: 1}

tuple_of_foo: Tuple[Foo, Foo, list] = (Foo(), Foo(), [])
