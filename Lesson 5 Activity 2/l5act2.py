actualamount=float(input("How much did you pay for the oranges?"))
sellingamount=float(input("How much are you selling the oranges for?"))
if sellingamount>actualamount:
    profit=sellingamount-actualamount
    print("The amount of profit you are making ={0}".format(profit))
else:
    print("You are not making a profit.Increase your sellign price.")