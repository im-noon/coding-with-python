"""
Knuth Moriss Pratt substring search
"""

def buil_pi_table(pattern):

    # the table has as many as values as the length of the pattern(first item
    # is always 0)

    pi_table = [0] * len(pattern)
    index = 0

    # consider all letters in pattern this take O(M) running time complexity
    for i in range(1, len(pattern)):

        if pattern[i] == pattern[index]:
            pi_table[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = pi_table[index - 1]
            else:
                pi_table[i] = 0
                i += 1

    return pi_table

def substring_search(text, pattern):
    """
    Knuth-Morris-Pratt algorithm : running time complexity O(N+M)
    :param text: string
    :param pattern: substring
    :return: match generator
    """

    # construct pi table
    pi_table = buil_pi_table(pattern)

    # index i track the text - index j track the pattern
    i = 0
    j = 0

    # iterate until the i index is less than the length of the text
    # and make sure i is smaller than the length of pattern
    while i < len(text) and j < len(pattern):

        # if the letters sre matching we are increment both index
        if text[i] == pattern[j]:
            i += 1
            j += 1

        # ewe found the pattern in the text: re initialize tge j index to be
        # able find more patterns

        if j == len(pattern):
            yield i-j
            j = pi_table[j - 1]

        # if the is mismatch
        elif i < len(text) and text[i] != pattern[j]:
            # initialize j base on the pi table
            if j != 0:
                j = pi_table[j - 1]
            # if we are not able to decrement j we decrement i
            else:
                i += 1

if __name__ == "__main__":

    for index in substring_search("this test is a test","is"):
        print("Pattern found at index: {}".format(index))