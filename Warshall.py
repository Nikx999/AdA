def warshall(adj, n):
  for i in range(n):
    for j in range(n):
      for k in range(n):
        if adj[j][k] != 1 and adj[j][i] == adj[i][k] == 1:
          adj[j][k] = 1
  print(adj)

vertices = 4
arr = [[0,0,0,0], [0,0,1,1], [0,1,0,0], [1,0,1,0]]
warshall(arr, vertices)
