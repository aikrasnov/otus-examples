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
contravariant_list: typing.List[Foo] = [Wednesday(), Wednesday(), Wednesday()]

# https://habr.com/ru/post/218753/


class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def bark(self):
        pass

class Cat(Animal):
    def meow(self):
        pass

animal_list: typing.List[Animal] = [Dog(), Cat()]

for animal in animal_list:
    animal.make_sound()