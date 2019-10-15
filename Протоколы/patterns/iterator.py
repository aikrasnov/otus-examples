# https://docs.python.org/3/c-api/iter.html

class Test:
    def __init__(self, limit):
        self.limit = limit

    # Called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        # Store current value ofx
        x = self.x

        # Stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration

        # Else increment and return old value
        self.x = x + 1
        return x


class Foo:

    def __init__(self):
        self.example = [1, 2, 3, 4]

    def __next__(self):
        for i in self.example:
            yield i