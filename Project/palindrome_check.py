"""
"A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking
whether a given string is palindrome or not!

"""
import heapq

# O(N)
def palindrome_check(str):
    original_str = str
    reversed_str = str[::-1]

    if original_str == reversed_str:
        return True
    return False

def palidrome_python(str):
    return str == ''.join(str[::-1])

if __name__ == "__main__":
    print(palidrome_python("lsdkjfskf"))
    print(palidrome_python("radar"))
    print(palidrome_python("implementation"))
    print(palidrome_python("anna"))