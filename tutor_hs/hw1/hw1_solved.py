# Homework 1
# Below are the problem sets. The problems will be numbered.
# if you have any questions, please email me :)
# note: this homework should be a bit hard. So, if you get stuck... let me know!
# total line of code you will write is 7 lines.

# 1. let's print "Hello World"
print("Hello World")

# scenario: You own an apple store. ;)
#           You have many apples, but want to know how much money
#           you will make with the amount of apples you have right now.
#           We will write a program that will calculate this for us.

# 2. set variable with a name: product to a string value: "apple(s)"
product = "apple(s)"

# 3. print the variable product
print(product)

# 4. set variable with a name: price to a float value: 10.0
price = 10.0

# 5. set variable with a name: count to a integer value: 1000
count = 1000

# 6. We can figure out how much money we will make in total by
#       multiplying price and count together.
#       Set variable wiht a name: income by multiplying variable price and count.
income = price * count

# 7. Print the total income exactly like this:
#       "In the Apple Store, we have [count] [product]... each sold at $[price]. This store will receive $[income] after selling all of the apples!"
# note: you will have to add strings together since you will have to use the variables count, price, and income.
# note #2: you will have to use the str() function, like we used in class for integer and float values!
print("In the Apple Store, we have " + str(count) + " " + product + "... each sold at $" + str(price) + ". This store will receive $" + str(income) + " after selling all of the apples!")

