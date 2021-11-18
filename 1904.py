#01타일 (전형적인 dp)

def dp_cnt(n):
	dp[1] = 1
	dp[2] = 2

	for i in range(3,n+1):
		dp[k] = dp[k-1] + dp[k-2]

	return dp[k]

if __name__=="__main__":
	dp = [0] * 1000001
	n = int(input())
	num = dp_cnt(n)
	print(num%15746)