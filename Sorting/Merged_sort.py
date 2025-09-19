def merged(left, right):
    result = []
    n, m = len(left), len(right)
    i, j = 0, 0

    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append remaining elements
    if i < n:
        result.extend(left[i:])
    if j < m:
        result.extend(right[j:])

    return result



def Merged_sort(arr):
    if len(arr)==1:
        return arr
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left=Merged_sort(left_arr)
    right=Merged_sort(right_arr)

    return merged(left,right)


arr=[3,1,6,2,4,8,7]
print(Merged_sort(arr))