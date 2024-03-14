def max(a, b):
    return a if a > b else b

def knapsack(values, weights, n, capacity):
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of knapsack: "))
    N = int(input("Enter the number of items: "))
    values = []
    weights = []

    for i in range(N):
        values.append(int(input(f"Enter the value I[{i + 1}]: ")))
        weights.append(int(input(f"Enter the weight W[{i + 1}]: ")))

    max_value = knapsack(values, weights, N, capacity)
    print("Tushar Bhatia")
    print("A2305221202")
    print(f"Maximum value that can be obtained: {max_value}")
