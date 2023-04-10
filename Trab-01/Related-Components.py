V = [[1,3], [0,2], [1], [0], []]
Visitado = [False] * len(V)
Related = []

for o in range(len(V)):
    if Visitado[o] == False:
        Related.append(o)
        Visitado[o] = True
        for v in Related:
            for u in V[v]:
                if Visitado[u] == False:
                    Related.append(u)
                    Visitado[u] = True
        Related.sort()
        print(*Related)
        Related.clear()