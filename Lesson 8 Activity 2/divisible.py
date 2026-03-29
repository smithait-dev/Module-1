numerator=int(input("Enter the number you want to divide:"))
denominator=int(input("What do you want to divide it by?"))
if numerator%denominator ==0:
    print("The number",numerator,"is divisable by",denominator,"and the answer is:",numerator/denominator)
else:
    print("It is not divisible")