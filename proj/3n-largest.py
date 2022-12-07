# write a python program to check largest of three numbers

def biggest(num1 , num2 , num3):
    if(num1 > num2) and (num1 > num3):
        largest = num1
    elif(num2 > num1) and (num2 > num3):
        largest = num2
    else:
        largest = num3

    return largest

num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

print(biggest(num1 , num2 , num3))