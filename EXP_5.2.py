# Initial values of Alpha and Beta
MAX = 1000
MIN = -1000

# Returns optimal value for current player
def alpha_beta_pruning(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition - leaf node is reached
    if depth == 3:
        return values[nodeIndex]
    
    if maximizingPlayer:
        best = MIN
        for i in range(0, 2):
            val = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        for i in range(0, 2):
            val = alpha_beta_pruning(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

# Driver code
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]
    print("The optimal value is:", alpha_beta_pruning(0, 0, True, values, MIN, MAX))