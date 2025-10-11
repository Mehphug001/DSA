def backtrack(start, k, n, subset, result):
    # Base cases
    if n == 0 and len(subset) == k:
        result.append(subset.copy())
        return
    if n < 0 or len(subset) > k:
        return

    # Try numbers from 'start' to 9
    for i in range(start, 10):
        subset.append(i)
        backtrack(i + 1, k, n - i, subset, result)
        subset.pop()


def combinationSum3(k, n):
    result = []
    backtrack(1, k, n, [], result)
    return result


# --- User Input ---
k = int(input("Enter k (number of elements): "))
n = int(input("Enter n (target sum): "))

print("Valid combinations are:")
print(combinationSum3(k, n))
