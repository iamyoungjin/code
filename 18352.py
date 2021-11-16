#특정거리의 도시 찾기

import sys
import heapq

def dijkstra(start):
	q = []
	heapq.heappush(q,(0,start))
	distance[start] = 0

	while q:
		dist,now = heapq.heappop(q)
		if distance[now] < dist:
			continue
		for k in graph[now]:
			cost = dist + 1
			print(cost)
			if cost < distance[k]:
				distance[k] = cost
				heapq.heappush(q,(cost,k))

if __name__=="__main__":
	INF = int(1e9)
	input = sys.stdin.readline
	n,m,k,x = map(int,input().split()) #노드 개수, 간선 개수, 최단거리가 K인 노드 출력, 출발 노드 번호
	graph = [[]*(n+1) for _ in range(n+1)]
	distance=[INF]*(n+1)


	# 간선 그래프 
	for i in range(m):
		a,b = map(int,input().split())
		graph[a].append((b,1))


	dijkstra(x)

	for a in range(n+1):
		if distance[a] == int(k):
			print(k)
		else:
			print(-1)