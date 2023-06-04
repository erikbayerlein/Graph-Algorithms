# The finality of this algorithm is to create a minimum spanning tree from a
# non directed graph, weighted and connected

import node_relatedComponents as nrc

# representation of the graph in a adjacency matrix,
# which the num of lines are the num of the vertex,
# the number inside the matrix will represent the weight of the edge
# -1 means that there isn't an edge connecting the vertices
V = [[-1, 2, -1, 1, -1],[2, -1, 1, -1, -1],[-1, 1, -1, 4, 2],[1, -1, 4, -1, 3],[-1, -1, 2, 3, -1]] 


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

L.sort(key=lambda x: x[2])

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


while len(A) != len(V)-1: # A will be a minimum spanning tree when its length = lenght of V - 1
    edge = L.pop(0) # analyze the first edge

    if repr[edge[0]] != repr[edge[1]]: # if the representatives are equal to each other, the vertices are in the same connected component
        A.append(edge) # add the edge to A
        rep_u = repr[edge[0]] # rep_u will be the representative of an end of the edge
        rep_v = repr[edge[1]] # rep_v will be the representative of the other end of the edge

        if comp[rep_u].length < comp[rep_v].length: # update the rep to the smallest connected component
            copy_u = rep_u
            rep_u = rep_v
            rep_v = copy_u

        first = comp[rep_v].first # first = the first node of the linked list of the rep of v
        comp[rep_u].last.next = first # the next of the last node of the linked list of the rep of u will point to first
        comp[rep_u].last = comp[rep_v].last # the last node of the linked list of u will point to the last node of the linked list of the rep of v
        comp[rep_u].length = comp[rep_u].length + comp[rep_v].length # sum of the lengths of the linked lists

        while first != None: # changing all the reps of the linked list of v to the reps of u
            repr[first.elem] = rep_u 
            first = first.next

print(A)