def floyd(adj, n):
  dist = adj.copy()
  for i in range(n):
    for j in range(n):
      for k in range(n):
        dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
  print(dist)
INF = 999999
vertices = 4
arr = [[0,5,INF,10], 
             [INF,0,3,INF], 
             [INF, INF, 0,   1], 
             [INF, INF, INF, 0] 
        ] 
floyd(arr, vertices)
