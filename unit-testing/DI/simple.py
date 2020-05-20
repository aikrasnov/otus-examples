import os

class DB:
    def __init__(self, *args, **kwargs):
        pass

    def connect(self):
        raise NotImplementedError


class DummyDB(DB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = "foobar"

    def connect(self):
        parent_self = self
        class stub:
            def execute_sql(self, _):
                return parent_self.data
        return stub()


class MyAwesomeServer:
    def __init__(self, db: DB):
        self.db = db

    def run(self):
        # something here
        db = self.db.connect()
        # noinspection SqlDialectInspection,SqlNoDataSourceInspection
        db.execute_sql("SELECT * FROM foo")
        # something latter

if os.environ.get("TESTING") is not None:
    server = MyAwesomeServer(DummyDB())
else:
    server = MyAwesomeServer(DB())

server.run()
