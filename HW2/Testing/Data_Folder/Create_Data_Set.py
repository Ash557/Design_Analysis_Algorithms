#!/usr/bin/python

import random

def create_set(N) :
	set = []
	  
	for i in range(N):
		set.append(random.randint(-10000, 10000))
		
	return set
	
def write_to_file(filename, dataset):
	for data in dataset:
		filename.write(str(data)+"\n")
	
def Create_Data_Set :

	sizes = [5, 10, 20, 100, 1000, 10000, 100000]
	new = []
	for size in sizes:
		new = create_set(size)
		
		#send data to new file
		f = open("Datafile_Size_"+str(size), "w")
		write_to_file(f, new)
