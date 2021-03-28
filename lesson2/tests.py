import unittest
from linked_list import Element, LinkedList
from stack import ElementStack, LinkedListStack, Stack
from queue import Queue


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


class StackTests(unittest.TestCase):
    def setUp(self):
        self.e1 = ElementStack(1)
        self.e2 = ElementStack(2)
        self.e3 = ElementStack(3)
        self.e4 = ElementStack(4)
        self.stack = Stack(self.e1)

    def test_push_element_two_and_three(self):
        self.assertIsNone(self.stack.push(self.e2))
        self.assertIsNone(self.stack.push(self.e3))

    def test_pop_first(self):
        self.stack.push(self.e2)
        self.stack.push(self.e3)
        self.assertEqual(3, self.stack.pop().value)

    def test_pop_second(self):
        self.stack.push(self.e2)
        self.stack.push(self.e3)
        self.stack.pop().value
        self.assertEqual(2, self.stack.pop().value)

    def test_pop_third(self):
        self.stack.push(self.e2)
        self.stack.push(self.e3)
        self.stack.pop().value
        self.stack.pop().value
        self.assertEqual(1, self.stack.pop().value)

    def test_pop_fourth(self):
        self.stack.push(self.e2)
        self.stack.push(self.e3)
        self.stack.pop().value
        self.stack.pop().value
        self.stack.pop().value
        self.assertIsNone(self.stack.pop())

    def test_push_element_four(self):
        self.assertIsNone(self.stack.push(self.e4))

    def test_pop_element_four(self):
        self.stack.push(self.e4)
        self.assertEqual(4, self.stack.pop().value)


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.q = Queue(1)
        self.q.enqueue(2)
        self.q.enqueue(3)

    def test_peek(self):
        self.assertEqual(self.q.peek(), 1)

    def test_dequeue(self):
        self.assertEqual(self.q.dequeue(), 1)

    def test_enqueue(self):
        self.assertEqual(self.q.enqueue(4), [1, 2, 3, 4])

    def test_second_dequeue(self):
        self.q.dequeue()
        self.assertEqual(self.q.dequeue(), 2)

    def test_thirdy_dequeue(self):
        self.q.dequeue()
        self.q.dequeue()
        self.assertEqual(self.q.dequeue(), 3)

    def test_fourty_dequeue(self):
        self.q.enqueue(4)
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.assertEqual(self.q.dequeue(), 4)

    def test_second_peek(self):
        self.q.enqueue(4)
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.q.dequeue()
        self.q.enqueue(5)
        self.assertEqual(self.q.peek(), 5)


if __name__ == '__main__':
    unittest.main()
