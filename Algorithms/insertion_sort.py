def insertion_sort(dataset):
	n = len(dataset)
	
	if n <= 1 : return dataset
	
	for index in range(1, n):
		key = dataset[index]
		temp = index-1
		while (key < dataset[temp]) and (temp >= 0) : 
			dataset[temp+1] = dataset[temp]
			temp -= 1
		dataset[temp+1] = key

	return dataset
