def bits(n):
  c = 0
  while n:
    x = n & 1
    c += x
    n = n >> 1
  if c % 2 == 0:
    return 1
  return 0

def sum_digits(n):
  sum_ = 0
  while n > 0:
    sum_ += n%10
    n = n // 10
  return sum_

n = int(input())
arr = list(map(int, input().split()))
sum_ = 0
for i in arr:
  if bits(i):
    sum_ += sum_digits(i)

print(sum_)
