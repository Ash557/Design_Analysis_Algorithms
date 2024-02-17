from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from Get_Data import Get_Data

import time

import random

def create_set(N) :
	set = []
	  
	for i in range(N):
		set.append(random.randint(-10000, 10000))
		
	return set
	
def write_to_file(filename, dataset):
	for data in dataset:
		filename.write(str(data)+"\n")
	
def Create_Data_Set() :

	sizes = [5, 100, 1000, 10000, 50000, 100000]
	new = []
	for size in sizes:
		new = create_set(size)
		
		#send data to new file
		f = open("Datafile_Size_"+str(size), "w")
		write_to_file(f, new)



if __name__ == "__main__" :
	files = ["Datafile_Size_5", "Datafile_Size_100", "Datafile_Size_1000", "Datafile_Size_10000", "Datafile_Size_50000", "Datafile_Size_100000"]
	for i in range(5) :
		Create_Data_Set()

		print("------------ Run " + str(i+1) + "-----------")
		for filename in files :
			new_data = Get_Data(filename)
			start_time = time.time()
			bubble_sort(new_data)
			print(filename + "\t---- %.3f seconds ------" % (time.time()-start_time))
			
			
			
			
			
