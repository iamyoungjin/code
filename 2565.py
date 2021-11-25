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
'''
*LIS
한 기둥을 기준으로 더 밑에 들어있는 숫자가 위에서 선택한 반대쪽 기둥으 수보다 높은 수를 선택하면 안됨

N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().split())))

lineList.sort()

dp = [1]*N
for i in range(N):
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1
print(N-max(dp))
'''
