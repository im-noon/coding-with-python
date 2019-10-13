import timeit
'''
anagram check
'''
def anagram_checkoff(s1, s2):
    '''
    This algorithm will check to see that each character in s1 actually
    occurs in s2. If it is possible to "checkoff" each character, then the
    two string must be anagrams. Checking off a character will accomplished
    by replacing it with the None value.

    Complexity:
    Each of the n characters in s1 will cause an iteration up to n characters
    in the s2. Each the number visits then becomes the sum of the integers
    from 1 to n, that can be writen as
                T(i->n) = n(n+1)/2
                        = (i/2)n^2 + (i/2)n

    As n gets large, then the n^2 term will dominate the n term, then the
    complexity is O(n^2)


    :param s1: first sting
    :param s2: second string
    :return: True if s1 and s2 are anagram, otherwise return False
    '''
    alist = list(s2)
    pos1 = 0
    stileOK = True

    while pos1 < len(s1) and stileOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stileOK = False

        pos1 += 1

    return stileOK


def anagram_sortcompare(s1, s2):
    '''
    This algorithm will make use of the fact that even through s1 and s2 are
    different, they are anagram only if they consist of the same characters.
    We begin by sorting each string alphabetically from a to x, we will end
    with the same string if the two string are anagram.

    Complexity:
    There is one simple iteration to compare the n character after the
    sorting, and the two Python sort() method that are cost, typically the
    sorting either O(n^2) or O(n log n), so the soring dominate the operation.

    :param s1: first string
    :param s2: second sting
    :return: True if s1 and s2 are anagram, otherwise return False
    '''
    alist1 =list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches

def anagram_countcompare(s1, s2):
    '''
    This algorithm will takes advantage of the fact that any two anagrams
    will have the same number of each character. In order to decide whether
    two strings are anagrams, we will first count the number of times each
    character occur, since there are possible 26 characters, we can use a
    list of 26 counters, one for each possible character. Each time we will
    see a particular character, we will increment the counter at that
    position. In the ean, if the lists of counter are identically, the string
    must be anagrams.


    Complexity :
    The first two iteration used to count the character base on
    n. The third iteration compare the two list of counts, always takes 26
    steps, according ti the 26 possible characters in the string. Adding all
    up gives use T(n) = 2n + 26
                      = O(2n + 26)
                      = O(n)


    :param s1: first string
    :param s2: second string
    :return: True if s1 and s2 are anagram, otherwise return False
    '''
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    cnt = 0
    matches = True
    while cnt < 26 and matches:
        if c1[cnt] == c2[cnt]:
            cnt += 1
        else:
            matches = False

    return matches


if __name__ == "__main__":

    print("anagram_checkoff")
    start = timeit.default_timer()
    print(anagram_checkoff('heart', 'earth'))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    print("\n\nanagram_sortcompare")
    start = timeit.default_timer()
    print(anagram_sortcompare('heart', 'earth'))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

    
    print("-----------");
