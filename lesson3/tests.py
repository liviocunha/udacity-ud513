import unittest
from binary_search import binary_search


class BinarySearchTests(unittest.TestCase):
    def setUp(self):
        self.test_list = [1, 3, 9, 11, 15, 19, 29]

    def test_binary_search(self):
        self.assertEqual(binary_search(25, self.test_list), -1)
        self.assertEqual(binary_search(15, self.test_list), -1)


if __name__ == '__main__':
    unittest.main()
