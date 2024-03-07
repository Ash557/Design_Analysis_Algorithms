
def quicksort(arr, low, high):
	if low < high:
		part = partition(arr, low, high-1)
		quicksort(arr, low, part)
		quicksort(arr, part+1, high)

def partition(arr, low, high):
	pivot = arr[high]
	i = low-1
	for j in range(low, high):
		if arr[j] <= pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def ith_order_statistic(arr, i):
	quicksort(arr, 0, len(arr)-1)
	return arr[i]

if __name__ == "__main__":
	arr = [5, 7, 2, 4, 9, 3, -2, 0, 1, -1]
	i = 2
	result = ith_order_statistic(arr, i)
	print(f"The {i+1}th order statistic is: {result}")