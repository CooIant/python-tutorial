#int 1, 4, 76 whole number only
#str 'Tom', 'Hello', '1' #anything in quotes, even numbers. can use single or double quotes. Can use single quotes inside double quotes.
#bool True, False #reserved words, highlighed. cannot be used for variable names, start with capital letters.
#float 0.32, 1.22 #any number with a decimal point.

name = 'Tom' #declare a variable name, and give it a value using =. Tom is a string.
print(name)
#variables can only contain letters, numbers, and underscores. Cannot begin with a number. Variable names are case sensitive.


print('hello, what is your name?') #print is a statement, inside parenth is called an argument
name = input()
print('hello, ', name) #separate arguments in a statement with commas

#Operaters : +, -, /, * for add, subtract, divide, multiply respectively. 
# ** is for exponents
# // is division without remainders. integer division. gives how many times a number goes into another.
# %  is division with remainders only. called modulus. eg. 5%2 = 1. 5/2 = 2, with a remainder of 1.

# input() will output given data as a string. 

#Conditions
# <, >, ==, != (\!\=)
# in python, one = is a declaration operator. Used for defining variables. For comparing, two = are used.
# can make comparisons between strings, integers, floats, etc.
print(2<3) #outputs a boolean value, True or False.

# if condition == True:
#    do this <--- input is important!

age = input('input your age: ')
if int(age) == 16: # input from console is taken as string, in order to compare with 'if', it must be converted to an integer with int()
    print("hey you're 16")
else:
    print('you are younger than 16') #indentation matters! python uses indentation to parse functions and conditionals.


height = input()
if int(height) < 1:
    print('you cannot ride, under 1m')
elif int(height) > 2:# checked next in sequence after 'if' is checked. one if, many elif, one else
    print('you cannot ride, over 2m')
else:
    print('you can ride')

#chained conditionals and nested if statements
x = 2
y = 3
if x == y and x + y == 5: #for this statement to be true, both conditions on each side of the 'and' must be true.
    print('ran')

if not(y == x or x + y == 5): #not() will reverse any arguments inside of it. instead of looking for statements to be true, it looks for false
    print('sad face')

#for loops
for x in range(0, 10, 1): #for loop will start at position '0'(inclusive) and run to '10'(exclusive), incrementing by '1'. Default increment is 1, not necessary to include.
    print(x)

loop = True
while loop: # 'loop' is considered the conditional, but can be any comparison. it defaults to == true, so no need to type it out
    name = input('type something:')
    if name == 'stop':
        loop = False #set original condition to false, stops loop
        break #stops loop by keyword

#lists
fruits = ['apple', 'pear', 3] #lists are denoted by brackets. items separated by commas
print(fruits[0]) #when calling a list, brackets will call a specific indicie. each item is assigned an integer sequentially from 0 

fruits.append('strawberry') #adds another item to the end of the list

fruits[1] = 'blueberry' #changes the item at indicie 1, pear, with blueberry

#touples vvvv
position = (2, 3)
color = (255,255,255)

fruits = ['apples', 'pears', 'strawberries']
for fruit in fruits: #for every item in fruits, named here as 'fruit', print each 'fruit'
    print(fruit)

for fruit in fruits: #iterate through each item, act only on condition
    if fruit == 'pears':
        print(fruit)
    else:
        print('not pears')

for x in range(len(fruits)): range()