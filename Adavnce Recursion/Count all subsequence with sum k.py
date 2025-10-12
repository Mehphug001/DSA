def backtrack(nums, ind, target, total):
    if total == target:
        return 1   # ✅ count this subset
    elif total > target:
        return 0
    if ind >= len(nums):
        return 0

    # include nums[ind]
    s = total + nums[ind]
    pick = backtrack(nums, ind + 1, target, s)

    # exclude nums[ind]
    not_pick = backtrack(nums, ind + 1, target, total)

    return pick + not_pick


nums = [4, 5, 9]
ind = 0
target = int(input("Enter the target: "))

n = backtrack(nums, ind, target, 0)

print("Number of subsets =", n)
