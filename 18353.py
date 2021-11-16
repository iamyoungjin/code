#LIS(Longest Increasing Subsequence)

n = int(input())
array = list(map(int,input().split()))
#순서를 뒤집어 '최장 증가 부분수열 문제로 변환'
array.reverse()

#dp를 위한 1차원 dp테이블 초기화
dp = [1]*n 

#가장 긴 증가부분수열(LIS)알고리즘 수행
for i in range(1,n):
	for j in range(0,i):
		if array[j] < array[i]:
			dp[i] = max(dp[i],dp[j]+1)

#열외해야 하는 병사의 최소수 출려
print(n-max(dp))