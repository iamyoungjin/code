#순열 사이클
'''

문제
1부터 N까지 정수 N개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 
Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다.
이러한 사이클을 "순열 사이클" 이라고 한다. N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다.
둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.
출력
각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.
'''
import sys

def dfs(start, visited):
	visited[start] = True
	for i in graph[start]:
		if not visited[i]:
			dfs(i,visited)

if __name__=='__main__':
	input = sys.stdin.readline
	t = int(input()) # 2≤t≤1000
	nodes = list(map(int,input().split()))
	graph = [[] for _ in range(t+1)]
	visited = [False]*(t+1)
	count = 0

	for i in range(1,t+1):
 		graph[i].append(nodes[i-1])
 		graph[nodes[i-1]].append(i)
 		#print(graph)

    for i in range(1,t+1):
        if not visited[i]:
            count += 1
            dfs(i, visited)

    print(count)

