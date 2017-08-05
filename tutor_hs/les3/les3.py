# today we are going to learn about lists and for loops and while loops
# Yesterday, we learned about conditions and comparisons.
# today, we will learn about:
#   lists
#   string
#   in/not in
#   loops
#   hopefully function!

'''
Lists are pretty cool. It's something you could maybe put a high score in.
you create a new list with no content by:
    l = list()
You can create a list with content in it by:
    l = ['a', 'b', 'c']
A list can hold many different types.

You can access and modify list by using this kind of syntax:
    a[1]
    x = a[0]

you can get the length of the array by: len(a)

Here are some list methods:
    list.append(elem) => add element to end
    list.insert(index, elem) => addd elements at the index, shift elements to right)
    list.extend(list2) -> adds element of list2 to the end of the list.
    list.index(elem) -> searches for the given element from start of list
    list.remove(elem) -> removes the element
    list.sort() -> sort in place
    list.reverse() -> reverse the list in place
    list.pop(index) -> removes and return element. if index omitted, opposite of append

Exercise 1: Create a new list called high score. Ask the user for a high score to insert
    5 times. After adding all of it, sort it, then reverse it, then print it.
    '''
highscore = list()

'''
Exercise 2: Create a list of vocabs. Show the list of vocab to memorize.
    Add one more vocab to the list. Then remove the second vocab in the list.
    Show me what is in the first index of the vocab list.
'''

'''
Strings are actaully just a list of something called a character.
So we can do many lists operations on strings.
We already know a few String operations
+ (concat)
* (duplicate)

There are some more:
    s.lower()/upper() -> lowercase or uppercase of string
    s.strip() -> remove whitespace start and end
    s.startwith('')/endwith('')
    s.find('') -> returns first index of where it is found; otherwise -1
    s.replace('old', 'new') -> return a string where all occurrences of 'old' have been replaced
    s.split('delim') -> splits the string into an array by the delimeter
    s.join(list) -> joins items in list into one string with s as its delimeter.

You can also access the string using list like syntax.
You can also find the length of the string like lists

# Exercise 1: take in 2 3-digit number and 1 4-digit number.
        Create a phone number out of it in this format: 123-456-7890
        Make sure you verify that it is in that format.
        Hint: len, s.isdigit()

# Exercise 2: Take in a name with the following format: Kevin Myungki Kang
        and change it to KANG, KEVIN MYUNGKI
        so that it can work for driver's license.
'''

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

Exercise:
    Using TrumpTwitter.py, extract all of the Trump's friends
        and print out the name of the friends of Trump's with Trump in their names.

# python3 -i TrumpTwitter.py
'''
