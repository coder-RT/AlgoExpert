#! /usr/bin/python
#-*- coding: utf-8 -*-

#Time O(N3) | Space O(N)
def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	result = []
	for i in range(len(array)):
		for j in range((i+1),len(array)):
			for k in range((j+1), len(array)):
				currSum = array[i] + array[j] + array[k]
				if currSum == targetSum:
					result.append([array[i], array[j], array[k]])
	return result
	
	
		
if __name__ == '__main__':
	array = [12, 3, 1, 2, -6, 5, -8, 6]
	targetSum = 0
	result = threeNumberSum(array, targetSum)
	print(result)