
'''For Loop'''
# the for loop executes a block of code
# repeatedly until the condition in the
# for statement is no longer valid.

# looping through an iterable

# pets = ['cats', 'dogs', 'rabbits', 'hamsters']
#
# for myPets in pets:
#     print(myPets)
#
# print("                        ")
#
# for index, myPets in enumerate(pets):
#     print(index,myPets)
#
# # the next example shows how to loop through
# # a string
#
# message = 'Hello'
#
# print("                        ")
#
# for i in message:
#     print(i)
#
# # looping through a sequence of numbers
#
# print("                        ")
#
# for i in range(6):
#     print(i)
#
# print("                        ")
#
# for i in range(3,10):
#     print(i)
#
# print("                        ")
#
# for i in range(4,10,2):
#     print(i)
#
# print("                        ")

'''While Loop'''
# a while loop repeatedly executes instructions
# inside the loop while a certain condition
# remains valid. the structure of a while
# statement is as follows:

# while condition is true:
#       do A
# print("***********")
# print("-----------")
# print("While Loops")
# print("-----------")
# print("***********")
# print("-----------")
# print("Example One:")
# print("-----------")
#
# counter = 5
#
# while counter > 0:
#     print ("Counter = ", counter)
#     counter = counter - 1
    # ^ the most crucial line
    # it decreases the value
    # of counter by 1 and
    # assigns this new value
    # back to counter, overwriting
    # the original value

# be careful when using while loops due to the
# danger of infinite loops

'''Break'''
# When working with loops, sometimes you may
# want to exit the entire loop when a certain
# condition is met. To do that, we use the
# break keyword.

# print("-----------")
# print("Break")
# print("-----------")
#
# j = 0
#
# for i in range(5):
#     j = j + 2
#     print('i = ', 'j =', j)
#
#     if j == 6:
#         break
#
# '''Continue'''
#
# print("-----------")
# print("Continue")
# print("-----------")
#
# j = 0
# for i in range(5):
#     j = j + 2
#     print('\ni = ', i, ' ,  j =', j)
#
#     if j == 6:
#         continue
#         print('I will be skipped over if j = 6')

'''Try, Except'''
# This control statement controls how the program proceeds when an
# error occurs.

# the syntax is as follows:

# print("example one:")
# print("--------------------------")
# print('try:')
# print('answer = 12/0')
# print('print(answer)')
# print('except:')
# print('print("An Error Occured")')
# print("--------------------------")
#
#
# print("Answer is:")
# try:
#     answer = 12/0
#     print(answer)
# except:
#     print("An Error Occured")

print("example two:")
print("--------------------------")

# try:
#     userInput1 = int(input("Please enter a number:"))
#     userInput2 = input(input("Please enter another number:"))
#     answer = userInput1/userInput2
#     print("The answer is: , ", answer)
#
#     myFile = open(("missing.txt", 'r'))
# except ValueError:
#     print("Error: You did not enter a number")
#
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
#
# except Exception as e:
#     print("Unknown error: ", e)





















