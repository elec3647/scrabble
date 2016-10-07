import re

__author__ = 'kreitzem'


class WordList(object):
    def __init__(self, listfile=None):
        if listfile is None:
            self.words = open("words.txt").read().upper().strip().split()
        else:
            self.words = open(listfile).read().upper().strip().split()
            #### END
            # print self.words

    ####

    def search(self, regex):
        """

        :param regex:
        :return:
        """
        return [x for x in self.words if re.search(regex, x)]

    def is_a_word(self, my_word):
        """

        :param my_word:
        :return:
        """
        if my_word in self.words:
            return True
        else:
            return False


wl = WordList()
