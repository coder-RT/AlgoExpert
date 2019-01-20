#! /usr/bin/python
#-*- coding: utf-8 -*-

def twoNumberSum(array, targetSum):
    # Write your code here.
	resultArray = []
	for i in range(len(array)):
		curr = array[i]
		currTargetSum = targetSum - curr
		for j in range(i+1, len(array)):
			if (currTargetSum - array[j]) == 0:
				if array[i] < array[j]:
					resultArray.append(array[i])
					resultArray.append(array[j])
				else:
					resultArray.append(array[j])
					resultArray.append(array[i])
	print("Result Array: ", resultArray)
	#sotedResultArray = InsertionSort(resultArray)
	#print("Sorted Result Array")
		
if __name__ == '__main__':
	array = [3, 5, -4, 8, 11, 1, -1, 6]
	targetSum = 10
	twoNumberSum(array, targetSum)