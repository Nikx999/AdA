
def dfs(vertices, arr, start, visited):
    
    visited[start] = 1
    for i in range(vertices):
            if arr[start][i] and not visited[i]:
                dfs(vertices, arr, i, visited)
    return 


    
start = 0
vertices = 6
visited = [0] * vertices
arr = [[0,1,1,1,0,0], [1,0,0,0,0,0], [1,0,0,1,1,0], [1,0,1,0,0,0], [0,0,1,0,0,0], [0,0,0,0,0,0]]
dfs(vertices, arr, start, visited)
count = 0
for i, n in enumerate(visited):
    if n:
        count += 1
if count == vertices:
    print("connected")
else:
    print("not_connected")

