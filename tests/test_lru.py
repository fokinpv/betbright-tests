import unittest

from betbright_tests.lru import lru


@lru(max_size=2)
def add(a, b, param=True):
    return a + b


@lru(max_size=30)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


class TestLRU(unittest.TestCase):

    def test_lru(self):
        self.assertEqual(add(1, 2, param=True), 3)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(4, 5), 9)

        self.assertTrue(hash((4, 5)) in add._cache)
        self.assertTrue(hash((1, 2)) not in add._cache)

        self.assertEqual(add(1, 2, param=True), 3)

        self.assertEqual(add.cache_len(), 2)

    @unittest.skip
    def test_lru_recursive(self):

        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(100), 354224848179261915075)
