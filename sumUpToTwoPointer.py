#! /usr/bin/python
#-*- coding: utf-8 -*-

#Time O(N) | Space O(N)
def twoNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	left = 0
	right = len(array) - 1
	
	while left < right:
		sum = array[left] + array[right]
		if sum > targetSum:
			right -= 1
		if sum < targetSum:
			left += 1
		if sum == targetSum:
			return [array[left], array[right]]
	return []
	
	
		
if __name__ == '__main__':
	array = [3, 5, -4, 8, 11, 1, -1, 6]
	targetSum = 10
	result = twoNumberSum(array, targetSum)
	print(result)