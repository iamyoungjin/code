#전깃줄 (LIS)

import sys

if __name__=="__main__":

	input = sys.stdin.readline
	n = int(input())
	arr = []
	for i in range(n):
		w = list(map(int,input().split()))
		arr.append(w)
		arr.sort()
	print(arr)


	dp = [1]*n
	for i in range(1,n):
		for j in range(0,i):
			if arr[i][1] > arr[j][1]:
				dp[i] = max(dp[i],dp[j]+1)

	print('arr->',arr)
	print('dp->',dp)

	print('ans->',n-max(dp))
#전기줄이 교차하지 않을 조건 (500이하의 자연수)
#선이 겹치는 경우: 정렬후 값이 큰 숫자에서 더 작은수의 연결 수보다 작은수 로 연결되는 경우
