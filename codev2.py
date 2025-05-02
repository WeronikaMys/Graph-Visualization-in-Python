import networkx as nx
import matplotlib.pyplot as plt

def read_adjacency_list(file_path):
    graphs = []
    current_graph = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):  # Pusta linia lub komentarz
                if current_graph:
                    graphs.append(current_graph)
                    current_graph = {}
                continue
            
            node, neighbors = line.split(":")
            node = node.strip()
            neighbors = neighbors.strip().split()
            current_graph[node] = neighbors
        
        if current_graph:
            graphs.append(current_graph)
    
    return graphs

def plot_graphs(graphs):
    for i, adj_list in enumerate(graphs, start=1):
        G = nx.Graph()
        for node, neighbors in adj_list.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)
        
        plt.figure(figsize=(6, 4))
        nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10)
        plt.title(f"Graf {i}")
        plt.show()

file_path = "grafy.txt"

graphs = read_adjacency_list(file_path)
plot_graphs(graphs)
