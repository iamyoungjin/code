# 가장 먼저 1 연산을 실행하는 이유가 이해가 되지 않음

if __name__=="__main__":
n = int(input())
d = [0]*(n+1)
d[1] = 0
for i in range(2, n+1):
    d[i] = d[i-1] + 1      #1을 왜 먼저 실행하는지 이해가 되지 않음...
    if i%2 == 0 and d[i] > d[i//2] + 1:
        d[i] = d[i//2] + 1
    if i%3 == 0 and d[i] > d[i//3] + 1:
        d[i] = d[i//3] + 1
print(d[n])
