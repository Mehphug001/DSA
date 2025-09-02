'''def Factors(n):
    result=[]
    for i in range (1,n+1):
        if n%i==0:
            result.append(i)
    return result
    '''



#Better Solution:

'''def Factors(n):
    result=[]
    for i in range (1,n//2):
        if n%i==0:
            result.append(i)
    result.append(n)
    return result
'''

#Optimal Solution:

from math import sqrt
def Factors(n):
    result=[]
    for i in range (1,int(sqrt(n))+1):
        if n%i==0:
            result.append(i)
        if n//i != i:
            result.append(n//i)

    return sorted(result)



a = int(input("Enter a number: "))
print("Factors of the number is :", Factors(a))