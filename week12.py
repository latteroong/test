is_prime = True
number = int(input("Input number : "))

if number <= 1: # 버그 픽스
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break   # perfomance up
        print(i, end=' ')

if is_prime:
    print(f"\n{number} is prime number~")
else:
    print(f"\n{number} is NOT prime number!")