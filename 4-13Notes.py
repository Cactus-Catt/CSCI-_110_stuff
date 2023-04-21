'''Notes for 4/13 csci 110'''
cost = 3.62 #float (input("Enter the cost of the products:"))
amountPaid = 5 #float (input ("enter the amt of money offered:"))

change = amountPaid - cost
dollars = int (change)
change = change - dollars 
change = round (change * 100)

print ("Dollars  ", dollars)
print ("Quarters ")
print ("Dimes    ")
print ("Nickles  ")
print ("Pennies  ")
