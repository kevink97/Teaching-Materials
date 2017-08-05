# pip3 install PyDictionary
from PyDictionary import PyDictionary
from flash_lib import print_options, get_defintions, initialize_flashcard, check_word_in_vocabs, add_word_definition, beautify_vocabs_list, test_user

# this is the actual english dictionary!
d = PyDictionary()

print("Welcome to the Flashcard app.")
# this is your dictionary specialized for you vocab
vocab_dict = initialize_flashcard()

while 1 :
    print_options()
    # get the option of the user
    print()
    if 1: # if the option was 'a'
        pass
        # ask what the word was
        # check that the word is in the vocab list already, if so. don't add it
        #   (use check_word_in_vocabs(vocab_dict, word)
        #   and continue
        # get defintion using... get_defintion(d, word)
        # check if there is a defition.
        # If there is one, list out all the definition.
        # Make the user choose one.
        # Add the chosen definition with the word by using add_word_definition(vocab_dict, word, meaning)
    elif 2: # if option was l
        pass
        # print out the list using beautify_vocab_list(vocab_dict)
    elif 3: # if option was q
        pass
        # get out of the loop using brea
    else:
        # tell the user that it doesn't understand the option. print the option they submitted
        print("I do not understand the option you picked: " + opt)
    print()

# this tests the user! You can look at flash_lib.py to check how this is implemented
test_user(vocab_dict)
