# Take number from user input
'''num = int(input("Enter a number: "))

n = num
count = 0

while num > 0:
    last_digit = num % 10
    count = count + 1
    num = num // 10

print("Number of digits:", count)'''
from math import log10

def count_digit(num):
    if num == 0:
        return 1   # special case
    return int(log10(abs(num)) + 1)

num = int(input("Enter a number: "))
print("Number of digits:", count_digit(num))


#Tc:O(log10(n))
#Sc:O(1)