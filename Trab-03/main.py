import sys

def numOfVertices(data):
    for i, line in enumerate(data):
        if i == 2:
            # ["n", "number of vertices"]
            aux = line.split("=")
            n = int(aux[1])
    return n

def graph(data):
    Graph = [[0]*n for _ in range(n)]

    for i, line in enumerate(data):
        if i >= 4:
            v, u, cap = line.split(" ")
            v = int(v)
            u = int(u)
            Graph[v-1][u-1] = float(cap)

    return Graph

def BFS(Graph, n, o, d, ancestral):

    queue = []
    queue.append(o)
    visited = [False]*n
    visited[o] = True

    while queue:
        u = queue.pop(0)
        for i, v in enumerate(Graph[u]):
            if not visited[i] and v > 0:
                queue.append(i)
                visited[i] = True
                ancestral[i] = u
                if i == d:
                    return True
    return False

def FordFulkerson(V, origin, destiny):
    
    n = len(V)
    V_aux = [row[:] for row in V]
    ancestral = [-1]*n
    max_flow = 0

    while BFS(V_aux, n, origin, destiny, ancestral):

        s = destiny
        path_flow = float("Inf")

        while s != origin:
            path_flow = min(path_flow, V_aux[ancestral[s]][s])
            s = ancestral[s]

        max_flow += path_flow
        v = destiny

        while (v != origin):
            u = ancestral[v]
            V_aux[u][v] -= path_flow
            V_aux[v][u] += path_flow
            v = ancestral[v]

    return max_flow


# reading the input in the run codes platform
data = sys.stdin.readlines()

# if there's necessity to test the code,
# go to the tests folder and copy an input into the tests.txt file
# need to comment line 96
'''with open('pathToTests.txt') as f:
    data = f.readlines()'''

n = numOfVertices(data)
V = graph(data)

origin = 0
for i in range(1, n):
    flow = FordFulkerson(V, origin, i)
    print(f"{i+1} {int(flow) if int(flow) == flow else flow}")