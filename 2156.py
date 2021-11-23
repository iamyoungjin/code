#포도주 시식

if __name__=="__main__":

	n = int(input())
	arr = []
	for i in range(n):
		arr.append(int(input()))
	print('arr:',arr)
	dp =[0]*10000

	dp[0] = arr[0]
	dp[1] = arr[0]+arr[1]
	dp[2] = max(arr[1],arr[0]+arr[2],arr[1]+arr[2])

	for i in range(3,n):
		dp[i]=max(arr[i]+dp[i-2],arr[i]+arr[i-1]+dp[i-3],dp[i-1])
	print('dp:',dp)
	print('max:',max(dp))

'''
경우의 수: 현재 포도주를 마실 지 말지 

① 현재 포도주와 이전 포도주를 마시고 전전 포두주는 마시지 않는다. ( arr[i]+arr[i-1]+dp[i-3] )

② 현재 포도주와 전전 포도주를 마시고 이전 포도주는 마시지 않는다. ( arr[i]+dp[i-2] )

③ 현재 포도주를 마시지 않는다. ( dp[i-1] )

이 세 가지 경우로 나눌 수 있다.

이 때, 3번케이스의 경우 dp[i-2]+arr[i-1] 로 표기하지 않은 이유는 dp[i-1]에 해당 케이스를 포함한 최댓값이 저장되어 있기 때문이다.

* 여기서 두번 연속 건너뛰는 경우의 수가 들어가지 않는 이유는 최대값이 형성이 되기 때문

'''
