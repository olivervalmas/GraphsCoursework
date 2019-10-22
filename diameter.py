import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10


def bfs(G,a,b):

    if a == b:
        return 0

    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.node[a]['label'] = 0

    i = 0

    while G.node[b]['label'] == -1:
        for u in G.nodes:
            if G.node[u]['label'] == i:
                adjacent_to_u = G.adj[u]
                for v in adjacent_to_u:
                    if G.node[v]['label'] == -1:
                        G.node[v]['label'] = i + 1
        i += 1

    return G.node[b]['label']




def max_distance(G):
    all_distances = set()
    for i in G.nodes():
        for j in G.nodes():
            all_distances.add(bfs(G,i,j))

    return max(all_distances)


print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()
