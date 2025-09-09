from itertools import count


def consecutive(nums):
    n=len(nums)
    count=0
    max_count=0
    for i in range(n):
        if nums[i]==1:
            count+=1
        else:
            max_count = max(max_count, count)
            count=0
    return max(max_count,count)

nums=[1,1,0,1,1,1]
nums2=[1,0,1,1,0,1]

print(consecutive(nums))
print(consecutive(nums2))