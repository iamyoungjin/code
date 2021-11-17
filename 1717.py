#union find
import sys



def union(a,b):
	a = find(a)
	b = find(b)

	if a == b:
		return
	if a < b:
		parent[b]=a
	else:
		parent[a]=b

def find(a):
	if a == parent[a]:
		return a
	p = find(parent[a])
	parent[a] = p
	return parent[a]

if __name__=="__main__":
	input = sys.stdin.readline

	parent = [0] * (N+1)
	for i in range(n+1):
		parent[i] = int

	n,m = map(int,input().split())

	for _ in range(n+1):
		op,a,b = map(int,input().split())
		if op == 0:
			union()
		else op ==1:
			if find(a) == find(b):
				print('YES')
			else:
				print('NO')