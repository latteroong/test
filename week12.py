counts = 0
number = int(input("Input number : "))

for i in range(1, number+1):
    if number % i == 0:
        counts = counts + 1
    print(i, end=' ')

if counts == 2:
    print(f"\n{number} is prime number~")
else:
    print(f"\n{number} is NOT prime number! (divisors : {counts})")