#DFS와 BFS

'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 
간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. 
V부터 방문된 점을 순서대로 출력하면 된다.
'''

import sys

def dfs(v):
	print(v,end=' ')
	visited[v] = True
	for i in graph[v]:
		if not visited[i]:
			dfs(i)



def bfs():
	pass


if __name__== "__main__":
	input = sys.stdin.readline
	n,m,v = map(int,input().split())
	print('n,m,v->',n,m,v)
	visited = [False] * (n+1)
	graph = [[] for _ in range(n+1)]
	# for i in range(1,n+1):
	# 	if visited[i] == False:
	# 		dfs(i)
	print('visited->',visited)

	for _ in range(m):
		a,b = map(int,input().split())
		graph[a].append(b)
		graph[b].append(a)
	print('graph->',graph)

	dfs(v)

'''
<다음 주 월요일 리딩 단어시험>

conceive 상상하다, 생각하다
vigorous 활발한 [ˈvɪɡərəs]
demand 필요, 요구, 수요
facilitate 가능케하다
teleworking 재택근무
trend 경향, 추세, 추이
substantial 상당한
fleet 함대, 무리
as far as … is/are concerned …에 관해서는
extent 범위
internal 내부의
frontier 국경
abolish 폐지하다
phenomenon 현상[fənɑːmɪnən]
emphasise 강조하다
relocation 재배치
labour intensive 노동 집약적인
assembly plant 조립 공장
candidate 후보
haulage 화물 수송[ˈhɔːlɪdʒ]
volume 양, 용적
inherit 물려받다, 상속받다
distribution 분배
tip in favour of …에 유리하게 움직이다
enlarged 확대된
on average 평균적으로
imperative 반드시 필요한 것, 해야하는 것 e[ɪmˈperətɪv]
sustainable 지속 가능한
adapt 맞추다, 적응하다
Integrate A into B : A를 B에 통합하다
lie at the heart of …의 중심에 놓여있다
proposed 제기된, 제시된
measure 방식, 방법
blame for …에 대해 비난하다
leading 가장 중요한
estimate 추정
reverse 뒤집다
culprit 장본인, 범인
account for …의 이유가 되다
attributable to …에 기인하는
ecological 생태학적인
overnight 하룻밤 사이에
deterioration 악화
in favour of …에 우호적인
freight 화물
marginalisation 소외, 부차화
market share 시장 점유율
emerge 등장하다
consist of …로 구성되다
solely 단독으로
pricing 가격 책정
be accompanied by …를 동반하다
complementary 상호 보완적인
curb 억제하다
ratio 비율, 비 [reɪʃioʊ]
revitalise 재활성화하다
logistics 실행계획
cohesion 화합, 결합, 응집력[koʊhiːʒn]
saturated 포화된, 흠뻑젖은[ˈsætʃəreɪtɪd]
artery (도로, 강, 철도 등의) 동맥[ɑːrtəri]
range from A to B : A에서 B에 이르다
bear in mind …을 고려하다
imbalance 불균형
'''