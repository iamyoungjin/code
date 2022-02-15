# 네트워크연결 (최소신장 트리 (최소스패닝트리))

'''
문제
도현이는 컴퓨터와 컴퓨터를 모두 연결하는 네트워크를 구축하려 한다. 하지만 아쉽게도 허브가 있지 않아 컴퓨터와 컴퓨터를 직접 연결하여야 한다.
그런데 모두가 자료를 공유하기 위해서는 모든 컴퓨터가 연결이 되어 있어야 한다. 
(a와 b가 연결이 되어 있다는 말은 a에서 b로의 경로가 존재한다는 것을 의미한다. a에서 b를 연결하는 선이 있고, b와 c를 연결하는 선이 있으면 a와 c는 연결이 되어 있다.)

그런데 이왕이면 컴퓨터를 연결하는 비용을 최소로 하여야 컴퓨터를 연결하는 비용 외에 다른 곳에 돈을 더 쓸 수 있을 것이다.
이제 각 컴퓨터를 연결하는데 필요한 비용이 주어졌을 때 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력하라. 모든 컴퓨터를 연결할 수 없는 경우는 없다.

입력
첫째 줄에 컴퓨터의 수 N (1 ≤ N ≤ 1000)가 주어진다.

둘째 줄에는 연결할 수 있는 선의 수 M (1 ≤ M ≤ 100,000)가 주어진다.

셋째 줄부터 M+2번째 줄까지 총 M개의 줄에 각 컴퓨터를 연결하는데 드는 비용이 주어진다.
이 비용의 정보는 세 개의 정수로 주어지는데, 만약에 a b c 가 주어져 있다고 하면 
a컴퓨터와 b컴퓨터를 연결하는데 비용이 c (1 ≤ c ≤ 10,000) 만큼 든다는 것을 의미한다. a와 b는 같을 수도 있다.

출력
모든 컴퓨터를 연결하는데 필요한 최소비용을 첫째 줄에 출력한다.

예제 입력 1 
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
예제 출력 1 
23
'''


#1922 네트워크 연결 - 크루스칼 알고리즘 

import sys

#Find the set which a specific element belongs ( 특정 원소가 속한 집합 찾기 )
def find_parent(parent,x):
	if parent[x] !=x:
		parent[x] = find_parent(parent,parent[x])
	return parent[x]

#Union the set which two elements belong ( 두 원소가 속한 집합 합치기 )
def union_parent(parent,a,b):
	a = find_parent(parent,a)
	b = find_parent(parent,b)

	if a < b:
		parent[b] = a
	else:
		parent[a] = b



if __name__=="__main__":
	input=sys.stdin.readline

	#input the number of Nodes and edges (노드의 개수와 간선(Union 연산)의 개수 입력 받기)
	N = int(input())
	M = int(input())
	
	#initialize the parent table ( 부모 테이블 초기화 )
	parent = [0]*(N+1)
	# The list contains every edges, The value contains final cost ( 모든 간선을 담을 리스트와, 최종 비용을 담을 변수)
	edges = []
	result = 0


	#initialize parents as themselves on the parent table ( 부모 테이블 상에서 부모를 자기 자신으로 초기화 )
	for i in range(1,N+1):
		parent[i] = i

	#input information on all edges ( 모든 간선에 대한 정보 입력 받기 (비용순서))
	for _ in range(M):
		a,b,c = map(int, input().split())
		edges.append((c,a,b))
	edges.sort()

	#check the edges one by one ( 간선을 하나씩 확인하며 )
	for e in edges:
		c,a,b =e
		#Include in the set only if there is no cycle ( 사이클이 발생하지 않는 경우에만 집합에 포함 )
		if find_parent(parent,a) != find_parent(parent,b):
			union_parent(parent,a,b)
			result +=c
	print(result)

