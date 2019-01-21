#! /usr/bin/python
#-*- coding: utf-8 -*-

#Time O(N2) | Space O(N)
def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	result = []
	for i in range(len(array)):
		left = i+1
		right = len(array) - 1
		while left < right:
			currSum = array[i] + array[left] + array[right]
			if currSum == targetSum:
				result.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif currSum < targetSum:
				left += 1
			else:
				right -= 1
	return result
	
	
		
if __name__ == '__main__':
	array = [12, 3, 1, 2, -6, 5, -8, 6]
	targetSum = 0
	result = threeNumberSum(array, targetSum)
	print(result)