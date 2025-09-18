def Min_num(nums):
    n=len(nums)
    min_num=float("inf")

    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=nums[high]:
            min_num=min(nums[mid],min_num)
            high=mid-1
        else:
            min_num=min(nums[mid],min_num)
            low=mid+1

    return min_num


nums=[4,5,6,7,0,1,2]
print(Min_num(nums))

