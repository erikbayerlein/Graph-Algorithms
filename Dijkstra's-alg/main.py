def AddToHeap():
    for i in range(len(Heap)/2, -1, 1):
        Down(i)

def Down(i):
    l = Left(i)
    r = Right(i)
    n = len(Heap)
    if l <= n and Heap[l] > Heap[i]:
        x = l
    else:
        x = r
    
    if r <= n and Heap[r] > Heap[x]:
        x = r
    if x != i:
        copy = Heap[i]
        Heap[i] = Heap[x]
        Heap[x] = copy
        Down(x)

def Anc(i):
    return int(Heap[i/2])

def Left(i):
    return Heap[2*i]

def Right(i):
    return Heap[2*i + 1]

def RemoveMinimum(Heap):
    return

def WeightInHeap(v):
    return

def UpdateWeight(s):
    return


V = [[1,3], [0, 2, 3, 5], [1, 4, 5], [0, 1, 4], [2, 3], [1, 2]] # all the vertices and its edges
V_in = [[], [0, 5], [1], [0, 1, 4], [2], [2]] # arrival neighborhood
V_out = [[1, 3], [2, 3], [4, 5], [], [3], [1]] # exit neighborhood

distance = [-1] * len(V)
ancestor = [-1] * len(V)

Heap = []


while len(Heap) != 0:
    u, w = RemoveMinimum(Heap)
    distance[u] = w
    for v in V_out[u]:
        if distance == -1:
            weight_through_u = w + V[u][v]
            if v not in Heap:
                AddToHeap([v, weight_through_u])
                ancestor[v] = u
            else:
                if weight_through_u < WeightInHeap(v):
                    UpdateWeight([v, weight_through_u])
                    ancestor[v] = u

print(distance)
print(ancestor)