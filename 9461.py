#파도반 수열


#  1, 1, 1, 2, 2, 3, 4, 5, 7, 9

if __name__=="__main__":
	p = [ 0 for i in range(101)]

	p[0]= 1
	p[1]= 1
	p[2]= 1

	for i in range(0,98):
		p[i+3] = p[i]+p[i+1]
		#p[i+3] = p[i-2]+p[i-3]

	t = int(input())

	for i in range(t):
		n = int(input())
		print(p[n-1])







