def backtrack(nums, ind, target, total):
    if total == target:
        return True  # ✅ explicitly return True when found

    if total > target:
        return False
    if ind >= len(nums):
        return False

    # include nums[ind]
    s = total + nums[ind]
    pick = backtrack(nums, ind + 1, target, s)

    if pick:  # shortcut: if True, no need to check further
        return True

    # exclude nums[ind]
    not_pick = backtrack(nums, ind + 1, target, total)
    return not_pick


nums = [4, 5, 9]
ind = 0
target = int(input("Enter the target: "))  # example target

n = backtrack(nums, ind, target, 0)

print("Subset exists?", n)
