#음식물 피하기
import sys

def dfs(x,y):
    global count
    count+=1
    visited[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if graph[nx][ny]=="#" and visited[nx][ny]==0:
                dfs(nx,ny)
    return count

if __name__=="__main__":
	input = sys.stdin.readline
	n,m,k = map(int,input().split())
	graph = [[0]*(m) for _ in range(n)]
	visited = [[0]*(m) for _ in range(n)]

	for _ in range(k):
		r,c = map(int,input().split())
		graph[r-1][c-1] = "#"

	dx=[-1,1,0,0] 
	dy=[0,0,-1,1]

	count = 0
	result=[]

	for i in range(n):
	    for j in range(m):
	        if graph[i][j]=="#" and visited[i][j]==0:
	            result.append(dfs(i,j))
	            count = 0

	print(max(result))
