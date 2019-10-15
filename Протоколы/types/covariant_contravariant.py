import typing

invariant = typing.TypeVar("invariant")
contravariant = typing.TypeVar("contravariant", contravariant=True)
covariant = typing.TypeVar("covariant", covariant=True)


class Wednesday:
    pass

class Foo(Wednesday):
    pass

class Bar(Foo):
    pass


covariant_list: typing.List[Wednesday] = [Foo(), Foo(), Foo()]
contravariant_list: typing.List[Foo] = [Bar(), Bar(), Bar()]

# https://habr.com/ru/post/218753/
