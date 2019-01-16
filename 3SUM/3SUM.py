"""Takes a sequence of number as argument
   print out number of such pairs and the pairs
"""
import sys
import solution.py as soln

raw_in = sys.argv
del raw_in[0]
arr = []

for elem in raw_in:
	try:
		num = int(elem)
		arr.append(num)
		break
	except:
		print("enter number sequence")
		sys.exit

ans = soln.solve_3SUM(arr)

print("total number is: " + len(ans)+".")
print(ans)

