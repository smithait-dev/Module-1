speed1=int(input("How fast is one F1 car going?"))
speed2=int(input("How fast is another F1 car going?"))
speed3=int(input("How fast is another F1 car going?"))
avg=(speed1+speed2+speed3)/3
print("The average speed of the F1 cars is:",avg)
if speed1>avg and speed2>avg:
    print("%d and %d is higer than the average speed of %f"%(speed1,speed2,avg))
elif speed2>avg and speed3>avg:
     print("%d and %d is higer than the average speed of %f"%(speed2,speed3,avg))
elif speed3>avg and speed1>avg:
     print("%d and %d is higer than the average speed of %f"%(speed1,speed3,avg))
elif speed1>avg:
    print("%d is higer than the average speed of %f"%(speed1,avg))
elif speed2>avg:
    print("%d is higer than the average speed of %f"%(speed2,avg))
elif speed3>avg:
    print("%d is higer than the average speed of %f"%(speed3,avg))
else:
    print("They are all the same speed!")