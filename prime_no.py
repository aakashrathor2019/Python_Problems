def is_prime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, num):
        if num % 2 == 0:
            return False
    return True


num = int(input("Enter no for check prime:"))
if is_prime(num):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")