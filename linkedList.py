# Optimized


class Node:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.node = None
        self.size = 0
        self.last = self.node
        self.lastButOne = self.node

    def getSize(self):
        # O(1)
        return self.size

    def prepend(self, node):
        # O(1)
        curr = node
        curr.next = self.node
        self.node = node
        self.size += 1  # track size
        return self.node

    def append(self, node):
        # O(1)
        if not self.node:
            self.node = node
            self.last = self.node  # track tail
            self.lastButOne = self.node  # track last but one
            self.size += 1  # track size
            return self.node

        self.last.next = node
        self.last = self.last.next  # track tail
        if self.getSize() >= 2:
            self.lastButOne = self.lastButOne.next  # track last but one
        self.size += 1  # track size
        return self.node

    def popFront(self):
        # O(1)
        self.node = self.node.next
        self.size -= 1  # track size
        return self.node

    def pop(self):
        # O(1)
        self.lastButOne.next = None
        self.size -= 1  # track size
        return self.node

    def print(self):
        curr = self.node
        print("Output::: ", end="")
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


import unittest


class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.print()

        self.assertEqual(ll.getSize(), 3)
        self.assertEqual(ll.node.val, 1)
        self.assertEqual(ll.node.next.val, 2)
        self.assertEqual(ll.node.next.next.val, 3)

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(Node(1))
        ll.prepend(Node(2))
        ll.prepend(Node(3))
        ll.print()

        self.assertEqual(ll.getSize(), 3)
        self.assertEqual(ll.node.val, 3)
        self.assertEqual(ll.node.next.val, 2)
        self.assertEqual(ll.node.next.next.val, 1)

    def test_popFront(self):
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.popFront()
        self.assertEqual(ll.getSize(), 2)
        self.assertEqual(ll.node.val, 2)
        self.assertEqual(ll.node.next.val, 3)

    def test_pop(self):
        ll = LinkedList()
        ll.append(Node(1))
        ll.append(Node(2))
        ll.append(Node(3))
        ll.pop()
        ll.print()
        self.assertEqual(ll.getSize(), 2)
        self.assertEqual(ll.node.val, 1)
        self.assertEqual(ll.node.next.val, 2)
        self.assertIsNone(ll.node.next.next)

    def test_getSize(self):
        ll = LinkedList()
        self.assertEqual(ll.getSize(), 0)
        ll.append(Node(1))
        self.assertEqual(ll.getSize(), 1)
        ll.append(Node(2))
        self.assertEqual(ll.getSize(), 2)


if __name__ == "__main__":
    unittest.main()
