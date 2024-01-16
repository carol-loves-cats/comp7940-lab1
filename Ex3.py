# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
# your code here

def print_factor(x):
	for i in range(x+1):
		if x % (i+1) == 0:
			print(i+1)

for i in l:
	print_factor(i)