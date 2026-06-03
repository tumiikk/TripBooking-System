class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = node

    def display(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = DNode(data)

        if not self.head:
            self.head = node
            return

        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = node
        node.prev = cur

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = CNode(data)

        if not self.head:
            self.head = node
            node.next = node
            node.prev = node
            return

        tail = self.head.prev

        tail.next = node
        node.prev = tail

        node.next = self.head
        self.head.prev = node