import sys
import math


def isPrime(n):
	if i == 1:
		return False
	else:
		for n in range(2,int(math.sqrt(n))+1):
			if i%n == 0:
				return False
		return True


if __name__=="__main__":
	m,n = map(int,input().split())

	for i in range(m,n+1):
		if isPrime(i):
			print(i)