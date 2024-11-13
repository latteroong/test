is_prime = True # count(int)를 is_prime(bool)로 변경
number = int(input("Input number : "))
if number <= 1:
    is_prime = False
    
for i in range(2, number):
    if number % i == 0:
        is_prime = False    # + 제거
    print(i, end=' ')

if is_prime:    # 비교연산 제거
    print(f"\n{number} is prime number~")
else:
    print(f"\n{number} is NOT prime number! (divisors : {counts})")