
# # suppose
#
# x = 5
# y = 2
#
# # increment by 2:
# x2 = x + 2

'''Operations'''

# float:
# userHeight = 1.82

# #floor division:
# print(x//y)
#
# #division:
# print(x/y)
#
# #modulus:
# print(x%y)
#
# #exponent
# print(x**y)

'''formatting strings using the % operator'''

# part I:
# brand = 'Apple'
# exchangeRate = 1.235235245
#
# message = 'The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR' %(brand,1299,exchangeRate)
#
# print(message)

# part II:
# message1 = '{0} is easier than {1}' .format('Python', 'Java')
# message2 = '{1} is easier than {0}' .format('Python','Java')
# message3 = '{:10.2f} and {:d}' .format(1.234234234,12)
# message4 = '{}'.format(1.234234234)
#
# print(message1)
# print(message2)
# print(message3)
# print(message4)

'''Arrays'''
# userAge = [21, 22, 23, 24, 25]
# print(userAge)
# print(userAge[2])
# print(userAge[0:2])

'''Tuple'''
# a collection of objects which ordered and immutable.
# Tuples are sequences, just like lists.
# The differences between tuples and lists are, the tuples cannot be changed
# unlike lists and tuples use parentheses, whereas lists use square brackets.

# monthsOfYear = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
#                 "Sep", "Oct", "Nov", "Dec")
#
# print(monthsOfYear[-8])

'''Dictionary'''
# a collection of related data PAIRS. For instance,
# storing the username and age of 5 users, we store them in a dictionary

# dictionaryName = {"Peter":38, "John":51, "Alex":32}
# print(dictionaryName)
# print(dictionaryName["John"])
# print(dictionaryName["Alex"])


'''Condition Statements'''

# # not equals
# print(5 != 2)
#
# # smaller
# print(2 < 4)
#
# # smaller than or greater to
# print(5 >= 2)
#
# # larger
# print(5 > 2)
#
# # larger than or greater to
# print(7 >= 7)
#
# # equal to
# print(5 == 5)

'''If Statement'''
# most commonly used control flow statements. it allows the program to
# evaluate if a certain condition is met, and to perform the approrpriate
# action based on the result of the evaluation.

# the structure of an if statement is as follows:
# if condition 1 is met: do A
# elif condition 2 is met: do B
# elif condition 3 is met: do C
# elif condition 4 is met: do D
# else:
     # do E

userInput = input('Choose between 1 or 2       ')

if userInput == "1":
    print('You  have chosen the path of light')

elif userInput == "2":
    print("You have chosen the path of darkness")

else:
    print("ERROR")

print("Now you must choose your most powerful weapon: ")

print("Knowledge")
print("Nothing about the known universe is out of your reach")

print("Immortality")
print("You will live as long as the ancient universe, unless you are slain")

print("Ruler of Hearts")
print("You are a charismatic soul whose charm is echoed by those who believe")

userInput = input("type your answer     ")


if userInput == "Knowledge":
    print("You must be careful, knowledge is powerful")

elif userInput == "Immortality":
    print("You will live beyond your wildest imagination, make sure it is worth the trek")

elif userInput == "Ruler of Hearts":
    print("With great power comes with great responsibiltiy")

else:
    print("Try again")



# Inline If:
# a simpler form of an if statement and is more convenient
# if you only need to perform a simple task. the syntax is:
# do task A if condition is true else do Task B







