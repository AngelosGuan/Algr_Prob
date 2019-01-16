"""Takes a sum result and a sequence of number as argument
   print out number of such pairs and the pairs
"""
import sys
from solution import solve_3SUM

raw_in = sys.argv
try:
	res = int(sys.argv[1])
except:
	print("enter integer sum")
	sys.exit

del raw_in[0]
del raw_in[1]
arr = []

for elem in raw_in:
	try:
		num = int(elem)
		arr.append(num)
	except:
		print("enter number sequence")
		sys.exit

ans = solve_3SUM(arr,res)

k = len(ans)

if k==0:
	print("No answer found.")
else:
	for i in range(0,k):
		a = ans[i][0]
		b = ans[i][1]
		c = ans[i][2]
		if (a+b+c != res):
			print("solution wrong")
			sys.exit()
		for j in range(i+1, k):
			other = ans[j]
			if ((a,b,c)==other) or ((a,c,b)==other) or ((b,a,c)==other) or ((b,c,a)==other) or ((c,a,b)==other) or ((c,b,a)==other):
				print("solution has duplicate")
				print(ans)
				sys.exit()

	print("total number is: " + str(k) + ".")
	print(ans)



