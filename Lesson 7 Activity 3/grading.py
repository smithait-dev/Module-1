a=24
b=76
c=43
d=87
e=90
total=a+b+c+d+e
print("The total is",total)
avg=total/5
print("The average is",avg)

if avg >=91 and avg <=100:
    print("Your grade is A1")
elif avg>= 81 and avg <=90:
    print("Your grade is A2")
elif avg>= 71 and avg <=80:
    print("Your grade is B1")
elif avg>=61 and avg <=70:
    print("Your grade is B2")
elif avg>=51 and avg <=60:
    print("Your grade is C1")
elif avg>=41 and avg <=50:
    print("Your grade is C2")
elif avg>31 and avg <=40:
    print("Your grade is D1")
elif avg>21 and avg <=30:
    print("Your grade is D2")
else:
    print("You failed :(")