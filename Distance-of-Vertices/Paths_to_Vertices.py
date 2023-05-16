# 2. Escreva uma variação do algoritmo da aula de hoje que,
# ao invés de retornar um vetor com as distâncias, retorne um vetor c[0..n-1]
# de listas encadeadas: para cada v ∈ V, a lista encadeada em c[v]
# deve ser uma sequência de vértices correspondente a um caminho mínimo
# de "o" a "v", isto é, um caminho com δ(o,v) arestas;
# se não houver caminho de "o" a "v", c[v] deve ser uma lista vazia (ponteiro nulo).

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


def ChangeLayers():
    for i in Next_Layer:
        Current_Layer.append(i)
    Next_Layer.clear()

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

V = [[3, 5, 2, -1, -1], [3, 4, -1, -1, -1], [0, -1, -1, -1, -1], [0, 1, 4, -1, -1], [3, 1, -1, -1, -1], [0, -1, -1, -1, -1]]

print(V)

o = int(input("\nChoose a vertex to know the distance to all the others: "))
Paths_from_O = []

for i in range(0, n):
    # Paths_from_O will contain the fastest path
    line = []*(n-1)
    Paths_from_O.append(line)

distance = 0
Current_Layer = [o]
Next_Layer = []

Visited = [False]*n
Visited[o] = True

# while Current_Layer is full
while Current_Layer:
    # going through the Current_Layer (each v is a vertex of the current layer)
    for v in Current_Layer:
        # u is going to be a the end of the edge of the vertex v
        for u in V[v]:
            # if u wasn't visited yet, which means that it is in the next layer
            if u != -1 and Visited[u] == False:
                Paths_from_O[u].append(u)
                Visited[u] = True
                Next_Layer.append(u)
            for i in V[u]:
                if i != -1:
                    Paths_from_O[u].append(i)
    # clear Current_Layer and change the values of both arrays (Current_Layer <-> Next_Layer)
    Current_Layer.clear()
    ChangeLayers()
    distance += 1

print(Paths_from_O)