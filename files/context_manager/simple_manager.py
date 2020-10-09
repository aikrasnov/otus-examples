import traceback


class Foo():

    def __init__(self):
        self.bar = "it's foo"

    def __enter__(self):
        print("setup")
        # Объяснить зачем return self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(traceback.extract_tb(exc_val))
        # print("teardown with:", exc_type, exc_val, exc_tb)
        # print("teardown with:", type(exc_type), type(exc_val), type(exc_tb))


with Foo() as f:
    print(f.bar)
    raise Exception("Foo")
