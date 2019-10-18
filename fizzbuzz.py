#This is a coding interview question that is often given called
#FIZZBUZZ. Its defining a module and making sure it outputs what it
#is suppose to do. Here's the code below:

def fizz_buzz(input):
	if (input % 3 == 0) and (input % 5 == 0):
		return "FizzBuzz"
	if input % 3 == 0:
		result = "Fizz"
		return result
	if input % 5 == 0:
		result = "Buzz"
		return result
	return input
