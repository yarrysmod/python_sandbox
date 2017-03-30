import re
import unittest

from utils import toolbox

"""
    Returns a sorted presentation of a given string by the digit within each string

    @:arg   {String}    sentence    the given sentence to sort by their respective digit
    @:returns {String}.
"""
def sortString(sentence):
    segments = sentence.split(' ')
    newSentence = ''

    if len(segments):
        newSentence = ' '.join(sorted(segments, key=toolbox.convertCmpToKey(numCompare)))

    return newSentence


"""
    Compares two strings and returns the comparison

    @:arg   {String}    firstStr    the first string to compare
    @:arg   {String}    secondStr   the second string to compare
    @:returns {Integer}
"""
def numCompare(firstStr, secondStr):
    firstText = int(re.findall(r'\d+', firstStr)[0])
    secondText = int(re.findall(r'\d+', secondStr)[0])

    if firstText < secondText:
        return -1
    elif firstText > secondText:
        return 1
    else:
        return 0


class TestStringMethods(unittest.TestCase):
    def testSortString(self):
        self.assertEqual(sortString("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")


if __name__ == '__main__':
    unittest.main()
