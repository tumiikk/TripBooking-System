
PAYMENT_FILE = "data/payment.json"

from collections import deque
from collections import deque
from utils.file_handler import load_json

# PAYMENT_FILE = "payment.json"
class Graph:
    def __init__(self):
        self.graph = {}
        # ambil data json
        data = load_json(PAYMENT_FILE)
        flights = data["flights"]
        # otomatis isi graph
        for flight in flights.values():

            asal = flight["asal"]
            tujuan = flight["tujuan"]

            self.add_edge(asal, tujuan)

    # tambah jalur
    def add_edge(self, asal, tujuan):
        if asal not in self.graph:
            self.graph[asal] = []
        self.graph[asal].append(tujuan)

    # BFS
    def bfs(self, start, goal):

        queue = deque([[start]])
        visited = set()

        while queue:
            path = queue.popleft()
            kota = path[-1]
            if kota == goal:
                return path
            if kota not in visited:
                visited.add(kota)
                for tetangga in self.graph.get(kota, []):
                    jalur_baru = list(path)
                    jalur_baru.append(tetangga)
                    queue.append(jalur_baru)

        return None
    
