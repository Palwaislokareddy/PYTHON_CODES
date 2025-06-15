def second_largest_greedy(arr):
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif second < num < first:
            second = num
    return second if second != float('-inf') else "No second largest element"
# Input
arr = list(map(int, input("Enter numbers: ").split()))
print("Second largest:", second_largest_greedy(arr))
