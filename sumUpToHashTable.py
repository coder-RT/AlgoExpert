#! /usr/bin/python
#-*- coding: utf-8 -*-

#Time O(N) | Space O(N)
def twoNumberSum(array, targetSum):
    # Write your code here.
	hashTable = {}
	for item in array:
		potentialMatch = targetSum - item
		if potentialMatch in hashTable:
			if potentialMatch > item:
				return [item, potentialMatch]
			else:
				return [potentialMatch, item]
		else:
			hashTable[item] = True
	return []
	
		
if __name__ == '__main__':
	array = [3, 5, -4, 8, 11, 1, -1, 6]
	targetSum = 10
	result = twoNumberSum(array, targetSum)
	print(result)