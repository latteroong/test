counts = 0
number = int(input("Input number : "))

for i in range(2, number):
    if number % i == 0:
        counts = counts + 1
    print(i, end=' ')

if counts == 0:
    print(f"\n{number} is prime number~")
else:
    print(f"\n{number} is NOT prime number! (divisors : {counts})")