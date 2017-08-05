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
    opt = input("What would you like to do?: ")
    print()
    if opt == 'a':
        word = input("What is the word?: ")
        if check_word_in_vocabs(vocab_dict, word):
            print("That word is already in the list")
            continue
        meanings = get_defintions(d, word)
        if len(meanings) == 0:
            print("There were no definitions")
            continue
        print("\nHere are the definitions I got: ")
        for i in range(len(meanings)):
            print(str(i + 1) + ". " + meanings[i])
        num = input("\nWhich definition would you like?[number]: ")
        meaning = meanings[int(num) - 1]
        add_word_definition(vocab_dict, word, meaning)
        print("Ok, added the word: " + word)
    elif opt == 'l':
        print("Here are all the words in the vocab list:")
        for vocab in beautify_vocabs_list(vocab_dict):
            print(vocab)
    elif opt == 's':
        print("We will now test you until you know all the words")
        break
    else:
        print("I do not understand the option you picked: " + opt)
    print()

test_user(vocab_dict)
