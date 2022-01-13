# Python 3 code to demonstrate removing duplicated from array using naive methods

# initializing array
array = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original array is : " + str(array))

# using naive method to remove duplicated from array
res = []
for i in array:
	if i not in res:
		res.append(i)

# printing array after removal
print ("The array after removing duplicates : " + str(res))
