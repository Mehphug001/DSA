def solve(nums, ind, subset, result):
    if ind >= len(nums):
        result.append(subset.copy())   # save one subset
        return

    # include nums[ind]
    subset.append(nums[ind])
    solve(nums, ind+1, subset, result)

    # exclude nums[ind]
    subset.pop()
    solve(nums, ind+1, subset, result)


nums = [5, 9, 7]
subset = []
result = []
ind = 0

solve(nums, ind, subset, result)
print(result)
