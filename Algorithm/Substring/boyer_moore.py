"""
boyer moore substring search
"""

def build_bad_macth_table(pattern):
    """
    Construct the bad match lookup table
    :param pattern: the substring pattern
    :return: lookup table of pattern
    """
    length_pattern = len(pattern)

    # lookup table is a dictionary {char:num of shift} for all letter in pattern
    lookup_table = {}

    # consider all letter in the pattern
    for index, char in enumerate(pattern):

        max_shift = max(1, length_pattern - index - 1)

        # update the lookup table
        lookup_table[char] = max_shift

    return lookup_table


def sunstring_search(text, pattern):
    """
    Boyer moore substring search implementation
    :param text: string
    :param pattern: substring
    :return: index of match substring
    """

    lookup_table = build_bad_macth_table(pattern)

    length_text = len(text)
    length_pattern = len(pattern)

    # index i will track the letter of the text
    i = 0

    # consider all letters in the text
    while i <= length_text - length_pattern:

        # reset shift index
        shift_index = 0

        # consider the pattern in reverse order
        for j in range(length_pattern - 1, -1, -1):

            # if there is a mismatch, update the shift index
            if text[i+j] != pattern[j]:

                #if bad match table contain the letter in the text
                if text[i+j] in lookup_table:
                    shift_index = lookup_table[text[i+j]]
                # otherwise update shift index with the pattern length
                else:
                    shift_index = length_pattern

                i += shift_index

                # the letter are not matching so no need to consider further
                # letter
                break

        # if all the letters are matching, then we find the pattern
        if shift_index == 0:
            return i

    # the pattern not found
    return -1


if __name__ == "__main__":
    print(sunstring_search("this is a test", "Adam"))

    print(sunstring_search("this is a test", "test"))
