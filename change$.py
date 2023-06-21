# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def count_change(coins, target):
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

coins = [1, 5, 10, 25, 50]
target_amount = 100  # 100 cents = $1

num_ways = count_change(coins, target_amount)
print("Number of ways to make change for $1:", num_ways)
