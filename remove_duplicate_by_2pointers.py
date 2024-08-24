def remove_duplicate(arr):
    # using two-pointers approach
    n = len(arr)
    i = 0

    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return arr[:i+1]

print(remove_duplicate([1, 2, 2, 3, 3, 3, 4, 5]))