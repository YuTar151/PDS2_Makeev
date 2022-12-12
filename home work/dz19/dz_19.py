import networkx as nx
import matplotlib.pyplot as plt

def list_edit():
    global edgelist
    edgelist = []
    filename = "D:\OneDrive\PythonProjects\Study\home work\dz19\cities.csv"
    with open(filename, 'r') as file:
        for i in file:
            line = i.split(";")
            line[2] = int(line[2])
            edgelist.append(line)

    return edgelist

list_edit()

g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight = edge[2])

print(nx.shortest_path(g, 'Kremenets', 'Yuzhnoukrainsk', weight='weight'))
print(nx.shortest_path_length(g, 'Kremenets', 'Yuzhnoukrainsk', weight='weight'))

nx.draw_networkx(g)
pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Graph Generation")
plt.show()

