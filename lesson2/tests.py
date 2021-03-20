import unittest
from linked_list import Element, LinkedList


class LinkedListTests(unittest.TestCase):
    def setUp(self):
        self.e1 = Element(1)
        self.e2 = Element(2)
        self.e3 = Element(3)
        self.e4 = Element(4)

    def test_start_setting_up_and_get_position(self):
        self.ll = LinkedList(self.e1)
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.assertEqual(3, self.ll.head.next.next.value)

    def test_get_position_three(self):
        self.ll = LinkedList(self.e1)
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.assertEqual(3, self.ll.get_position(3).value)

    def test_insert_element_four_in_position_three(self):
        self.ll = LinkedList(self.e1)
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.ll.insert(self.e4, 3)
        self.assertEqual(4, self.ll.get_position(3).value)

    def test_delete_value_one(self):
        self.ll = LinkedList(self.e1)
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.ll.insert(self.e4, 3)
        self.ll.delete(1)
        self.assertEqual(2, self.ll.get_position(1).value)

    def test_get_position_two(self):
        self.ll = LinkedList(self.e1)
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.ll.insert(self.e4, 3)
        self.ll.delete(1)
        self.assertEqual(4, self.ll.get_position(2).value)

    def test_get_position_three_again(self):
        self.ll = LinkedList(self.e1)
        self.ll.append(self.e2)
        self.ll.append(self.e3)
        self.ll.insert(self.e4, 3)
        self.ll.delete(1)
        self.assertEqual(3, self.ll.get_position(3).value)


if __name__ == '__main__':
    unittest.main()