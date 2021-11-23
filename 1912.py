#연속합


import sys

if __name__=="__main__":

	n = int(input())
	dp = [0]*n
	arr = list(map(int,input().split()))

	#print(arr)
	dp[0] = arr[0]

	for i in range(1,n):
		print('i->',i)
		dp[i] = max(arr[i],dp[i-1]+arr[i])

	#print(dp)
	print(max(dp)) 
