#exercise 1:
def MakeaNewList(list):
	first = list[0]
	last = list[-1]
	print(first, last)

MakeaNewList([5, 10, 15, 20, 25])

#exercise 2:
def numbers(num):
	for x in num:
		if x<5:
			print(x)
numbers([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

#exercise 3:
def NoDuplicates(com):
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	for x in a: 
		for y in b: 
			if x == y:
				print(x)