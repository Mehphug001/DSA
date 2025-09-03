def miss(nums):
    nums_sum,n=0,len(nums)
    total_sum=int((n*(n+1))/2)
    for num in nums:
        nums_sum+=num

    return total_sum-nums_sum


nums=[1,0,3,4]
print(miss(nums))

nums1=[3,0,1]
print(miss(nums1))

nums2=[9,6,4,2,3,5,7,0,1]
print(miss(nums2))