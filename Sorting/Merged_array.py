def merged(left, right):
    result = []
    n, m = len(left), len(right)
    i, j = 0, 0

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append remaining elements
    if i < n:
        result.extend(left[i:])
    if j < m:
        result.extend(right[j:])

    return result


left = [1, 2, 3, 4]
right = [1, 2, 4, 5, 6]

print(merged(left, right))
