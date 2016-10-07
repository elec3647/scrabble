#!/usr/bin/python
import re
import sys

search_pattern = sys.argv[1]
query_regex = re.compile(search_pattern+"$")

# Strips special chars from regex.
search_letters = re.sub(r'\W+', '', sys.argv[1]).upper()

rack = sys.argv[2].upper()

word_list = [x.upper().strip() for x in open("words.txt").readlines()]

# Scores for Words with Friends Facebook/Phone Game
scores = { 'A': 1, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'F': 4, 'G': 3, 'H': 3, 'I': 1, 'J': 10, 'K': 5, 'L': 2, 'M': 4,
    'N': 2, 'O': 1, 'P': 4, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 2, 'V': 5, 'W': 4, 'X': 8, 'Y': 3, 'Z': 10 }


def is_a_word(dict_word, my_rack):
    #word = re.sub(search_letters,'',word,count=1)
    stripped_word = dict_word.replace(search_letters, '', 1)
    test = True
    for letter in stripped_word:
        if letter in my_rack:
            my_rack = my_rack.replace(letter, "", 1)
        elif "*" in my_rack:
            my_rack = my_rack.replace('*', "", 1)
        else:
            test = False
            ####
    ####
    return test


def score_word(word):
    return sum([scores[c] for c in word])

matches = []
for word in word_list:
    if re.match(query_regex, word) and is_a_word(word, rack):
        matches.append([word, score_word(word)])

for word in sorted(matches, key=lambda entry: entry[1], reverse=True):
    print " ", word[1], word[0]
