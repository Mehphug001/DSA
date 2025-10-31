def solve(nums, ind, subset, result):
    if ind >= len(nums):
        result.append(subset.copy())   # store one subset
        return

    # include nums[ind]
    subset.append(nums[ind])
    solve(nums, ind + 1, subset, result)

    # exclude nums[ind]
    subset.pop()
    solve(nums, ind + 1, subset, result)


def countPartitions(nums, d):
    total = sum(nums)
    result = []
    subset = []

    # Step 1: generate all subsets
    solve(nums, 0, subset, result)

    # Step 2: count valid partitions
    count = 0
    for s1 in result:
        sum1 = sum(s1)
        sum2 = total - sum1
        if sum1 >= sum2 and abs(sum1 - sum2) == d:
            count += 1

    return count


# 🔹 Example Test Cases
print(countPartitions([5, 2, 6, 4], 3))      # ✅ Output: 1
print(countPartitions([1, 1, 1, 1], 0))      # ✅ Output: 6
print(countPartitions([1, 2, 1, 0, 1, 3, 3], 11))  # ✅ Output: 2
