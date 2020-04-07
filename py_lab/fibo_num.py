#!/usr/bin/python

n=int(input("fibonacci number? "))

def fibo(n):
	if (n < 3):
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

for i in range(1, n):
	print ("%d," % fibo(i), end='')

print ("%d" % fibo(n))
print("F%d = %d"  % (n, fibo(n)))
