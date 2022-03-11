from typing import List, Dict
from typing import TypeVar

V = TypeVar('V')
E = TypeVar('E')


class SimpleGraph:
    vertices: Dict[int, V]
    edges: List[List[int]]
    edge_label: Dict[tuple, E]

    def order(self):
        return len(self.edges)

    def add_vertex(self):
        self.edges.append(list())

    def add_vertices(self, n):
        for i in range(n):
            self.add_vertex()

    def add_edge(self, u, v):
        m = max(u, v)
        if m > self.order():
            self.add_vertices(m - self.order())
        self.edges[u].append(v)

    def add_edges(self, edges):
        for e in edges:
            self.add_edge(e[0], e[1])
