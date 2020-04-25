def optimal_weight(capacity, weights, n):
    optimal = [[0 for i in range(capacity + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            optimal[i][j] = optimal[i - 1][j]
            if weights[i - 1] <= j:
                val = optimal[i - 1][j - weights[i - 1]] + weights[i - 1]
                if val > optimal[i][j]:
                    optimal[i][j] = val
            
    return optimal[n][capacity]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
