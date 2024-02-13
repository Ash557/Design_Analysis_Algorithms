
def remove_duplicate(arr) : 
	cap = len(arr)
	index = 0
	while index < cap-1 :
		if arr[index] == arr[index+1]: 
			arr.pop(index)
			cap -= 1
		else : index += 1 
	return arr

if __name__ == "__main__" :
	# arr1 = [2, 2, 2, 2]
	# print(remove_duplicate(arr1))
	# arr2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
	# print(remove_duplicate(arr2))

	print("Enter SORTED elements of array seperated by a space: ")
	sorted_arr = list(input().strip().split(" "))
	print(remove_duplicate(sorted_arr))