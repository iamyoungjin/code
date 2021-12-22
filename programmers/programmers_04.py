#2021 KAKAO BLIND RECRUITMENT
#Lv1. 신규 아이디 추천


def solution(new_id):
	answer = ''
    # 1단계
    new_id = new_id.lower()

    # 2단계
    for word in new_id:
    	if word.isalnum or word in ['-','_','.']:
    		answer+=word

    # 3단계
    while '..' in answer:
    	answer = answer.replace('..','.')
    	print(answer)

    # 4단계
    if answer[0] == ".":
    	if len(answer) >= 2:
    		answer = answer[1:]
    if answer[-1]==".":
    	answer=answer[:-1]

    # 5단계
    if answer == '':
    	answer = 'a' 
    	
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 3:
        answer = answer + answer[-1] 
    return answer


if __name__ == '__main__':
	input = sys.stdin.readline
	new_id = input()
	print(solution(new_id))


