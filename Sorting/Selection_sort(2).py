def sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        max_ind=i
        for j in range(i+1,n):
            if arr[max_ind]<arr[j]:
                max_ind=j
        arr[i],arr[max_ind]=arr[max_ind],arr[i]
    return arr


arr=[5,7,8,4,1,6,9,2]
print(sort(arr))