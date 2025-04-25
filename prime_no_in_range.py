def is_prime(num):
    for i in range(2,num):
        if  num % i == 0:
            return False
    return True

start, end = map(int, input("Enter the start and end points for finding prime no:").split())
print("Start and End Value:", start, end)
prime_no = []
non_prime = []
for i in range(start, end+1):
    if is_prime(i):
        prime_no.append(i)
    else:
        non_prime.append(i)

print("ALL Prime No are:", prime_no)
print("All Non prime no:", non_prime)