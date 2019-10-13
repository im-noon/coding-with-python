def head(n):
    # base case
    if n == 0:
        return

    # recursive
    head(n - 1)

    # do something here
    print(n)

# same as iteration
def tail(n):

    # base case
    if n == 0:
        return

    # do something here
    print(n)

    # recursive
    tail(n -1)

if __name__ == "__main__":
    print("head recursion...")

    head(5)

    print("tail recursion...")
    tail(5)
