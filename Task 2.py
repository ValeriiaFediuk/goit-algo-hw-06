import networkx as nx
from collections import deque

G = nx.Graph()

G.add_edges_from([("Нетішин", "Шепетівка"), 
         ("Шепетівка", "Старокостянтинів"),
         ("Нетішин", "Старокостянтинів"), 
         ("Старокостянтинів","Хмельницький"), 
         ("Хмельницький", "Ярмолинці"), 
         ("Хмельницький", "Дунаївці"),
         ("Ярмолинці", "Дунаївці"),
         ("Дунаївці", "Кам'янець-Подільський")])


def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    if start not in visited: 
        visited.add(start)
        if parent is not None:
            path.append((parent, start)) 
        for next in graph[start]:
            dfs(graph, next, visited, path, start)
    return path


def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    return path



dfs_result = dfs(G, "Дунаївці")

bfs_result = bfs(G, "Дунаївці")

print(f"Шляхи, знайдені за допомогою DFS: {dfs_result}")

print(f"\nШлях, знайдений за допомогою BFS: {bfs_result}")

