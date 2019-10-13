import time


def factorial_head(n):
    if n == 1:
        return 1
    return n * factorial_head(n-1)



# avoid stack oveflow, no backtracking
def factorial_tail(n, ans = 1):
    if n == 1:
        return ans

    return factorial_tail(n - 1, n * ans)


if __name__ == "__main__":

    print("factorial with head recursion: {}".format(factorial_head(4)))

    print("factorial with tail recursion: {}".format(factorial_tail(4)))

