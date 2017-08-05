# Phone Directory App!

# Make 2 lists below. 
#   One for names
names = #TODO

#   One for phone numbers
numbers = #TODO

# don't worry about line 11!
while(1):
    # Ask the user "Give me a name in this format FIRST LAST or type x to stop"
    name = #TODO
    # don't worry about line 18 and 19. It just stops asking the user.
    if name == 'x':
        break
    # verify that the name is in the right format by checking that there is only 2 words and 1 space. If not, write code in this format:
    #   if not correct format:
    #       pass
    # TODO


    # Ask the user "What is his/her number in this format XXX-XXX-XXXX"
    number = #TODO
    # verify that the number is in the right format by checking that there is 2 dashes
    #   and there is right amount of numbers between each dash [-]
    # If not, write code in this format:
    #   if not correct format:
    #       pass

    #TODO


    # insert both the name and number in its respective list names and numbers
    #TODO


# don't worry about line 28... it's just a loop :)
while(1):
    # Ask the user "Give me a name or number in the correct format or type x to stop"
    answer = #TODO
    # don't worry about line 33 and 34. It just stops asking the user if they typed x.
    if answer == 'x':
        break
    # Create an if ____ else ____ condition.
    # it should look something like this:   
    # if [the answer was in a name format]:
    #   print the number that is associated with that name by using string comparison
    #   AND using functions like index() and accessing the list as shown in line 12 of hw3_instruction file.
    # else:
    #   print the name that is associated with that name by using string comparison
    #   AND using functions like index() and accesing the list as shown in line 12 of hw3_instruction file.
    # Yes we are assuming that if it wasn't a name, it is a number
    #TODO

# ignore line 50 It just says bye to the user.
print("Thank you for using the Phonebook")
