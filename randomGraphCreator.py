import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

def boolean_with_chance(p):
    return random.random() < p

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(vertices)]

    def add_edge(self, u, v):
         if v not in self.graph[u]:
            self.graph[u].append(v)
            self.graph[v].append(u)
        
    def print_adj_list(self):
        for i, vertex in enumerate(self.graph):
            print(f"Vertex {i} -> {vertex}")
            
    def visualize(self):
        G = nx.Graph()
        for i in range(self.V):
            G.add_node(i)
        for i in range(self.V):
            for j in self.graph[i]:
                G.add_edge(i, j)
        nx.draw(G, with_labels=True)
        plt.show()
        
    def countComponents(self):
        visited = [False] * (self.V)
        count = 0

        def dfs(v):
            visited[v] = True
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for i in range(self.V):
            if not visited[i]:
                dfs(i)
                count += 1

        return count
    
    def findDiameter(self):
        diameter = 0
        components = self.countComponents()
        
        for i in range(self.V):
            visited = [False]*(self.V)
            q = deque()
            q.append(i)
            visited[i] = True
            distance = defaultdict(int)
            while len(q) != 0:
                u = q.popleft()
                for v in self.graph[u]:
                    if visited[v] == False:
                        q.append(v)
                        visited[v] = True
                        distance[v] = distance[u] + 1
                        diameter = max(diameter, distance[v])
        
        if(components > 1):
            return (f"Diameter: infinity Components: {components} Diameter of connected components {diameter}")
        
        return (f"Diameter: {diameter} Components: {components} Diameter of connected components {diameter}")
    
N = 3000
P = 0.0001
        
g = Graph(N)

for edgeFrom in range(0, N):
        for edgeTo in range(0, N):
            if(boolean_with_chance(P) and edgeFrom != edgeTo):
                g.add_edge(edgeFrom, edgeTo)
                

                