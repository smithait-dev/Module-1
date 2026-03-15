amount=int(input("What is the amount withdrawn?"))
note500=amount//500
amount%=500
note100=amount//100
amount=amount%100
note50=amount//50
amount=amount%50
note10=amount//10
amount=amount%10
print("The number of 500 rupee notes is",note500)
print("The number of 100 rupee notes is",note100)
print("The number of 50 rupee notes is",note50)
print("The number of 10 rupee notes is",note10)
print("The remaining amount is",amount)