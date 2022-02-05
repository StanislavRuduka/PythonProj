def sum_recursion(a, b):
    list_numbers = range(a, b + 1)
    return sum(list_numbers)


a = int(input("Type the min number: "))

b = int(input("Type the max number: "))

if a > b:
    exit("Please provide range where first input is min, and second is max, restart the program")

if a == b:
    print(a + b)
else:
    print(sum_recursion(a, b))






