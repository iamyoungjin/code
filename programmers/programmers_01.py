#2021 Dev-Matching:웹 백엔드 개발자(상반기)
#Lv1. 로또의 초고 순위와 최저 순위



'''
알아볼 수 없는 번호를 0으로 표기하기로 하고, 
민우가 구매한 로또 번호 6개가 44, 1, 0, 0, 31 25라고 가정해보겠습니다. 
당첨 번호 6개가 31, 10, 45, 1, 6, 19라면, 당첨 가능한 최고 순위와 최저 순위의 한 예는 아래와 같습니다.


당첨 번호	31	10	45	1	6	19	결과
최고 순위 번호	31	0→10	44	1	0→6	25	4개 번호 일치, 3등
최저 순위 번호	31	0→11	44	1	0→7	25	2개 번호 일치, 5등


순서와 상관없이, 구매한 로또에 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정됩니다.
알아볼 수 없는 두 개의 번호를 각각 10, 6이라고 가정하면 3등에 당첨될 수 있습니다.
3등을 만드는 다른 방법들도 존재합니다. 하지만, 2등 이상으로 만드는 것은 불가능합니다.
알아볼 수 없는 두 개의 번호를 각각 11, 7이라고 가정하면 5등에 당첨될 수 있습니다.
5등을 만드는 다른 방법들도 존재합니다. 하지만, 6등(낙첨)으로 만드는 것은 불가능합니다.
민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 매개변수로 주어집니다.
이때, 당첨 가능한 최고 순위와 최저 순위를 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.
'''
#완료

import sys

def solution(lottos, win_nums):
    answer = [0]*2
    count = 0

    rank = [1,2,3,4,5,6]

    for i in range(6):
    	for j in range(6):
    		if lottos[i] == win_nums[j]:
    			count+=1

    if count != 0: 
	    answer[0]=7-count-2
	    answer[1]=7-count
	    for i in range(len(answer)):
	    	if answer[i] <= 0:
	    		answer[i] = 1
    return answer

if __name__ == '__main__':
	input = sys.stdin.readline
	lottos = list(map(int,input().split(',')))
	win_nums = list(map(int,input().split(',')))


	lottos.sort() 
	win_nums.sort()

	print(solution(lottos,win_nums))

