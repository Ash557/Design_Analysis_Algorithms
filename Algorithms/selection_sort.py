def selection_sort(dataset):
	i = 0
	j = 0
	n = len(dataset)
	
	for i in range(n):
		# find smallest number in the non sorted part of the dataset
		smallest_index = i
		for j in range(i, n) :
			if dataset[j] < dataset[smallest_index]: smallest_index = j
		dataset[smallest_index], dataset[i] = dataset[i], dataset[smallest_index]
		
	return dataset
