#음료수 얼려먹기

'''
[문제]
N * M 크기의 얼음 틀이 있습니다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다. 
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하세요.
 

[입력 조건]
1. 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N, M <= 1,000)
2. 두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어집니다.
3. 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.


[출력 조건]
한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.
'''


def dfs(i,j):
	if i<0 or i>=n or j<0 or j>=m:
		return False

	if graph[i][j] == 0:
		graph[i][j] = 1
		dfs(i-1,j)
		dfs(i+1,j)
		dfs(i,j-1)
		dfs(i,j+1)
		return True
	return False


if __name__ =="__main__":

	n, m = map(int,input().split())

	graph = []

	for i in range(n):
		graph.append(list(map(int,input())))

	for i in range(n):
		for j in range(m):
			if dfs(i,j) == True:
				count+=1

print(result)