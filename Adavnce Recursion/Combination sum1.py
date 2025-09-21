def solve(index, curr_sum, subset, nums, target, result):
    if curr_sum == target:
        result.append(subset.copy())
        return
    if curr_sum > target or index >= len(nums):
        return

    # Pick nums[index]
    subset.append(nums[index])
    solve(index, curr_sum + nums[index], subset, nums, target, result)  # stay at same index (reuse allowed)
    subset.pop()

    # Skip nums[index]
    solve(index + 1, curr_sum, subset, nums, target, result)


def combinationSum(candidates, target):
    result = []
    solve(0, 0, [], candidates, target, result)
    return result


nums = list(map(int, input("Enter numbers (space separated): ").split()))
target = int(input("Enter target sum: "))

print("Unique combinations are:")
print(combinationSum(nums, target))
