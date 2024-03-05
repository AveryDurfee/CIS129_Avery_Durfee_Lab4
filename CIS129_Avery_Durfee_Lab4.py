# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
storeAmount = 0  # percent of sales increase
# prompt = ?????? # prompt will be a string literal

# This code determines the storeAmount bonus
monthlySales = float(input("How much did you sell"))
if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 100000:
	storeAmount = 5000
elif monthlySales >= 90000:
	storeAmount = 4000
elif monthlySales >= 80000:
	storeAmount = 3000
else:
	storeAmount = 0
	
# This code gets the percent of increase in sales
salesIncrease = float(input("By what percentage))
salesIncrease = salesIncrease / 100
if salesIncrease >= .05:
	empAmount = 75
