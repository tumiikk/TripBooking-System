class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

<<<<<<< HEAD
    def pop(self):
        return self.data.pop()

    def show(self):
        return self.data

=======
    def show(self):
        return self.data


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
