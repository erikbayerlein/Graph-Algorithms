# Pensando por conta própria, escreva um algoritmo que receba como entrada
# Um grafo não-direcionado G = (V,E), com V = {0, ..., n-1}, e
# Um vértice o ∈ V ("origem"),
# e que então retorne um vetor d[0..n-1] tal que,
# para todo v ∈ V, d[v] = δ(o,v)
# (portanto, o algoritmo deve retornar um vetor com as distâncias de
# "o" a todos os outros vértices do grafo).

def NewEdge(origin, end):
    # finding a blanck space to write the end
    for i in range(0, n-1):
        if V[origin][i] == -1:
            V[origin][i] = end
            break
        else:
            continue

    # finding a blanck space to write the origin
    for j in range(0, n-1):
        if V[end][j] == -1:
            V[end][j] = origin
            break
        else:
            continue


def MakeGraph(n):
    # each location of the array will correspond to a vertex (0,...,n-1)
    V = []
    for i in range(0, n):
        # V will contain all the possible edges
        line = [-1]*(n-1)
        V.append(line)  

    return V


n = int(input("Please enter the number of vertices of the graph: "))
V = MakeGraph(n)

# adding edges to the graph
while True:
    origin = int(input("Please enter the origin of the edge: "))
    end = int(input("Please enter the end of the edge: "))
    if end == -1 or origin == -1:
        print("No more edges to add to the graph.\n")
        break
    else:
       NewEdge(origin, end)
       print("Edges added\n")

print(V)

o = int(input("\nChoose a vertex to know the distance to all the others: "))
Distance_from_O = [-1]*(n)
Distance_from_O[o] = 0

queue = []
queue.append(o)

# while queue is full (True)
while queue:
    u = queue.pop(0)
    # finding the neighbours of u
    for i in V[u]:
        if i == -1:
            break
        elif Distance_from_O[i] == -1:
            Distance_from_O[i] = Distance_from_O[u] + 1
            queue.append(i)

print("\n")
print(Distance_from_O)