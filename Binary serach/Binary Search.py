def Binary_search(nums, target):
    n = len(nums)
    l = 0
    h = n - 1

    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            h = mid - 1
        else:
            l = mid + 1

    return -1

nums = [2, 4, 6, 7, 9, 11, 18, 19]
target = int(input("Enter the target value: "))

index = Binary_search(nums, target)
if index != -1:
    print(f"The target value is at index: {index}")
else:
    print("Target value not found in the list.")
