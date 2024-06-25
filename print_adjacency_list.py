class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def __str__(self):
        return '\n'.join([f'{vertex}: {neighbors}' for vertex, neighbors in self.adjacency_list.items()])

    def print_adjacency_list(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex}: {', '.join(neighbors)}")


if __name__ == "__main__":
    g = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    
    for vertex in vertices:
        g.add_vertex(vertex)

    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F')
    ]
    
    for vertex1, vertex2 in edges:
        g.add_edge(vertex1, vertex2)

    print("Graph adjacency list:")
    g.print_adjacency_list()