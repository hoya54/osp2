#!/usr/bin/python

N = int(input("input N : "))
i=0
sum=0

while i < N:
	num = int(input("enter the num : "))
	sum = sum + num
	i=i+1
average = sum/N
print("average = %f" % average)
