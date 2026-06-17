from collections import deque

class Graph:

    def __init__(self):
        self.graph = {}

    def add_vertex(self, city):
        if city not in self.graph:
            self.graph[city] = []

    def add_edge(self, asal, tujuan):
        self.add_vertex(asal)
        self.add_vertex(tujuan)

        self.graph[asal].append(tujuan)

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
