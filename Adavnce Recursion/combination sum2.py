def backtrack(nums, index, target, subset, result):
    if target == 0:
        result.append(subset.copy())
        return
    if target < 0:
        return

    for i in range(index, len(nums)):
        # Skip duplicates
        if i > index and nums[i] == nums[i - 1]:
            continue

        subset.append(nums[i])
        backtrack(nums, i + 1, target - nums[i], subset, result)
        subset.pop()


def combinationSum2(nums, target):
    nums.sort()  # sort to handle duplicates
    result = []
    backtrack(nums, 0, target, [], result)
    return result


# --- User Input ---
nums = list(map(int, input("Enter numbers (space separated): ").split()))
target = int(input("Enter target sum: "))

print("Unique combinations are:")
print(combinationSum2(nums, target))
