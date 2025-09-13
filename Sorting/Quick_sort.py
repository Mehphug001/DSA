def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high

    while True:
        while i <= high and nums[i] <= pivot:
            i += 1
        while j >= low and nums[j] > pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break

    nums[low], nums[j] = nums[j], nums[low]
    return j


def quick_sort(nums, low, high):
    if low < high:
        p_ind = partition(nums, low, high)
        quick_sort(nums, low, p_ind-1)
        quick_sort(nums, p_ind+1, high)


nums = [3, 1, 6, 2, 4, 8, 7]
quick_sort(nums, 0, len(nums)-1)
print(nums)




