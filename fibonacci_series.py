n = int(input("Enter the number:"))
a, b = 0, 1
for i in range(n):
    c = a + b
    a = b 
    b = c 
    print(a)