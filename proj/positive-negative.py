# Write a python program to check given number is positive or negative

num = float(input('Enter a number: '))

if num > 0:
    print(num , 'is a positive number')
elif num == 0:
    print(num , 'is zero')
elif num < 0:
    print(num , 'is negative number')