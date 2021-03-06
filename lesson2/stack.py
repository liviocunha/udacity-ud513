"""

"""


class ElementStack(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListStack(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None


class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedListStack(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()


if __name__ == '__main__':
    e1 = ElementStack(1)
    e2 = ElementStack(2)
    e3 = ElementStack(3)
    e4 = ElementStack(4)

    stack = Stack(e1)

    stack.push(e2)
    stack.push(e3)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop())
    stack.push(e4)
    print(stack.pop().value)


