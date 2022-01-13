# Python program to count Even
# and Odd numbers in a array

# array of numbers
array = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in array
for num in array:
	
	# checking condition
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1
		
print("Even numbers in the array: ", even_count)
print("Odd numbers in the array: ", odd_count)
