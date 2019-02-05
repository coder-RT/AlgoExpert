#! /usr/bin/python
#-*- coding: utf-8 -*-

# find the max subset sum : non adjacent values

#Time O(N) | Space O(N)
def maxSubsetSum(array):
    # if array is empy
	if not len(array):
		return []
	#if array has only one element
	elif len(array) == 1:
		return array[0]
	# base condition
	maxSum = array[:]
	maxSum[1] = max(array[0], array[1])
	for i in range(2, len(array)):
		maxSum[i] = max ()

		
if __name__ == '__main__':
array = [75, 105, 120, 75, 90, 135]
result = maxSubsetSum(array)
print(result)