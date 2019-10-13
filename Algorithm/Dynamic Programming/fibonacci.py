"""
Fibonacci number:

Fibonacci numbers are defined as
        f(n) = f(n - 1) + f(n - 2)
        f(0) = 0
        f(1) = 1
dynamic programming approach:
- use memorization in order to avoid recalculating a sub-problem over and
over again.
- should use an associative array abstract data type (hash table) to store
the solution for the sub-problem, O(1) time complexity
- on every f() method call, we should insert the calculated value if necessary.
- instead of exponential time complexity, we will have O(N) time complexity +
  requires O(N) space.
"""
import time
class Fibonacci(object):

    def __init__(self):
        self.memorize_table = {}
        self.memorize_table[0] = 0
        self.memorize_table[1] = 1

    def naiveApproach(self, n):

        # f(n) = f(n - 1) + f(n - 2) where f(0) = 0 and f(1) = 1
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.naiveApproach(n - 1) + self.naiveApproach(n - 2)

    def memorizeApproach(self, n):
        if n in self.memorize_table:
            return self.memorize_table[n]

        self.memorize_table[n - 1] = self.memorizeApproach(n - 1)
        self.memorize_table[n - 2] = self.memorizeApproach(n - 2)

        fnumber = self.memorize_table[n - 1] + self.memorize_table[n - 2]
        self.memorize_table[n] = fnumber
        return fnumber


if __name__ == "__main__":


    fibonacci = Fibonacci()

    n = 100


    start = time.time()
    print("naive fibonacci {} = {}".format(n, fibonacci.naiveApproach(n)))
    end = time.time()
    print("\texecute time :{}".format(end - start))
    

    start = time.time()
    print("memorize fibonacci {} = {}".format(n, fibonacci.memorizeApproach(n)))
    end = time.time()
    print("\texecute time :{}".format(end - start))
