
numbers = [1,2,3,4,5,6,7]

def square(num):
    result = num**2
    return result
print("-------MAP------")
for item in map(square,numbers):
    print(item)

print(list(map(square,numbers)))
print("-------FILTER------")
def check_even(num):
    return num % 2 == 0

for n in filter(check_even,numbers):
    print(n)
print("-------LAMBDA------")

square_l = lambda num: num ** 2

print(square_l(5))
print(list(map(lambda num1: num1 ** 2,numbers)))
print(list(filter(lambda num2: num2 % 2 == 0,numbers)))
