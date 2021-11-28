#나무 자르기




if __name__ == '__main__':

	n,m = list(map(int,input().split()))
	array = list(map(int,input().split()))

	start = 0 
	end = max(array)
	result = 0

	while(start<=end):
		total = 0 
		print('array->',array)

		print('start->',start)
		print('end->',end)

		mid = (start+end)//2
		print('mid->',mid)

		for i in array:
			if i>mid:
				total += i-mid
				print('i->',i)
				print('total->',total)
		print('result->',result)

		if total < m:
			end = mid-1
		else:
			result = mid
			start = mid+1

	print(result)

