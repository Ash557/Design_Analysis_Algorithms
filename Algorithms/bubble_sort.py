def bubble_sort(dataset):
	n = len(dataset)
	if n <= 1 : return dataset
	
	for i in range(n):
		swapped = False
	
		for j in range(0, n-i-1):
			if dataset[j] > dataset[j+1]:
				dataset[j], dataset[j+1] = dataset[j+1], dataset[j]
				swapped = True
				
		if swapped == False:
			break
			
	
	return dataset
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
