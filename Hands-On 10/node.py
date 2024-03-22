class Node:
	def __init__(self, key, data):
		# print("N: INIT")
		self.key = key
		self.data = data
		self.next = None
		self.prev = None
		print("Create Node: " + str(self.key))