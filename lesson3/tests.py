import unittest
from binary_search import binary_search
from get_fib import get_fib


class BinarySearchTests(unittest.TestCase):
    def setUp(self):
        self.test_list = [1, 3, 9, 11, 15, 19, 29]

    def test_binary_search(self):
        self.assertEqual(binary_search(25, self.test_list), -1)
        self.assertEqual(binary_search(15, self.test_list), -1)


class GetFibTests(unittest.TestCase):
    def test_get_fib_nine(self):
        self.assertEqual(get_fib(9), 34)

    def test_get_fib_eleven(self):
        self.assertEqual(get_fib(11), 89)

    def test_get_fib_zero(self):
        self.assertEqual(get_fib(0), 0)


if __name__ == '__main__':
    unittest.main()
