from collections import deque

class Graph:
    def __init__(self, size, directed=True):
        self.size = size
        self.directed = directed
        self.adjMatrix = [[-1] * size for _ in range(size)]
        self.vertices = {}
        self.verticesList = [0] * size

    # sets
    def set_vertex(self, v, id):
        if 0 <= v <= self.size:
            self.vertices[id] = v
            self.verticesList[v] = id

    def set_edge(self, frm, to, weight=0):
        frm = self.vertices[frm]
        to = self.vertices[to]

        self.adjMatrix[frm][to] = weight
        if not self.directed:
            self.adjMatrix[to][frm] = weight

    # gets
    def get_matrix(self):
        return self.adjMatrix

    def get_vertices(self):
        return self.verticesList

    def get_edges(self):
        edges = []
        for i in range(self.size):
            for j in range(self.size):
                if self.adjMatrix[i][j] != -1:
                    edges.append((self.verticesList[i], self.verticesList[j], self.adjMatrix[i][j]))
        return edges
    
    # traversals
    def dfs(self, start):
        visited = [False] * self.size
        start = self.vertices[start]
        l = []

        def visit(start):
            nonlocal visited, l
            
            if visited[start]:
                return

            l.append(start)
            visited[start] = True
            for v in range(self.size):
                if self.adjMatrix[start][v] != -1 and not visited[v]:
                    visit(v)
            return
        
        visit(start)
        return l

    def bfs(self, start):
        visited = [False] * self.size
        start = self.vertices[start]
        l, q = [], deque()

        q.append(start)
        visited[start] = True
        while q:
            start = q.popleft()
            l.append(start)

            for i in range(self.size):
                if self.adjMatrix[start][i] != -1 and not visited[i]:
                    q.append(i)
                    visited[i] = True

        return l

# def main():
# directed graph
print('\nDirected Graph:')
# build graph
graph = Graph(5)
graph.set_vertex(0, 'a')
graph.set_vertex(1, 'b')
graph.set_vertex(2, 'c')
graph.set_vertex(4, 'e')
graph.set_vertex(3, 'd')
graph.set_edge('a', 'b')
graph.set_edge('a', 'd')
graph.set_edge('b', 'a')
graph.set_edge('b', 'c')
graph.set_edge('b', 'd')
graph.set_edge('c', 'd')
graph.set_edge('d', 'c')
graph.set_edge('d', 'e')
graph.set_edge('e', 'b')

# display graph
print(f'Vertices: {graph.get_vertices()}')
print(f'Adjacency Matrix: {graph.get_matrix()}')
print(f'Edges: {graph.get_edges()}')

# traversals
print('Depth-First Search')
print(f'DFS from \'a\': {graph.dfs("a")}')
print(f'DFS from \'b\': {graph.dfs("b")}')
print(f'DFS from \'c\': {graph.dfs("c")}')
print(f'DFS from \'d\': {graph.dfs("d")}')
print(f'DFS from \'e\': {graph.dfs("e")}')
print('Breadth-First Search')
print(f'BFS from \'a\': {graph.bfs("a")}')
print(f'BFS from \'b\': {graph.bfs("b")}')
print(f'BFS from \'c\': {graph.bfs("c")}')
print(f'BFS from \'d\': {graph.bfs("d")}')
print(f'BFS from \'e\': {graph.bfs("e")}')

# undirected graph:
print('\nUndirected Graph:')
# build graph
graph2 = Graph(5, False)
graph2.set_vertex(0, 'a')
graph2.set_vertex(1, 'b')
graph2.set_vertex(2, 'c')
graph2.set_vertex(4, 'e')
graph2.set_vertex(3, 'd')
graph2.set_edge('a', 'b')
graph2.set_edge('a', 'd')
graph2.set_edge('b', 'd')
graph2.set_edge('c', 'e')
graph2.set_edge('d', 'e')

# display graph
print(f'Vertices: {graph2.get_vertices()}')
print(f'Adjacency Matrix: {graph2.get_matrix()}')
print(f'Edges: {graph2.get_edges()}')

# traversals
print('Depth-First Search')
print(f'DFS from \'a\': {graph2.dfs("a")}')
print(f'DFS from \'b\': {graph2.dfs("b")}')
print(f'DFS from \'c\': {graph2.dfs("c")}')
print(f'DFS from \'d\': {graph2.dfs("d")}')
print(f'DFS from \'e\': {graph2.dfs("e")}')
print('Breadth-First Search')
print(f'BFS from \'a\': {graph2.bfs("a")}')
print(f'BFS from \'b\': {graph2.bfs("b")}')
print(f'BFS from \'c\': {graph2.bfs("c")}')
print(f'BFS from \'d\': {graph2.bfs("d")}')
print(f'BFS from \'e\': {graph2.bfs("e")}')