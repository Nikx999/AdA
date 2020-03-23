def bfs(vertices, arr, start):
    queue = [start]
    visited = [0] * vertices
    while queue:
        a = queue.pop(0)
        for i in range(vertices):
            if arr[a][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
    for i, n in enumerate(visited):
        if n:
            print(i)

vertices = 4
arr = [[0,1,1,0], [0,0,0,1], [0,1,0,0], [0,0,0,0]]
start = 0
bfs(vertices, arr, start)

