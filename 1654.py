#랜선 자르기 



import sys

if __name__=="__main__":
	input = sys.stdin.readline
	k,n = map(int,input().split())

	line = []

	for _ in range(k):
		line.append(int(input()))

	print(line)

	start = 0
	end = max(line)

	while (start<end):
		mid = (start+end)//2
		cnt = 0
		for i in line:
			cnt+= i//mid
		if cnt>=n:
			start = mid+1
		else:
			end = mid-1
		print('start-->',start)
		print('end-->',end)

	print(end)