#계단 오르기


# 1칸 또는 2칸씩 이동 가능
# 연속 세칸 이동이 불가능
# 마지막 도착 계단은 반드시 밟아야 함 


if __name__ == '__main__':

	n = int(input())
	dp = [0 for i in range(301)] #[0]*301
	arr = [0 for i in range(301)]
	for i in range(n):
		arr[i] = int(input())

	dp[0] = arr[0]
	dp[1] = arr[0] + arr[1]
	dp[2] = max(arr[0]+arr[2], arr[1]+arr[2])

	for i in range(3,n):
		dp[i]= max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]) #dp[i-1]이 아니라 dp[i-3]+arr[i-1]인 이유는? : 마지막 전 단계를 밟아야 되는 경우로 설정



	print(dp[n-1])
