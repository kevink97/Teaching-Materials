# today we are going to learn about lists and for loops and while loops
# Yesterday, we learned about conditions and comparisons.
# today, we will learn about:
#   lists
#   string
#   in/not in
#   loops
#   hopefully function!

'''
in/not in

in and not in is very useful for string and lists.
You can asks python to check if a part of a string is in the bigger string or
an element is in the list as follows:
    "a" in "cat" => True
    "b" in "cat" => False
    3 in [1, 2, 3] => True
    4 in [1, 2, 3] => False

Not in just basically does the opposite.
'''
# Let's try in and not in out!
"a" in "cat"
"ca" in "cat"
"ca" not in "cat"
3 in [1, 2, 3]
5 in [1, 2, 3]
8 not in [1, 3, 5]

# Where can this be useful?
# in the phone book we built, maybe we wanna parse by the area code.
# or maybe we wanna check if a person's name is in the phone book.
# it is also VERY useful for loops.

'''
for loops:
    in python, we do loops with a list.
    the most common way to do it is by using a function called range.
        range(2) => [0, 1]
        range(1, 5) => [1, 2, 3, 4]
        range(1, 14, 7) => [1, 8]
    we iterate through this list by:
    for i in range(2):
        print(i)
    Similarly, with a string, we can:
    for c in "abcd":
        print(c)
    this extacts all characters.
    Again similarly, with an array, we can:
    for e in [1, 2, 3]:
        print(e)


# python3 -i TrumpTwitter.py
'''

# out of all the loops, for loops are one of the most common.
# we use range most often.
# loops in python basically iterates through lists.
# for i in range(5)
# ^ after every loop, i will be set to 0, then 1, 2, 3, and 4.
# THIS IS VERY USEFUL FOR GOING THROUGH LISTS that we make.
# we can also do this:
#   for i in [1, 3, 5]
# often we want to go through lists, so we would just:
#   for i in list
# for phone books, we have 2 lists...
#   so we can try: for n, num in zip(names, numbers)...
#       this will iterate names and numbers together.
# in the phonebook, you can notice we have something called a while loop with a 1.
# how while loop works is:
# while(cond):
# the reason I did while(1) is that anything other than 0 is actually translated to True.
# cuz 0 is false.


'''
Exercise:
    Using TrumpTwitter.py, extract all of the Trump's friends
        and print out the name of the friends of Trump's with Trump in their names.
'''

'''
Exercise 2:
'''

