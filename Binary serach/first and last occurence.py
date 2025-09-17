#Brute Force
"""


def first_last(nums,target):
    first=-1
    last=-1

    for i in range(len(nums)):
        if nums[i]==target:
            if first==-1:
                first=i
            last=i
    return [first,last]

"""
#Optimal:
#lower_bound=smallest index nums[i]>=target
#uper_bound= index nums[i]>target
def lower_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    lb = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lb = mid
            high = mid - 1
        else:
            low = mid + 1

    return lb

def upper_bound(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    ub = -1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub



nums=[1,2,3,3,3,3,3,5,6,8,9,9,10]

target=int(input("Enter the Target :"))

lower=lower_bound(nums,target)
upper=upper_bound(nums,target)
print(lower,upper)
