# yes, it's not very good code

print(" ")
minNumber = int(input("Minimum amount of consecutive numbers: "))
maxFindNumber = int(input("Maximum number to search: "))
startNumber = int(input("Number to start search at: "))

x = startNumber

def findAmountFactors(number):
	r = 2
	count = 0
	while r < number:
		if number % r == 0:
			count += 1
		r += 1
	return count



factors =  0

# while True:
while x <= maxFindNumber:
	factors = findAmountFactors(x)
	list = []
	while factors == findAmountFactors(x):
		list.append(x)
		x += 1
	list.append(len(list))
	list.append(factors)
	if len(list) > 1 + minNumber:
		print(list)
	else:
		pass
	
print("End")
print(" ")
print(" ")
