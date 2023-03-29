# 1. (Este exercício contempla diferentes alternativas de implementação,
# algumas das quais foram mencionadas na aula de hoje)
# Escreva uma variação do algoritmo da aula de hoje que atenda a todos os requisitos a seguir:
# Não utilize um vetor para armazenar as distâncias,
# que devem passar a ser apenas impressas na tela (use um comando "imprima"
# em pseudocódigo, e omita a pós-condição;
# o algoritmo ainda deve funcionar corretamente, mas não é necessário redigir a especificação).
# Utilize um vetor de booleanos para saber quais vértices já foram atingidos.
# Ao invés de 1 fila, use 2 conjuntos:
# o conjunto "A" dos vértices da "camada atual" e o conjunto "P" dos vértices da "próxima camada".
# Presuma que um conjunto "C" possui as operações "C.vazio()",
# que informa se "C" está vazio, "C.inserir(v)",
# que insere "v" em "C", e "u := C.remover()",
# que remove e retorna algum elemento de C (sem qualquer
# garantia sobre qual elemento do conjunto é removido e retornado).
# Outra operação disponível é trocar o conteúdo de dois conjuntos.
# Utilize uma variável numérica para armazenar a distância
# até os vértices da camada atual, e utilize os conjuntos A e P para saber quando incrementá-la.


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

print(V)

o = int(input("\nChoose a vertex to know the distance to all the others: "))

distance = 0
Current_Layer = [o]
Next_Layer = []

Visited = [False]*n
Visited[o] = True

# while Current_Layer is full
while Current_Layer:
    print(f"\nThe distance from the origin to {Current_Layer} is {distance}")

    # going through the Current_Layer (each v is a vertex of the current layer)
    for v in Current_Layer:
        # u is going to be a the end of the edge of the vertex v
        for u in V[v]:
            # if u wasn't visited yet, which means that it is in the next layer
            if u != -1 and Visited[u] == False:
                Visited[u] = True
                Next_Layer.append(u)
    # clear Current_Layer and change the values of both arrays (Current_Layer <-> Next_Layer)
    Current_Layer.clear()
    ChangeLayers()
    distance += 1

