# Copyright 2017 Kevin Kang
#
# Library built for Education.
# Specifically for for loops and in keywords
# pip3 install PyDictionary
from PyDictionary import PyDictionary
import random

def print_options():
    print('a -> add word')
    print('l -> list all the words')
    print('s -> stop adding words and test me!')

def get_defintions(d, word):
    print("getting definition")
    meaning = d.meaning(word)
    meaning_list = list()
    if meaning == None:
        return meaning_list
    for pos, means in meaning.items():
        for mean in means:
            meaning_list.append(pos + ": " + mean)
    return meaning_list

def initialize_flashcard():
    return dict()

def check_word_in_vocabs(vocab_dict, word):
    return word in vocab_dict

def add_word_definition(vocab_dict, word, definition):
    vocab_dict[word] = definition

def beautify_vocabs_list(vocab_dict):
    beautified = list()
    for word, meaning in vocab_dict.items():
        beautified.append(word + " - " + meaning)
    return beautified

def test_option():
    print('Here are the options:')
    print('r -> randomized')
    print('a -> alphabetized')
    print('q -> quit')
    return input("Pick an option: ")

def test_helper(o_list, vocab_dict):
    while o_list:
        word = o_list[0]
        print('Define this: ' + word + '\n\n')
        input('Press enter when ready for the definition...')
        print('Here is the definition:\n' + vocab_dict[word])
        ans = input('If you were correct, type y. Otherwise, type n: ')
        if ans == 'n':
            o_list.append(o_list.pop(0))
        else:
            o_list.pop(0)

def test_user(vocab_dict):
    copy_dict = dict(vocab_dict)
    while (1):
        opt = test_option()
        words = list(vocab_dict)
        if opt == 'a':
            words.sort()
            test_helper(words, vocab_dict)
        elif opt == 'r':
            words = list(words)
            random.shuffle(words)
            test_helper(words, vocab_dict)
        elif opt == 'q':
            print("Thank you for using the flashcard app!")
            break
