import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

### count the length of the path between two pre-specified vertices a and b, using Depth-First-Search


def dfs(G, a, b, u):
    
    # label represents the distance from the starting node
    # sets label of starting node to 0
    G.nodes[a]['label'] = 0

    # checks if the end node has been visited

    if G.nodes[b]['visited'] == 'no':

        # sets the current node to visited

        G.nodes[u]['visited'] = 'yes'
        print(u)
        adjacent = list(G.adj[u])
        adjacent.sort()

        # carries out dfs on all adjacent nodes to u in ascending order if they haven't already been visited

        for v in adjacent:
            if G.nodes[v]['visited'] == 'no':
                G.nodes[v]['label'] = G.nodes[u]['label'] + 1
                dfs(G, a, b, v)


print()
G6=graph6.Graph()
a=12
b=40
print('Depth-First-Search visited the following nodes of G6 in this order:')
dfs(G6,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G6 between vertices', a, 'and', b, 'of length', G6.node[b]['label'])
print()


G7=graph7.Graph()
a=5
b=36
print('Depth-First-Search visited the following nodes of G7 in this order:')
dfs(G7,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G7 between vertices', a, 'and', b, 'of length', G7.node[b]['label'])
print()


G8=graph8.Graph()
a=15
b=40
print('Depth-First-Search visited the following nodes of G8 in this order:')
dfs(G8,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G8 between vertices', a, 'and', b, 'of length', G8.node[b]['label'])
print()


G9=graph9.Graph()
a=1
b=19
print('Depth-First-Search visited the following nodes of G9 in this order:')
dfs(G9,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G9 between vertices', a, 'and', b, 'of length', G9.node[b]['label'])
print()


G10=graph10.Graph()
a=6
b=30
print('Depth-First-Search visited the following nodes of G10 in this order:')
dfs(G10,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G10 between vertices', a, 'and', b, 'of length', G10.node[b]['label'])
print()
