def binary(nums, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary(nums, low, mid - 1, target)
    else:
        return binary(nums, mid + 1, high, target)


nums = [2, 4, 6, 7, 9, 11, 18, 19]
n = len(nums)

target = int(input("Enter the target number: "))
index = binary(nums, 0, n - 1, target)

if index != -1:
    print(f"The index of the target number is: {index}")
else:
    print("Target number not found in the list.")
