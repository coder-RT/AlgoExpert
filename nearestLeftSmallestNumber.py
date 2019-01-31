#code

# find the nearest smallest number to the left of a given number in an array
def immediateSmaller(array):
    stack = list()
    for elem in array:
        # pop till stack contains an element lesser than that of curent element
        while (len(stack) > 0 and stack[-1] > elem):
            stack.pop()
        # if all elements were greater
        if (len(stack) == 0):
            print(-1, end = " ")

        else:
            print(stack[-1], end = " ")
        
        stack.append(elem)

N = int(input())

for test_case in range(N):
    size = int(input())
    array = [elem for elem in input().strip().split()]
    immediateSmaller(array)