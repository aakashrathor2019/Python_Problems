def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result = result * i
        return result
    
num = int(input("Enter a number:"))
print("The factorial of", num, "is", fact(num))