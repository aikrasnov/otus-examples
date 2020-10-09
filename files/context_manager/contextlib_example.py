import contextlib


with contextlib.suppress(Exception):
     raise Exception


@contextlib.contextmanager
def foo():
    print("This is inside foo")
    yield 'from foo'
    print("Teardown")


with foo() as f:
    print(f)