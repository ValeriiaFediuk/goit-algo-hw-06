import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

cities = ["Хмельницький", "Кам'янець-Подільський", "Шепетівка", "Старокостянтинів", "Ярмолинці", "Дунаївці","Нетішин"]
G.add_nodes_from(cities)

roads = [("Нетішин", "Шепетівка"), 
         ("Шепетівка", "Старокостянтинів"),
         ("Нетішин", "Старокостянтинів"), 
         ("Старокостянтинів","Хмельницький"), 
         ("Хмельницький", "Ярмолинці"), 
         ("Хмельницький", "Дунаївці"),
         ("Ярмолинці", "Дунаївці"),
         ("Дунаївці", "Кам'янець-Подільський")]

G.add_edges_from(roads)

plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=1500, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Транспортна мережа Хмельницької області")
plt.show()

print("Кількість вершин (міст):", G.number_of_nodes())
print("Кількість ребер (шляхів):", G.number_of_edges())
print("Ступінь вершин:")
for city in G.nodes():
    print(f"{city}: {G.degree(city)}")
