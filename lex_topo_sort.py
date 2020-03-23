def lex_topological_sort(vertices, arr):

    top = []
    in_degree = [0] * vertices
    for i in range(vertices):
        for j in range(vertices):
            if arr[i][j]:
                in_degree[j] += 1
    
    for i in range(vertices):
        if not in_degree[i]:
            top.append(i)
    count = len(top)
    i = 0
    top_order = []
    c = 0
    while i < count:
        mini = top[i]
        i = i + 1
        top_order.append(mini)
        for j in range(vertices):
            if arr[mini][j]:
                in_degree[j] -= 1
                if in_degree[j] == 0:
                    top.append(j)
                    count += 1
        c += 1
    if count != vertices:
        print(-1)
    else:
        print(top_order)
        

vertices = 6
arr = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,1,0,0], [0,1,0,0,0,0], [1,1,0,0,0,0], [1,0,1,0,0,0]]
lex_topological_sort(vertices, arr)
