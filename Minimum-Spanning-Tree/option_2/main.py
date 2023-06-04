# The finality of this algorithm is to create a minimum spanning tree from a
# non directed graph, weighted and connected

def HasCycle(A):
    for o in range(len(A)):
        if state[o] == "not_visited":
            ancestor = o
            if FoundCycle(A, o, state, ancestor):
                return True
            
    return False


def FoundCycle(A, o, state, ancestor):
    state[o] = "visiting"

    for v in range(len(A)):
        if A[o][v] != -1 and v != ancestor and state[v] == "visiting":
            edge = [o, v, A[o][v]]
            cycle.append(edge)
            return True
        if A[o][v] != -1 and v == "not_visited":
            if FoundCycle(A, v, state, o):
                edge = [o, v, A[o][v]]
                cycle.append(edge)
                return True
            
    state = "visited"
    return False


# representation of the graph in a adjacency matrix,
# which the num of lines are the num of the vertex,
# the number inside the matrix will represent the weight of the edge
# -1 means that there isn't an edge connecting the vertices
V = [[-1, 5, 1, -1],[5, -1, 2, -1],[1, 2, -1, 3],[-1, -1, 3, -1]] 
#V = [[-1, 2, -1, 1, -1],[2, -1, 1, -1, -1],[-1, 1, -1, 4, 2],[1, -1, 4, -1, 3],[-1, -1, 2, 3, -1]] 

A = V
cycle = []

state = []
for n in range(len(A)):
    state.append("not_visited")

while HasCycle(A):
    heavy_edge = cycle[0]
    for m in cycle:
        if m[2] > heavy_edge[2]:
            heavy_edge = m
    A[heavy_edge[0]][heavy_edge[1]] = -1
    A[heavy_edge[1]][heavy_edge[0]] = -1

print(A)