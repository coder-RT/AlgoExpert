#! /usr/bin/python
#-*- coding: utf-8 -*-

def coinChange(denominationArray, target):
	ways = [0] * len(range(target+1))
	ways[0] = 1
	for denomination in denominationArray:
		for amount in range(len(ways)):
			if denomination <= amount: 
				ways[amount] = ways[amount] + ways[amount-denomination]
	return ways[-1]

if __name__ == '__main__':
	denominationArray = [1, 5, 10, 25]
	target = 10
	result = coinChange(denominationArray, target)
	print(result)