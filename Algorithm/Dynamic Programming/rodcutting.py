"""
Rod cutting:
 - given a rod with certain length L
 - given the prices of different lengths
 - how to cut the rod in order to maximize the profit

 Recursive method:
 - use a simple recursive approach
 - N-1 cuts can be made in the rod of length N
 - there are 2^N-1 way to cut the rod
 - problem >> the time complexity and overlapping sub-problem
 - running time complexity is exponential O(2^N) where N is the rod length
 for every length we have to options whether cut or not.

Dynamic programming:
- we have create a solution matrix:
    dpTable = [num_of_lengths + 1][total_length + 1]
                //row               // col

- we have define the base case:
    if total_length is 0 -> then the profit is 0
    if we do not consider any lengths -> thr profit is 0

    dpTable[i][j] =     0 if j = i and j = 0

                        # if the price is smaller or equal the rod
                        max(dpTable[i - 1][j], prices[i] + dpTable[i][j - 1]
                        if i <= j

                        # if the prices is greater than the length of the rod
                        dpTable[i-1][j] if i > j


- running time complexity is O(num_of_lengths * total_length)

"""


class RodCutting(object):

    def __init__(self, length, prices):
        self.length = length
        self.prices = prices
        self.dpTable = [[0] * (length + 1) for _ in range(len(prices))]

    def solve_rod_cutting(self, length, prices):

        self.dpTable = [[0] * (length + 1) for _ in range(len(prices))]

        for i in range(1, len(prices)):
            for j in range(1, length + 1):

                if i <= j:
                    self.dpTable[i][j] = max(self.dpTable[i - 1][j], prices[
                        i] + self.dpTable[i][j - i])
                else:
                    self.dpTable[i][j] = self.dpTable[i - 1][j]

        # show result
        self.show_result()

    def show_result(self):

        print("Maximum profit is : {}".format(self.dpTable[len(self.prices)-1][self.length]))
        col_index = self.length
        row_index = len(self.prices) - 1 # exclude base case

        while col_index > 0 or row_index > 0:
            if self.dpTable[row_index][col_index] == self.dpTable[row_index -
                                                                  1][col_index]:
                row_index -= 1
            else:
                print("we make cut: {}".format(row_index))
                col_index -= row_index


if __name__ == "__main__":
    length = 5
    prices = [0,2,5,7,3]

    rodCutting = RodCutting(length, prices)
    rodCutting.solve_rod_cutting(length, prices)






