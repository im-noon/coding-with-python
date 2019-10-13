"""
The power function define as
                            power (x, n) = x^n

A trivial recursive definition follows the fact that n^n = x * x^n-1 for n > 0.


                            power(x, n) = { 1                   if  n = 0
                                            x*power(x, n-1)     otherwise.
"""

def power(x, n):
    """Compute the value x**n for n."""
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


if __name__ == "__main__":
    x = 10.0
    y = 4.0

    print(x/y)
    print(x//y)