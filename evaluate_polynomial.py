def eval_poly(numberX,coeffList):
	print ("function evaluating polynomial was triggered")
	print ("number x: ",numberX)
	print ("coefficient list:",coeffList)

	#degree of the polynomial
	d = len(coeffList) - 1
	print ("degree of the polynomial is:",d)

	#value (v) of polynomial
	v = 0
	#used (c) to decrease the degree in each iteration
	c = 0
	for i in coeffList:
		v = v + i*(numberX**(d-c))
		c = c + 1
	return (v)

#uncomment below for a menu that requests all input details - and comment the fixed lines 29&30
# numberX = int(input("Please enter number X:"))
# coeffList = []
# ans='y'
# while (ans != 'n') :
# 	c = int(input("Please enter a coefficient:"))
# 	coeffList.append(c)
# 	ans = input("Add another coefficient? y/n:")

#this is used for fixed inputs instead of asking user to input details
numberX = 2
coeffList = [2,2,2]

valueOfPolynomial=eval_poly(numberX,coeffList)
print("Polynomial value:",valueOfPolynomial)