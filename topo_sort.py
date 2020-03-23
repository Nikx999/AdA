def topo_sort(i, arr, stack, visited, vertices):
    visited[i] = 1
    for j in range(vertices):
        if not visited[j] and arr[i][j]:
            topo_sort(j, arr, stack, visited, vertices)
    stack.append(i)

def topological_sort(vertices, arr):
    visited = [0] * vertices
    stack = []
    for i in range(vertices):
        if not visited[i]:
            topo_sort(i, arr, stack, visited, vertices)
    i = vertices
    while i > 0:
        print(stack.pop() + 1)
        i -= 1

vertices = 6
arr = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,1,0,0], [0,1,0,0,0,0], [1,1,0,0,0,0], [1,0,1,0,0,0]]
topological_sort(vertices, arr)
