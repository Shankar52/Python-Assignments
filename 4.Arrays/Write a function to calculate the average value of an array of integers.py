def average( a , n ):

	sum = 0
	for i in range(n):
		sum += a[i]
	
	return sum/n

arr = [10, 2, 3, 4, 1, 5, 6, 7, 8, 9]
n = len(arr)
print(average(arr, n))
