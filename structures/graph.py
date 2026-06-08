<<<<<<< HEAD
from collections import deque

=======
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, city):
<<<<<<< HEAD
        if city not in self.graph:
            self.graph[city] = []

    def add_edge(self, asal, tujuan):
=======

        if city not in self.graph:
            self.graph[city] = []

    def add_edge(self, asal, tujuan):

>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
        self.add_vertex(asal)
        self.add_vertex(tujuan)

        self.graph[asal].append(tujuan)

<<<<<<< HEAD
    def cari_rute(self, asal, tujuan):

        queue = deque([[asal]])
        visited = set()

        while queue:

            path = queue.popleft()
            kota = path[-1]

            if kota == tujuan:
                return path

            if kota not in visited:
                visited.add(kota)

                for tetangga in self.graph.get(kota, []):
                    jalur_baru = list(path)
                    jalur_baru.append(tetangga)

                    queue.append(jalur_baru)

        return None
=======
    def display(self):

        for city in self.graph:

            print(
                city,
                "->",
                self.graph[city]
            )
>>>>>>> f75d7907f9e37a28371497f59575f5d3bdb8dbde
