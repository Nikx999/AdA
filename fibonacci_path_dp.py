n = int(input())
start = int(input())
arr = list(map(int, input().split()))
arr = arr[start:]
n = n - start
fibo = []
a = 0
b = 1
while b < n:
  a, b = b, a+b
  fibo.append(b)
path = [0] * n
for i in range(n):
  if arr[i] == 0:
    continue
  temp = []
  for j in fibo:
    if j <= i and arr[i-j] != 0:
      temp.append(path[i - j] + 1)
  if len(temp) != 0:
    path[i] = min(temp)

print(path[n -1])
