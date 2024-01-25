
def Get_Data(filename):
	file_data = []
	f = open(filename, "r")
	data = f.readlines()
	for line in data:
		file_data.append(int(line[0:len(line)-1]))
	return file_data
