"""
Knapsack problem:
- It is a problem in combinatorial optimization.
- Given a set of items, each with a mass "w" and a value "v", determine the
number of each item to include in ca collection so that the total weight M is
less than or equal to a given limit and the total value is as large as possible.
- The problem often arises in resource allocation where there are financial
constraints.

Applications:
- Finding the least wasteful way ti cut raw materials.
- Selection of investment and portfolios.
- Selection of assets fot asset-backed securitization.
- Construction and scoring of tests in which the test-takers have a choice
as to which questions they answer.

Divisible problem:
- If we can take fractions of a given items, the the greedy approach can be
used.
- Sort the items according to their values, it can be done in O(N*logN)
- Start with the item that is the most valuable and take as much as possible.
- Then try the next item from our sorted list.
- This linear search has O(N) time complexity.
- Overall complexity: O(N*logN) + O(N) = O(N*loN)
- So we can solve the divisible knapsack problem quite fast

0-1 knapsack problem:
- In this case we are not able to take fraction, whe have ti decide whether
to take an item or not.
- Greedy algorithm will not provide the optimum result.
- Dynamic programming is the right way.

Knapsack with dynamic programming
- we have ot decide sub-problem: we have N items so we have to make N
decisions whether to take the item with given index or not.
- The sub-problems: the solution considering every possible combination of
remaining items and maintaining weight.
- S[i][w] the solution to the sub-problem corresponding to the first i items
and available weight w
Or in other words...
- S[i][w] = the maximum cost of items that fit inside a knapsack of size
(weight) w, choosing from the first i items
- We have to decide whether to take the item or not.
"""


class Knapsack(object):

    def __init__(self, items_count, capacity, items_weight, items_ptofit):
        self.items_count = items_count
        self.capacity = capacity
        self.items_weight = items_weight
        self.items_profit  = items_ptofit
        self.memorize_table = [[ 0 for _ in range(capacity + 1)] for _ in
                               range(items_count + 1)]

    def solve_knapsack_problem(self):

        for i in range(1, self.items_count + 1):
            for w in range(1, self.capacity + 1):

                not_taking_item = self.memorize_table[i-1][w]
                taking_item = 0

                if self.items_weight[i] <= w:
                    taking_item = self.items_profit[i] + self.memorize_table[
                        i-1][w - self.items_weight[i]]

                self.memorize_table[i][w] = max(not_taking_item, taking_item)

    def show_result(self):

        print("Total benefit : {}".format(self.memorize_table[
                                              self.items_count][self.capacity]))

        w = self.capacity
        for n in range(self.items_count, 0, -1):
            if self.memorize_table[n][w] != 0 and self.memorize_table[n][w] \
                    != self.memorize_table[n-1][w]:
                print("we take item :{}".format(n))
                w -= self.items_weight[n]



if __name__ == "__main__":
    numOfItems = 4
    capacityOfKnapsack = 7
    weightOfItems = [0, 1, 3, 4, 5]
    profitOfItems = [0, 1, 4, 5, 7]

    knapsack = Knapsack(numOfItems, capacityOfKnapsack, weightOfItems,
                        profitOfItems)
    knapsack.solve_knapsack_problem()
    knapsack.show_result()


