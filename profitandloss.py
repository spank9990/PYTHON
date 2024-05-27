CP=int(input("enter cost price of an item:"))
SP=int(input("enter selling price of an item:"))

if CP>SP:
    loss=CP-SP
    print("we have incurred loss of:",loss)
elif SP>CP:
    profit=SP-CP
    print("we have made profit of:",profit)
else:
    print("we have made no profit and no loss.")    