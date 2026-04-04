num1 = int(input("Enter a: "))
num2 = int(input("Enter b: "))
num3 = int(input("Enter c: "))

temp = num1
num1 = num2
num2 = num3
num3 = temp

print("After swapping:", num1, num2, num3)
