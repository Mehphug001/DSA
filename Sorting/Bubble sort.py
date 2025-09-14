def Bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    print(arr)

def bubble(arr):
    n=len(arr)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swap=True
        if is_swap==False:
            break
    print(arr)
arr=[5,8,1,6,9,2,4]
arr2=[1,2,5,6,8,11,14,17]
#Bubble(arr)
bubble(arr2)