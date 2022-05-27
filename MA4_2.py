#!/usr/bin/env python3.9
#Redovisade för: David R
#2022-05-18

from person import Person
import matplotlib.pyplot as plt
from time import ctime, perf_counter as pc
from numba import njit


@njit
def fib_py(n):
    if n <= 1:
        return n
    else:
        return (fib_py(n-1) + fib_py(n-2))

def main():
	fig, axis = plt.subplots()

	nums = [n for n in range(30,46)]
	ctime =[]
	for num in nums:
		start=pc()
		f = Person(num)
		f.fib()
		end=pc()
		temp = round(end-start, 2)
		ctime.append(temp)
		print(f"C++ for n = {num} took {temp} sec")

	axis.scatter(nums, ctime)
	plt.savefig(f'fibtidC.png')

	ptime = []
	for i in nums:
		start = pc()
		fib_py(i)
		end = pc()
		temp = round(end-start, 2)
		ptime.append(temp)
		print(f'Python for n = {i} took {temp} sec')

	axis.scatter(nums,ptime)
	plt.savefig(f'fibtidP.png')

	#############################################
	print('Going in to calculate fib for n = 47')
	f = Person(47)
	print(f.fib())
	print('Done with C++')
	print(fib_py(47))
	print('Done')


if __name__ == '__main__':
	main()