def find_target_floor_ceil(nums, target):
    low = 0
    high = len(nums) - 1
    floor = None
    ceil = None

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return [nums[mid], nums[mid]]  # Target found: return [target, target]
        elif nums[mid] > target:
            ceil = nums[mid]
            high = mid - 1
        else:
            floor = nums[mid]
            low = mid + 1

    return [floor, ceil]  # Target not found: return floor and ceil


# Example usage:
nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]
target = int(input("Enter the target number: "))

result = find_target_floor_ceil(nums, target)
print(f"Result (Target or [Floor, Ceil]): {result}")
