import sys

#그래프의 모든 정점을 방문해야하므로 bfs,dfs 어떤걸 사용해도 상관 없음
def dfs_W(x,y):
	global cnt_w
	if x<=-1 or x>=m or y<=-1 or y>=n:
		return False
	if graph[x][y] =="W" and visited[x][y] == 0:
		visited[x][y] = 1
		cnt_w +=1

		for i in range(4):
			dfs_W(x+dx[i],y+dy[i])
	return cnt_w


def dfs_B(x,y):
	global cnt_b 
	if x<=-1 or x>=m or y<=-1 or y>=n:
		return False
	if graph[x][y] =="B" and visited[x][y] == 0:
		visited[x][y] = 1
		cnt_b +=1
		for i in range(4):
			dfs_B(x+dx[i],y+dy[i])
	return cnt_b

if __name__=='__main__':
	input = sys.stdin.readline
	n,m = map(int,input().split())
	graph = []
	visited = [[0]*n for _ in range(m)]

	for i in range(m):
		graph.append(list(map(str,input())))

	dx = [1,-1,0,0]
	dy = [0,0,1,-1]

	cnt_w ,cnt_b = 0, 0
	res_w=[]
	res_b=[]
	for i in range(m):
		for j in range(n):
			if dfs_W(i,j):
				w = dfs_W(i,j)
				res_w.append(w**2)
				cnt_w = 0
			elif dfs_B(i,j):
				b = dfs_B(i,j)
				res_b.append(b**2)
				cnt_b = 0

	# print('res_w>',res_w)
	# print('res_b>',res_b)
	print(sum(res_w),sum(res_b))
