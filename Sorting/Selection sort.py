def sort(arr):
    n = len(arr)
    for i in range(n):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[i], arr[min_ind] = arr[min_ind], arr[i]  # swap
    print(arr)

arr = [5, 7, 8, 4, 1, 6, 9, 2]
sort(arr)
