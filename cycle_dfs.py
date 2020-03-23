
def dfs_cycle(vertices, arr, start, stack):
    if start in stack:
        return True
    stack.append(start)
    for i in range(vertices):
        if arr[start][i]:
            if i == start:
                continue
            if i in stack:
                return True
            else:
                return dfs_cycle(vertices, arr, i, stack)
    return False


    
start = 0
vertices = 4
arr = [[0,0,1,1], [1,0,0,0], [0,1,0,0], [0,1,0,0]]
stack = []
if dfs_cycle(vertices, arr, start, stack):
    print("cycle present")
else:
    print("not present")

