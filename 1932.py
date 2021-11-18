#정수 삼각형 
import sys

def dp(n):
	for i in range(1,n):
		for j in range(i+1):
			if j == 0:
				dp[i][j] = dp[i-1][j]+a[i][j]
			elif j == i:
				dp[i][j] = dp[i-1][j-1]+a[i][j]
			else:
				dp[i][j] = max(dp[i-1][j-1] + a[i][j],dp[i-1][j]+a[i][j])
	return dp

if __name__=="__main__":
	input = sys.stdin.readline
	n = int(input())
	dp = [[0]*(n+1) for i in range(n+1)]

	res = dp(n)

	print(res)

'''
ij  
	7
	3 8
	8 1 0
	2 7 4 4 
	4 5 2 6 5 



'''
import sys

read = sys.stdin.readline
lst = []
n = int(read())

#각 줄마다 입력하는 숫자들을 리스트로 만들고 순서에 맞게 리스트들을 lst안에 넣는다
for _ in range(n):
	lst.append(list(map(int,read().split())))

#lst안에 있는 리스트들을 차례대로 하나씩 꺼낸다 하지만 2번째 리스트 부터 꺼낸다.
for i in range(1,n):
	#그다음 for loop는 각 리스트 안에 이는 숫자들을 불러온다
	for j in range(len(lst[i])):
		if j==0: #i번째 리스트의 index가 0일때
			lst[i][j] += lst[i-1][j]
		elif j == len(lst[i]-1): #i번째 리스트의 마지막 숫자 일때: j가 -1이 될 수 없기 때문에 리스트 길이에 -1을 한다
			lst[i][j] += lst[i-1][j-1]
		else: #리스트 중간에 있는 값들은 연결되어 있는 그전 리스트 두개와 비교해서 가장 큰 값으로 한다
			lst[i][j] += max(lst[i-1][j-1],lst[i-1][j])
print(max(lst[n-1]))