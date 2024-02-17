def min_heapify(heap, heapsize, index):
	left = (index<<1) + 1
	right = (index<<1) + 2
	min_index = index

	if left < heapsize and heap[min_index] > heap[left]:
		min_index = left
	if right < heapsize and heap[min_index] > heap[right]:
		min_index = right
	if (min_index != index):
		heap[index], heap[min_index] = heap[min_index], heap[index]
		min_heapify(heap, heapsize, min_index)

def build_min_heap(array):
	n = len(array)
	parent = n // 2 -1
	while parent >= 0:
		min_heapify(array, n, parent)
		parent -= 1

def pop_root(heap):
	print("Root: " + str(heap[0]))
	heap.pop(0)
	build_min_heap(heap)

if __name__ == "__main__" :
	int_array = [2, 6, 2, 8, 5, 1, 0, 3, 7]
	print("ORIGINAL: " + str(int_array))
	build_min_heap(int_array)
	print("After function build_min_heap: " + str(int_array))
	pop_root(int_array)
	print("After root popped: " + str(int_array))

	float_array = [5.5, 3.6, 7.9, 2.3, 7.33, 6.4, 1.6]
	print("ORIGINAL: " + str(float_array))
	build_min_heap(float_array)
	print("After function build_min_heap: " + str(float_array))
	pop_root(float_array)
	print("After root popped: " + str(float_array))

	str_array = ["strings", "str", "s", "tr", "st", "string", "Strings", "S", "Trings", "Tr"]
	print("ORIGINAL: " + str(str_array))
	build_min_heap(str_array)
	print("After function build_min_heap: " + str(str_array))
	pop_root(str_array)
	print("After root popped: " + str(str_array))