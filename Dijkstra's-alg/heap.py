class heap:
    H = []

    def AddToHeap(x):
        heap.H.append(x)

    def anc(i):
        return int(heap[i/2])
    
    def left(i):
        return heap[2*i]
    
    def right(i):
        return heap[2*i + 1]
    
