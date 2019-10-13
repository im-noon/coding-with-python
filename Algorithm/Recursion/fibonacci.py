"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!

So we can write the rule:

The Rule is xn = xn-1 + xn-2

where:

xn is term number "n"
xn-1 is the previous term (n-1)
xn-2 is the term before that (n-2)
"""

def fibonacci(n, a = 0, b = 1):
    if n == 0:
        return a

    if n == 1:
        return b

    return fibonacci(n - 1, b, a + b)

if __name__ == "__main__":

    n = 10
    print("fibonacci of sequence {} = {}".format(n, fibonacci(n)))

