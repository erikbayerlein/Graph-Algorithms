# Algorithm to verify if a directed graph has a circuit or not

def NewEdge(origin, end):
    # finding a blanck space to write the end
    for i in range(0, n-1):
        if V_out[origin][i] == -1:
            V_out[origin][i] = end
            V[origin][i] = end
            break
        else:
            continue

    # finding a blanck space to write the origin
    for j in range(0, n-1):
        if V_in[end][j] == -1:
            V_in[end][j] = origin
            V[end][i] = origin
            break
        else:
            continue


def MakeGraph(n):
    # each location of the array will correspond to a vertex (0,...,n-1)
    V = []
    V_in = []
    V_out = []
    for i in range(0, n):
        # V will contain all the possible edges
        line = [-1]*(n-1)
        V_in.append(line)  
        V_out.append(line)  
        V.append(line)

    return V_in, V_out, V


def hasCircuit():
    for o in range(len(V)):
        if state[o] == "not visited":
            if foundCircuit(state, o):
                return True
    return False


def foundCircuit(state, u):
    state[u] = "visiting"
    for v in V_out[u]:
        if state[v] == "visiting":
            return True
        if state[v] == "not visited":
            if foundCircuit(state, v):
                return True
    state[u] = "visited"
    return False


n = int(input("Please enter the number of vertices of the graph: "))
V_in, V_out, V = MakeGraph(n) # two types of neighbours # this line will be edited


# Fill the graph here
#V = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]] # all the vertices and its edges
#V_in = [[3], [0], [0, 1], [2]] # arrival neighborhood
#V_out = [[1, 2], [2], [3], [0]] # exit neighborhood

V = [[1,3], [0, 2, 3, 5], [1, 4, 5], [0, 1, 4], [2, 3], [1, 2]] # all the vertices and its edges
V_in = [[], [0, 5], [1], [0, 1, 4], [2], [2]] # arrival neighborhood
V_out = [[1, 3], [2, 3], [4, 5], [], [3], [1]] # exit neighborhood


state = ["not visited"]*n # three states: not visited, visiting and visited

if hasCircuit():
    print("The graph has circuit")
else:
    print("The graph doesnt have circuit")
