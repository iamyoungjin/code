#숨박꼭질2

# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
# 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 그리고, 
# 가장 빠른 시간으로 찾는 방법이 몇 가지 인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

# 둘째 줄에는 가장 빠른 시간으로 수빈이가 동생을 찾는 방법의 수를 출력한다.

# 예제 입력 1 
# 5 17
# 예제 출력 1 
# 4
# 2



import sys
from collections import deque


def bfs():
	find_method_cnt = 0
	short_time = -1

	queue = deque()
	queue.append((N,0))
	if N == 0:						# 시작점일 경우 +1 밖에 방법이 없다.
		queue.append((N+1,1))

	while queue:
		tmp, cnt = queue.popleft()
		visited[tmp] = True			# 방문처리

		if tmp == K:				# 동생을 찾은 경우
			if short_time == -1:	# 한번에 바로 찾은 경우
				short_time = cnt
			if short_time == cnt:	# 한번에 바로 찾은 경우가 아닐때
				find_method_cnt +=1 
			else:
				break

		if 100000 >= tmp and tmp > 0:
			if visited[tmp - 1] == False:	# 뒤로 
				queue.append((tmp-1, cnt+1))
			if visited[tmp+1] == False:		# 앞으로 
				queue.append((tmp+1,cnt+1))
			if visited[tmp*2] == False:		# 순간 이동
				queue.append((tmp*2,cnt+1))

	print(short_time,find_method_cnt)



if __name__ == "__main__":
	input = sys.stdin.readline
	N, K = map(int, input().split())
	visited = [False] * 100001  

	bfs()

