#LCS (Longest Common Substring 문제)

'''
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 
모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 
최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK

예제 출력 1 
4
'''


def Lcs(dp):
	for i in range(1,l1 + 1) :
		for j in range(1,l2 + 1) :
		    if s1[i-1] == s2[j-1] :	# 문자가 같다면
		        dp[i][j] = dp[i-1][j-1] + 1 # 이전까지의 문자열 공통개수(왼쪽 대각선 한칸 위) 길이에 +1	
		    else :	# 두 문자가 다르다면
		        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) #큰 값 표시

		# print(dp)

	print(dp[l1][l2])

if __name__=='__main__':
	s1 = list(input()) # 첫번째 문자열
	s2 = list(input()) # 두번째 문자열
	l1 = len(s1) # 첫번째 문자열 길이
	l2 = len(s2) # 두번째 문자열 길이
	
	dp = [[0]*(l2 + 1) for _ in range(l1+1)]  # 길이를 저장할 이차원 배열 생성
	Lcs(dp)

