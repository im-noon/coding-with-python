"""
Our task is to design an efficient algorithm to reverse a given integer.
For example if the input of the algorithm is 1234 then the output should be 4321.
"""
def reveres_integer(n):
    reversed = 0
    while n>0:
        remainder = n % 10
        n = n //  10
        reversed = reversed * 10 + remainder

    return reversed

if __name__ == "__main__":
    number = 32
    print(reveres_integer(number))



