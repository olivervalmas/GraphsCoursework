import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G, i):

    available_colors = [x for x in range(1, len(G.nodes)+1)]

    for neighbour in G.adj[i]:
        neighbour_color = G.node[neighbour]['color']
        if neighbour_color in available_colors:
            available_colors.remove(neighbour_color)

    return available_colors[0]


def greedy(G):

    k_max = 0

    for i in range(1, G.number_of_nodes()+1):
        smallest_color = find_smallest_color(G, i)
        G.nodes[i]['color'] = smallest_color
        if smallest_color > k_max:
            k_max = smallest_color

    print()

    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])

    print()
    print('The number of colors that Greedy computed is:', k_max)
    print()


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)