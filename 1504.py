import sys
import heapq


def dijkstra(start):
	distance = [INF] * (n+1)
	graph[start] = 0
	q=[]
	heapq.heappush(q,[0,start])

	while q:
		dist,now = heapq.heappop(q)

		if dist[now] < dist:
			continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    #최단거리배열
	return distance 

if __name__=="__main__":
	input = sys.stdin.readline
	n,e = map(int,input().split())

	graph = [[]*(n+1) for _ in range(n+1)]

	for i in range(n+1):
		a,b,c = map(int,input().split)

		graph.[a].append((b,c))
		graph.[b].append((a,c))



	#방향성이 없는 그래프이기 때문에 두가지 가능성 비교


	v1,v2 = map(int,input().split())
	orign_dist =dijkstra(1)
	v1_dist = dijkstra(v1)
	v2_dist = dijkstra(v2)

	# 1->v1->v2->N
	v1_path = orign_dist[v1]+v1_dist[v2]+v2_dist[n] 
	# 1->v2->v1->N
	v2_path = orign_dist[v2]+v2_dist[v1]+v1_dist[n]

	result = min(v1_path,v2_path)
	print(result if result < INF else -1)
