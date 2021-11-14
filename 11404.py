import sys

def floyd():
	for a in range(1,n+1):
		for b in range(1,n+1):
			if a==b:
				graph[a][b]=0

	for _ in range(m):
		#A에서 B로 가는 비용은 C라고 설정
		a,b,c = map(int,input().split())
		graph[a][b]=c

	for k in range(1,n+1): #k는 거쳐가는노드
		for a in range(1,n+1): #a는 출발노드
			for b in range(1,n+1): #b는 도착노드
				graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])


if __name__=="__main__":
	input = sys.stdin.readline
	INF = int(1e9)
	n = int(input())
	m = int(input())
	graph = [[INF]*(n+1) for _ in range(n+1)]

	floyd()

	#수행된 결과를 출력
	for a in range(1,n+1): 
		for b in range(1,n+1):
			#도달할 수 없는 경우 무한이라고 출력
			if graph[a][b]==INF:
				print('INFINITY',end=" ")
			#도달할수 있는 경우 거리 출력
			else:
				print(graph[a][b],end=" ")
		print()
