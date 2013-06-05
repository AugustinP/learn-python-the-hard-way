def printNumbersWhile(upto, inc):
	i = 1
	numbers = []

	while i <= upto:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + inc
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

def printNumbersFor(upto):
	i = 1
	numbers = []

	for i in range(i, upto):
		print "At the top i is %d" % i
		numbers.append(i)

		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

printNumbersWhile(50, 10)
printNumbersFor(10)