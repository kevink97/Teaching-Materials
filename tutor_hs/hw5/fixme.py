# Homework 5
# For this homework, we will be doing some bug fixing.
# In this program, there will be many bugs and I will be providing some hints
#   for you.
# IMPORTANT: the bugs will be labeled on the line above with a FIXME comment
# Do your best!

########### Section 1: printing some stuff
# this print line is fine!
print("hello world")

# this print line is also fine...
print("My favorite number is: " + str(1))

# FIXME: print can only take in one type (integer, string, real)!
#           Should print "Hello, ma name is Bob"
print(Hello, my name is Bob)

# FIXME: non-strings cannot be added with a string
#           Should print "hello! I am 13 years old"
print("hello! I am " + 13 + " years old")

# FIXME: you can have arithmetics in your print, but should be string
#           Should print "1 + 1 = 2"
print("1 + 1 = " + (1 + 1))


########### Section 2: asking user for input.
# this user input is fine:
name = input("What is your name: ")
print("Oh.. hi "+ name)

# this user input is also fine
age = input("What is your age?")
print("wow! you are so old: " + int(age))

# FIXME: if you want to use the user's input, you need to save it
#           Should print: "wow! I didn't know this ____ was your favorite color!"
input("What is your favorite color?")
print("wow! I didn't know this " + color + " was your favorite color!")

# FIXME: Whatever input the user type...is a string... even though he typed a number
x = input("give me a number!: ")
print("your number is: " + x)


########### Section 3: If True or False.
# this works!
if True:
    print("I should be printed!")

# FIXME: make the below if/elif/else statement print out "HELLO!"
if False:
    print("hi")
elif True:
    print("hey")
elif True:
    print("HELLO!")
else:
    print("bye")

# FIXME: make the below if/elif/else statement print "I am great at coding"
x = 1
if x == 3:
    print("I am great at cooking")
elif x > 1:
    print("I am great at running")
elif not x == 1:
    print("I am great at coding!")


########### Section 4: looping and looping and more looping
# this works! Should print: 0, 1, 2 each on its own line
for i in range(3):
    print(i)

# this works! Should print a, b, c
for character in "abc":
    print(character)

# FIXME: make this print 0, 1, 2, 3, 4
for i in range(3):
    print(i)

# FIXME: make this print out everything in the list:
x = [1, 'a', 2, 3, 'b'] # this is a list
for i in fixme:
    print(i)









