def Check_sorted(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False

    return True


arr=[1,3,5,6,7,8,9]
arr2=[1,3,2,5,6,7,8,9]

print(Check_sorted(arr))
print(Check_sorted(arr2+
                   ))