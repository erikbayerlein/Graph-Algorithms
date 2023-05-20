# The finality of this algorithm is to create a minimum spanning tree from a
# non directed graph, weighted and connected
# and return the total weight of the tree

import sys

class Node:
    def __init__(self, elem, next):
        self.elem = elem
        self.next = next
        
class LinkedList:
        first = None
        last = None
        length = None


def numOfVertices(data):
    for i, line in enumerate(data):
        if i == 2:
            # ["n", "number of vertices"]
            aux = line.split("=")
            n = int(aux[1])
    return n

def graph(data):
    V = []
    for i, line in enumerate(data):
        if i >= 4:
            aux = line.split()
            aux[0], aux[1], aux[2] = int(aux[0]), int(aux[1]), float(aux[2])
            V.append(aux)
    return V

def orderWeightedGraph(V):
    return V.sort(key=lambda x: x[2])

def representativesList(n):
    repr = [-1] * (n) # array that will contain the representative of each related components
    # in the beginning, each vertex is its representative
    for i in range(n):
        repr[i] = i + 1
    return repr

def connectedCompList(n):
    comp = [-1] * n # array that will contain linked lists 
    # each linked list will represent a connected component of the graph
    for i in range(n):
        new_node = Node(1 + i, None) # a node will have the number of the vertex and a pointer to the next vertex in the connected component
        
        new_link_list = LinkedList()
        new_link_list.first = new_node
        new_link_list.last = new_link_list.first 
        new_link_list.length = 1

        comp[i] = new_link_list # adding the recently created linked list to its respective place in the Comp array
    return comp

def totalWeightAGM(n, L, repr, comp):
    A = [] # the array which will contain the edges to make an minimum spanning tree
    total_weight = 0

    while len(A) != n-1: # A will be a minimum spanning tree when its length = lenght of V - 1
        edge = L.pop(0) # analyze the first edge

        if repr[edge[0] - 1] != repr[edge[1] - 1]: # if the representatives are equal to each other, the vertices are in the same connected component
            A.append(edge) # add the edge to A
            total_weight += A[-1][2] # adding the weights
            rep_u = repr[edge[0] - 1] # rep_u will be the representative of an end of the edge
            rep_v = repr[edge[1] - 1] # rep_v will be the representative of the other end of the edge

            if comp[rep_u - 1].length < comp[rep_v - 1].length: # update the rep to the smallest connected component
                copy_u = rep_u
                rep_u = rep_v
                rep_v = copy_u

            first = comp[rep_v - 1].first # first = the first node of the linked list of the rep of v
            comp[rep_u - 1].last.next = first # the next of the last node of the linked list of the rep of u will point to first
            comp[rep_u - 1].last = comp[rep_v - 1].last # the last node of the linked list of u will point to the last node of the linked list of the rep of v
            comp[rep_u - 1].length = comp[rep_u - 1].length + comp[rep_v - 1].length # sum of the lengths of the linked lists

            while first != None: # changing all the reps of the linked list of v to the reps of u
                repr[first.elem - 1] = rep_u 
                first = first.next

    print ("%.3f" %total_weight)


# reading the input in the run codes platform
data = sys.stdin.readlines()

# if there's necessity to test the code,
# go to the tests folder and copy an input into the test.txt file
# need to comment line 96
'''with open('/Users/erikbayerlein/Documents/GitHub/Graph-Algorithms/Trab-02/tests.txt') as f:
    data = f.readlines()'''

n = numOfVertices(data)
V = graph(data)
L = orderWeightedGraph(V)
repr = representativesList(n)
comp = connectedCompList(n)
totalWeightAGM(n, L, repr, comp)