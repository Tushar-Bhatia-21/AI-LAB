class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit
        self.ratio = profit / weight

def partition(arr, low, high):
    pivot = arr[high].ratio
    i = low - 1

    for j in range(low, high):
        if arr[j].ratio >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)

def knapsack(arr, capacity):
    profit = 0.0
    for item in arr:
        if item.weight <= capacity:
            profit += item.profit
            capacity -= item.weight
        else:
            profit += item.ratio * capacity
            break
    return profit

if __name__ == "__main__":
    print("\nTushar Bhatia")
    print("A2305221202")
    n = int(input("Enter the number of items: "))
    items = []
    print("Enter the weight and profit of each item:")
    for i in range(n):
        print(f"Item {i+1}:")
        weight = int(input("Weight: "))
        profit = int(input("Profit: "))
        items.append(Item(weight, profit))
    capacity = int(input("Enter the capacity of knapsack: "))
    sort(items)
    max_profit = knapsack(items, capacity)
    print(f"Maximum profit: {max_profit}")
