
def fibo(num):
    zero_cnt = [1,0]#0일때 초기화 0:1번, 1:0번
    one_cnt = [0,1]#1일때 초기화 0:0번, 1:1반
    if num <= 1:
        return
 
    for i in range(2, num+1):#1이후는 점화식으로 추가
        zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
        print('zero_cnt->',zero_cnt)
        one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
        print('one_cnt->',one_cnt)

    return zero_cnt, one_cnt


if __name__=="__main__":
 
	t = int(input())
	lst = []
	zero_cnt, one_cnt = fibo(40)
	 
	for k in range(t):
	    n = int(input())

		lst.append([zero_cnt[n],one_cnt[n]])
	print(lst)

