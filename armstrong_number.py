num = int(input("Enter a number :"))
length_of_num = len(str(num))
original_number = num
sum_of_powers = 0
for i in range(length_of_num):
    digit = num % 10
    sum_of_powers += digit ** length_of_num
    num = num // 10
if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number")
else:
    print(f"{original_number} is not an Armstorng number")
    