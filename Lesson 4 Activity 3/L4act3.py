Biology=int(input("How many marks did you score in biology?"))
Chemistry=int(input("How many marks did you score in chemistry?"))
Physics=int(input("How many marks did you score in chemistry?"))
ComputerScience=int(input("How many marks did you score in computer science?"))
English=int(input("How many marks did you score in english?"))
totalmarks=Biology+Chemistry+Physics+ComputerScience+English
print("The total marks you have scored is",totalmarks)
percent=(totalmarks*100)/500
print(end="Percentage of total marks is=")
print(percent)