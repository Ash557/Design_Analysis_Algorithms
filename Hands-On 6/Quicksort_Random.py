import random
	
def quicksort(arr, start, end):
	print("start: " + str(start) + " End: " + str(end))
	if start < end:
		part = partition(arr, start, end-1)
		quicksort(arr, start, part)
		quicksort(arr, part+1, end)

def partition(arr, start, end):
	p = random.randint(start, end)
	arr[end], arr[p] = arr[p], arr[end]
	pivot = arr[end]
	i = start-1
	for j in range(start, end):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[end] = arr[end], arr[i+1]
	return i+1