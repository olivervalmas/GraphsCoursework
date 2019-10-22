import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):

    all_adjacent_to_colored = []

    for vertex in G.nodes:
        # print(vertex)
        if G.nodes[vertex]['color'] != 'never coloured':
            # print(G.nodes[vertex])
            for adjacent_to_colored in G.adj[vertex]:
                if G.nodes[adjacent_to_colored]['color'] == 'never coloured':
                    all_adjacent_to_colored.append(adjacent_to_colored)

    if all_adjacent_to_colored == []:
        return False

    return min(all_adjacent_to_colored)

def find_smallest_color(G,i):

    available_colors = [x for x in range(1, len(G.nodes) + 1)]

    for neighbour in G.adj[i]:
        neighbour_color = G.node[neighbour]['color']
        if neighbour_color in available_colors:
            available_colors.remove(neighbour_color)

    return available_colors[0]


def greedy(G):

    kmax = []
    all_colored_status = []

    for vertex in G.nodes:
        all_colored_status.append(G.nodes[vertex]['color'])

    G.nodes[1]['color'] = 1

    while 'never coloured' in all_colored_status:

        next_vertex = find_next_vertex(G)

        if not next_vertex:
            break

        new_color = find_smallest_color(G, next_vertex)

        kmax.append(new_color)
        G.nodes[next_vertex]['color'] = new_color

        for vertex in G.nodes:
            all_colored_status.append(G.nodes[vertex]['color'])

    kmax = max(kmax)

    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
# print(find_next_vertex(G))
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)