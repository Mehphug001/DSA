def solve(nums, ind, subset, target, result, total):
    if total == target:
        result.append(subset.copy())
        return
    elif total > target:
        return
    if ind >= len(nums):
        return

    # include nums[ind]
    subset.append(nums[ind])
    solve(nums, ind + 1, subset, target, result, total + nums[ind])

    # exclude nums[ind]
    subset.pop()
    solve(nums, ind + 1, subset, target, result, total)


nums = [4,5,9]
subset = []
result = []
ind = 0
target=int(input("Enter the target :"))  # example target

solve(nums, ind, subset, target, result, 0)
print(result)
