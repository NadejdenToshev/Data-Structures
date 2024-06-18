class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        else:
            raise ValueError("One or both vertices not found in the graph")

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def __str__(self):
        graph_str = ""
        for vertex in self.graph:
            graph_str += f"{vertex}: {self.graph[vertex]}\n"
        return graph_str

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_vertex('A')
    g.add_vertex('B')
    g.add_vertex('C')
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.display()
    # Alternatively, you can use print(g) to display the graph