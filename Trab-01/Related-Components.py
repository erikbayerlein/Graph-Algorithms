#Escreva um programa que receba um grafo não-direcionado e que
#escreva as suas componentes conexas.
#Uma componente conexa é um conjunto maximal de vértices ligados por caminhos no grafo

import sys

def num_of_vertices(data):
    # using enumerate to have the information and the number of the exact line (i)
    for i, line in enumerate(data):
        if i == 2:
            # ["n", "number of vertices"]
            aux = line.split("=")
            n = int(aux[1])

    return n


def make_graph(n, data):
    # first create a graph V (adjacency list) which will contain the edges
    V = []
    for i in range(0, n):
        V.append([])

    # using enumerate to have the information and the number of the exact line (i)
    for i, line in enumerate(data):
        # all the vertices are after the fourth line
        if i >= 4:
            aux = line.split()
            # turning the strings into int
            origin, end = (int(aux[0]), int(aux[1]))
            # adding the edges to the graph
            V[origin - 1].append(end - 1)
            V[end - 1].append(origin - 1)
    
    return V


def related_components(V):
    Visited = [False] * len(V)
    Related = []

    # going through all the vertices
    for o in range(len(V)):
        # if the vertex have been visited, skip it
        if Visited[o] == False:
            # add the vertex to the related list
            Related.append(o)
            Visited[o] = True
            # going through the related list to visit the neighbors of the vertices
            for v in Related:
                # u is going to be the neighbor
                for u in V[v]:
                    if Visited[u] == False:
                        # add the vertex (neighbor) to the related list to visit its neighbors
                        Related.append(u)
                        Visited[u] = True
            # formatting the output
            Related.sort()
            for i in range(len(Related)):
                Related[i] += 1
            print(*Related)
            # when all the related components have been detected, we need to clear the list for the next components
            Related.clear()

            
# reading the input in the run codes platform
data = sys.stdin.readlines()

# if there's necessity to test the code,
# go to the tests folder and copy an input into the test.txt file
# need to comment line 66
'''with open('test.txt') as f:
    data = f.readlines()'''

n = num_of_vertices(data)
V = make_graph(n, data)
related_components(V)
