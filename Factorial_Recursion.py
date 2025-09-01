#Factorial of a number :

def func(n):
    if n==1:
        return 1
    return n*func(n-1)

n=int(input("Enter the number :"))
print(f"Factorial of {n} :",func(n))