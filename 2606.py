#바이러스


import sys

def dfs(graph,start,visited):
	global count
	visited[start]=1

	for i in graph[start]:
		if not visited[i]:
			count+=1
			dfs(graph,i,visited)
	return count


if __name__=="__main__":
	input = sys.stdin.readline
	com_num = int(input())
	net_num = int(input())
	visited = [0] *(com_num+1)
	graph = [[0]*(com_num+1) for i in range(com_num+1)]
	
	start = 1
	count = 0

	for i in range(net_num):
		a,b = map(int,input().split())
		graph[a].append(b)
		graph[b].append(a)

	dfs(graph,start,visited)

	print(count-1)