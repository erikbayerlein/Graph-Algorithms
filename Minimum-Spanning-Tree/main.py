# The finality of this algorithm is to create a minimum spanning tree from a
# non directed graph, weighted and connected

import node_relatedComponents as nrc

# representation of the graph in a adjacency matrix,
# which the num of lines are the num of the vertex,
# the number inside the matrix will represent the weight of the edge
# -1 means that there isn't an edge connecting the vertices
V = [[-1, 3, 2, 1],[3, -1, 4, 4],[2, 4, -1, 2],[1, 4, 2, -1]] 


L = [] # list sorted by the weight of the edges
G_aux = V
aux = []

# L won't have double edges, like [0,1] and [1, 0]
for i in range(len(G_aux)):
    for j in range(len(G_aux[i])):
        if G_aux[i][j] != -1:
            aux.append(i)
            aux.append(j)
            aux.append(G_aux[i][j])
            G_aux[i][j] = -1
            G_aux[j][i] = -1
            L.append(aux)
            aux = []

# bubble sort adapted to order the list by weight
for i in range(len(L)-1, 0, -1):
    for j in range(i):
        if L[j][2] > L[j+1][2]:
            copy = L[j]
            L[j] = L[j+1]
            L[j+1] = copy


repr = [-1] * len(V) # array that will contain the representative of each related components


# in the beginning, each vertex is its representative
for i in range(len(V)):
    repr[i] = i


comp = [-1] * len(V) # array that will contain linked lists 


# each linked list will represent a connected component of the graph
for i in range(len(V)):
    new_node = nrc.Node(i, None) # a node will have the number of the vertex and a pointer to the next vertex in the connected component

    new_link_list = nrc.LinkedList()
    new_link_list.first = new_node
    new_link_list.last = new_link_list.first 
    new_link_list.length = 1

    comp[i] = new_link_list # adding the recently created linked list to its respective place in the Comp array
    

A = [] # the array which will contain the edges to make an minimum spanning tree


while len(A) != len(V)-1: # the condit
    edge = L.pop(0)

    if repr[edge[0]] != repr[edge[1]]:
        A.append(edge)
        rep_u = repr[edge[0]]
        rep_v = repr[edge[1]]

        if comp[rep_u].length < comp[rep_v].length:
            copy_u = rep_u
            rep_u = rep_v
            rep_v = copy_u

        first = comp[rep_v].first
        comp[rep_u].last.next = first
        comp[rep_u].last = comp[rep_v].last
        comp[rep_u].length = comp[rep_u].length + comp[rep_v].length

        while first != None:
            repr[first.elem] = rep_u
            first = first.next

print(A)