def compound_intrest(principal, rate, time):
    amount = principal * (pow((1 + rate /100), time))
    ci = amount - principal
    print("Compound Intrest is:", ci)


compound_intrest(10000, 5.3, 8)