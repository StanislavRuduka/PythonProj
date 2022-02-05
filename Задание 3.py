import math

lower_value = int(input("Type the min number: "))
upper_value = int(input("Type the max number: "))

array_prime = []

print("The Prime Numbers in the range are: ", end=" ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number, end=" ")
            array_prime.append(number)

print()
print()
checker = int(input("Please specify if you want:\n1. sum \n2. multiplication \n"))

if checker == 1:
    print(f'The sum is: {sum(array_prime)}')
elif checker == 2:
    print(f'The product is: {math.prod(array_prime)}')
