import sys

while True:
	try:
		quantity = int(input("enter the no of quantity = "))
		if quantity > 0:
			break

	except:
		sys.exit("enter the correct quantity")

price = 20

Total_amount = quantity * price


print(Total_amount)