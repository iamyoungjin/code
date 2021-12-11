#단지번호붙이기


import sys
import collections
sys.setrecursionlimit(10**6)

def dfs(y, x, cnt):
    visited[y][x] = 1
    cnt += 1
    print('cnt-->',cnt)

    for i in range(4): 
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < n and 0 <= nx < n: #범위 체크
            if graph[ny][nx] == 1  and visited[ny][nx] == 0:
                cnt = dfs(ny, nx, cnt)

    return cnt




if __name__=="__main__":
	n = int(input())
	graph = []
	for _ in range(n):
	    graph.append(list(map(int,input())))
	visited = [[0 for _ in range(n)] for _ in range(n)]

	dy = [-1,0,1,0]
	dx = [0,1,0,-1]
	result = []

	for i in range(n):
	    for j in range(n):
	        if graph[i][j] and not visited[i][j]:
	            result.append(dfs(i, j, 0))
	print(len(result))
	result.sort()
	for i in result:
	    print(i)

