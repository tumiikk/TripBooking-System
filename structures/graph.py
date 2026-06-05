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

    def display(self):

        for city in self.graph:

            print(
                city,
                "->",
                self.graph[city]
            )