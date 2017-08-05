# Homework 1 Notes
# Overview of print, variables, types, and mathematical operators.
# This is just notes. Look over it, but for this file, you will not have to write
# any code. Feel free to mess around with this notes file.
# <- btw this hashtag is a thing that lets the python know that things that follow the hashtag are comments.

# 1. Print
# note: to print something, you do: print("something")
print("something") # this statement will print "something"

# 2a. variables
# a variable is like a variable in algebra.
# In programming, we use variables to store values
#   and compute with other variables!
# We can store values into variables like this:
a = 1
# in above statement (or line), we set the variable a to a value of 1.
# if we print a out, we get that it is 1.
print(a)
# now, if we set a to something else, note that it will no longer hold the value 1.
a = "I am something else!"
print(a)

# 2b. types
# there are 3 types we will be looking at:
#   1. str (or string or text)
#   2. int (or integer)
#   3. float (or real numbers)
# Remember, str types must have quotation marks around it:
s = "I am a text/string!!!!"
# Integers are simply integers... so no decimals :)
i = 123
# floats are real numbers. They MUST have a decimal point!
f = 123.0
# you can check the type of a variable by passing the
#   variable into a function called type().
#   We will review what functions are next week.
type(s) # should print <type 'str'>
type(i) # should print <type 'int'>
type(f) # should print <type 'float'>

# 3. math ops
# python language offers many cool math operations!
# Here are some of them: 
# add: +, subtract: -, multiply: *, divide: /,
#   power of: **, and remainder after divide (mod): %.
# note: we haven't covered mod in class;
#       we will go over it next week.
# Here are some examples :)
i = 1
print(i) # should be 1
i = 1 * 4
print(i) # should be 4
x = i / 3
print(x) # hmmm... we get that it is 1! that doesn't seem right. Run this on python2. You probably don't need to worry about this.
x = i * 1.0 / 3
print(x) # now we get 1.3333. This is due to how programming languages implement integer div.
# computers actually really really hate real numbers! We will learn why later :)

# COOL! now that you know how to do some basic python, let's see if you can 
# do some on your own :)
