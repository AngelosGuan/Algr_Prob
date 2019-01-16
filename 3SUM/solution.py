import numpy as np

# Takes in a sequence and a sum to find
# iterate through the arr without duplicate, then iterate from start and end of right side
# if sum of two numbers > desired, move back right pointer; else move forward left pointer
# remove duplicate of left and right pointer
# result should be unique then

def solve_3SUM(arr,res):
	l = len(arr)
	if l < 3:
		return []

	arr.sort()

	ans = []

	i = 0
	while i < l:

		if(float(arr[i])>res/3.0):
			return ans

		target = res - arr[i]
		left = i + 1
		right  = l - 1
		while (left < right):
			total = arr[left] + arr[right]

			if total > target:
				right -= 1
			elif total < target:
				left += 1
			else:
				a = arr[i]
				b = arr[left]
				c = arr[right]
				ans.append( (a, b, c) )
				while(left < right and arr[left]==b):
					left += 1
				while(left < right and arr[right]==c):
					right -= 1
		while ( i+1 < l and arr[i] == res-target):
			i += 1

	return ans