"""
Coin change problem:
- Given a set of coin v[]
- Given an M amount (the total)
- How many ways the coin v[] can be combined in order to get the total M
- The order of coin does not matter.

Example:
    Coins v[] = {1, 2, 3}
    Total amount M = 4
    Combination:
    {1, 1, 1, 1}, {1, 1, 2}, {1, 3}, {2, 2} >> the order does not matter.

Solution:
- Recursion:
    > The naive approach is to use a simple recursive method
    > For every single coin we have two options; include or exclude
    > Exponential time complexity O(2^N) where N is the number of coins
- dynamic programming approach:
    > we have to calculate the solution matrix:
                    # row              # col
        dqpTable[num_of_coins + 1][total_amount + 1]
    > the base case:
        -> if total_amount is 0 -> there is 1 to make the change because we do
           not include any coin
        -> if number_of_coins is 0 -> there is 0 way to change the amount
    > for every coin: make a decision whether to include or not
    > check if the coin value is less than or equal to the amount needed.
        -> if yes: then we will find ways by including that coin and
        excluding that coin.
            1. include the coin: reduce the amount by coin value and use
               sub-problem solution // total_amount - v[i]
            2. exclude the coin: solution for the same amount without
               considering that coin.
    > running time complexity is O(v*M)

                                # base case
    dpTable[i][j] =             0 if j 0
                                1 if j 0
                     # if the coin value is smaller than the amount
                     dpTable[i-1][j] + dpTable[i][j-v[i-1] if v[i] <= j

                     # if the coin value is grater that the amount
                     dpTable[i-1][j] if v[i] > j

"""


class CoinChange(object):

    def __init__(self, coins, amount):
        self.coins = coins
        self.amount = amount
        self.dpTable = [[0]*(amount + 1) for _ in range(len(coins) + 1)]

    def change_coin_naive(self, amount, index):
        if amount < 0:
            return 0
        if amount == 0:
            return 1

        if index == len(self.coins):
            return 0

        return self.change_coin_naive(amount - self.coins[index], index) + \
               self.change_coin_naive(amount, index + 1)


    def change_coin_dp(self):

        self.dpTable = [[0] * (self.amount + 1) for x in range(len(self.coins) + 1)]

        for i in range(len(self.coins) + 1):
            self.dpTable[i][0] = 1

        for i in range(1, len(self.coins) + 1):
            for j in range(1, self.amount + 1):
                if self.coins[i - 1] <= j:
                    self.dpTable[i][j] = self.dpTable[i - 1][j] + \
                                         self.dpTable[i][j- self.coins[i - 1]]
                else:
                    self.dpTable[i][j] = self.dpTable[i - 1][j]

        print("solution is : {}".format(self.dpTable[len(self.coins)][self.amount]))


if __name__ == "__main__":
    M = 4
    coins = [1, 2, 3]

    coinChange = CoinChange(coins, M)
    #coinChange.change_coin_dp()
    total_way = coinChange.change_coin_naive(M, 0)
    print("coin chage naive approach of {} : {}".format(M, total_way))
