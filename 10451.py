
#수정중

import sys



def dfs(idx):
	visited[idx] = True
	next =  arr[idx-1]
	print(next,end='')
	print('arr->',arr)
	print('visited->',visited)
	if visited[next] ==0:
		dfs(next)





if __name__=='__main__':
	input = sys.stdin.readline
	#T = int(input())
	N = int(input())
	arr = list(map(int,input().split()))
	visited = [False]*(len(arr)+1)
	answer=0


	print('first_arr->',arr)
	print('first_visited->',visited)
	visited[1] = True
	
	for i in range(1,N+1):
		if visited[i] == False:
			print('i->',i)
			dfs(i)
			answer+=1
		print('answer->',answer)

	print(answer)
