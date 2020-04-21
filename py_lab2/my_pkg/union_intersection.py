#!/usr/bin/python

def uni_inter():
	list1=input("1st list: ")
	list1=list1.replace(',', ' ')
	list1=list1.replace('[', ' ')
	list1=list1.replace(']', ' ')
	list1=list1.split()
	s1 = set(list1)

	list2=input("2nd list: ")
	list2=list2.replace(',', ' ')
	list2=list2.replace('[', ' ')
	list2=list2.replace(']', ' ')
	list2=list2.split()
	s2 = set(list2)

	l3=list(s1|s2)
	l4=list(s1&s2)
	l3.sort()
	l4.sort()
	l3=",".join(l3)
	l4=",".join(l4)
	print("=> union [", end='')
	print(l3, end='')
	print("]")
	print("=> intersection [", end='')
	print(l4, end='')
	print("]\n")
