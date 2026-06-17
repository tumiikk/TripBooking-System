class Stack:
    def __init__(self):
        self.items = []

    # push = masukin data ke atas stack
    def push(self, item):
        self.items.append(item)

    # pop = ambil data paling terakhir (LIFO)
    def pop(self):
        if self.is_empty():
            print("Stack kosong, tidak bisa pop.")
            return None
        return self.items.pop()

    # cek kosong
    def is_empty(self):
        return len(self.items) == 0

    # lihat isi stack (tanpa menghapus)
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    # tampilkan semua isi stack
    def show(self):
        return self.items.copy()

    # ukuran stack
    def size(self):
        return len(self.items)