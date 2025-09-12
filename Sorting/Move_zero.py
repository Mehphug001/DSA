"""def Move_zero(arr):
    n=len(arr)
    i=0
    j=i+1
    if n==1:
        return
    while i<n:
        if arr[i]==0:
            break
        i+=1

    if i==n:
        return
    while j<n:
        if arr[j]!=0:

            arr[i],arr[j]=arr[j],arr[i]
            i += 1
        j+=1
    return arr
"""

def Move_zero(arr):
    n = len(arr)
    if n <= 1:
        return arr





    i = 0  # points to where next non-zero should go
    for j in range(n):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    if i == n:
        print("No Zero")
        return arr
    return arr


arr = [5, -2, 3, 9, 6, 10, 7]
print(Move_zero(arr))


print("New Array :")
arr2=[1,0,2,4,3,0,0,3,5,1]
print(Move_zero(arr2))