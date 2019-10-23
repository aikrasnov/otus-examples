import typing

class Bar:
    def awesome_method(self):
        print("kek")


def factory_without_typing(class_object):
    return class_object()

T = typing.TypeVar("T")
def factory_typed(class_object: typing.Type[T]) -> T:
    return class_object()

sad_bar = factory_without_typing(Bar)
sad_bar.bar()
sad_bar.awesome_method() # Показать, что автокомплит не работает

# не забыть показать type info awesome_bar
awesome_bar = factory_typed(Bar)
awesome_bar.awesome_method()


class ReturnSelf:
    def get_new_instance(self) -> 'ReturnSelf':
        return ReturnSelf()