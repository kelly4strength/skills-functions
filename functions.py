# SOLUTIONS!

################################################################
# PART ONE

# 1. Write a function that does not take any arguments and
#    prints "Hello World".
#functin is defined with empty paranthesis as no arguments will be taken
def say_hello():
	"""Takes no arguments and prints 'Hello World'"""
	print "Hello World"
#calling the function
say_hello() 

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def say_hi(name):
	"""Ask for a name and print Hi (name)"""
	
	"Hi %s." % name
	print "Hi %s" % name

say_hi("Kelly")	


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.
def multiply_nums(x,y):
	"""Multiply two numbers togther"""
	sum = (x * y) 
	print sum

multiply_nums(5, 10)


# 4. Write a function that takes a string and an integer and
#    prints the string that many times
#Not sure if this is what you guys were looking for...
def print_string_x_times(badger, x):
	"""Take a string and an integer and prints the string that many times"""
	#here's the string
	for i in range(x):
		print 'badger' 

print_string_x_times("badger",7 )


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".
def high_low_or_0(compare_integer):
	"""evaluate whether given integer is higher than 0, lower than 0 or 0."""
	if compare_integer == 0:
		print "Zero"
	elif compare_integer > 0:
		print "Higher than Zero"
	elif compare_integer < 0:
		print "Lower than Zero"

high_low_or_0(743)
	

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.
#YAY I get to use a modulus!!!

def eval_bool(num):
	"""Return a boolean, if an integer is evenly divisible by 3."""

	if num % 3 == 0: 
		print True
	else:
		print False

eval_bool(12)


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

my_sentence = 'I love to code'

def eval_sentence_spaces(num_spaces):
	"""Return the number of spaces in a string"""
	count_spaces = []
	space = ' '
	for space in my_sentence:
		if space == ' ':
			count_spaces.append(space)
	return len(count_spaces)

print eval_sentence_spaces(my_sentence)



# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.
def tip_total_calculator(meal_price,tip):

	return total amount paid

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.


default_tax = .05

state = "CA"
price = 8

if state == "CA":
    total =  .07 * price
else:
    total = default_tax * price

print total

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
