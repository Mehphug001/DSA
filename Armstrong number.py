def Count_digit(n):
    #return len(str(n))
    num = n
    c = 0
    while num > 0:
        last_digit = num % 10
        c = c + 1
        num = num // 10
    return c


def IsArm(n):
    num=n
    total=0
    size=Count_digit(n)
    while num>0:
        last_digit=num%10
        p=last_digit**size
        total=total+p
        num=num//10
    return n==total

a = int(input("Enter a number: "))
print("Is the number a Armstrong:", IsArm(a))
