def factorial(n):
    """
    Compute the valu of the factorial function.
    :param n: is positive integer denote n!
    :return: 1 if n == 0, else return recursion of n-1
    """

    if n == 0:
            return 1
    else:
        return n * factorial(n - 1)



if __name__ == "__main__":
    f = factorial(5)
    print(f)
