import unittest
from binary_search import binary_search
from get_fib import get_fib
from bubble_sort import bubble_sort
from merge_sort import merge_sort


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


class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    def test_bubble_sort(self):
        self.expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        self.assertEqual(bubble_sort(self.test_list), self.expected)


class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    def test_bubble_sort(self):
        self.expected = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        merge_sort(self.test_list)
        self.assertEqual(self.test_list, self.expected)


if __name__ == '__main__':
    unittest.main()
