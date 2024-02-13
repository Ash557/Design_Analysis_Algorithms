def sort(arr1, arr2): 
	sorted_arr = []
	i1 = 0
	i2 = 0

	while i1 < len(arr1) and i2 < len(arr2) :
		if int(arr1[i1]) <= int(arr2[i2]) :
			sorted_arr.append(arr1[i1])
			i1+=1
		else : #arr2 is bigger
			sorted_arr.append(arr2[i2])
			i2+=1

	if i1 < len(arr1) : 
		for h in range(i1, len(arr1)) :
			sorted_arr.append(arr1[h])
	elif i2 < len(arr2) :
		for p in range(i2, len(arr2)) :
			sorted_arr.append(arr2[p])

	return sorted_arr

if __name__ == "__main__":

	print("Enter the number of arrays: ")
	input_k = input()
	print("Enter the size of arrays: ")
	input_n = input()

	base_arr = []
	next_arr = []

	print("Enter SORTED elements of FIRST array seperated by a space: ")
	base_arr = list(input().split(" "))

	# print("Array 1: " + str(base_arr))
	for e in range(int(input_k)-1) :
		print("Enter SORTED elements of NEXT array seperated by a space: ")
		next_arr = list(input().split(" "))
		# print("Array " + str(e+2) + ": " + str(next_arr))
		base_arr = sort(base_arr, next_arr)
		# print("Current: " + str(base_arr))

	print("Final Sorted Array: ")
	print(base_arr)