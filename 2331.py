import sys

if __name__=="__main__":
	input = sys.stdin.readline
	a,p = map(int,input().split())

	d = [a]

	while True:
		tmp = 0
		for i in str(d[-1]):
			tmp += int(i)**p

		if tmp in d:
			break
		d.append(tmp)

print(d.index(tmp))


#DFS로 풀 수 있는 이유와 코드 추가