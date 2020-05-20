import unittest
import sys
from bar import foo


# python -m unittest -h
class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.data = [1, 2, 3, 4]

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(foo.__version__ < 1,
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")


# def skipUnlessHasattr(obj, attr):
#     if hasattr(obj, attr):
#         return lambda func: func
#     return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))