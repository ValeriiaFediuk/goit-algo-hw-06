import heapq
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edge("Нетішин", "Шепетівка", weight=40)
G.add_edge("Шепетівка", "Старокостянтинів", weight=54)
G.add_edge("Нетішин", "Старокостянтинів", weight=93)
G.add_edge("Старокостянтинів","Хмельницький", weight=111)
G.add_edge("Хмельницький", "Ярмолинці", weight=38)
G.add_edge("Хмельницький", "Дунаївці", weight=65)
G.add_edge("Ярмолинці", "Дунаївці", weight=37)
G.add_edge("Дунаївці", "Кам'янець-Подільський", weight=33)


def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths

shortest_paths = dijkstra(G, "Дунаївці")
print(f"Найкоротші шляхи: {shortest_paths}")

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight = "bold", width=1)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()
