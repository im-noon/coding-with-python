"""
worst case running time complexity is O(N*M)
"""

def substring_search(text, pattern):
    # length of the text is N
    length_text = len(text)

    # length of the pattern is M
    length_pattern = len(pattern)

    # we consider all the letter in the text O(N) complexity
    for i in range(length_text):
        # we check the pattern (it is misleading it has O(M) running time)
        if text[i:length_pattern + i] == pattern:
            # if find a match return with the index
            return i

    # we do not find the pattern
    return -1


if __name__ == "__main__":
    print(substring_search("My name is Adam", "ad"))