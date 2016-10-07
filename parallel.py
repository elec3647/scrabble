#!/usr/bin/env python
from word_list import WordList

__author__ = 'kreitzem'

# rack = sys.argv[1].upper()
wl = WordList()

word = "WASTE"
rack = "THAT".upper()

word_num = 0
rack_num = 0

for num in range(0, len(word)-1, 1):
    temp_word = word[word_num] + rack[rack_num]
    if wl.is_a_word(temp_word):
        print "we got %s" % temp_word
        word_num = + 1
        rack_num = + 1
        next
    else:
        print("not a word %s" % temp_word )
        word_num = + 1
        next


