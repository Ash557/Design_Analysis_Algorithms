import random
import math
from node import Node
from linked_list import Linked_List

class HashTable:
	def __init__ (self):
		# print("HT: INIT")
		self.max_size = 2
		self.table = [0]*2

	# Search each list for a given key
	def search_key(self, key):
		# print("HT: SEARCH_KEY")
		temp = None
		for x in self.table:
			if x == 0 : continue
			temp = x.list_search(key)
			if temp != None : 
				print("Key Found: " + str(temp))
				return x
		print("Key Not Found.")
		return None

	def get_index(self, index):
		# print("HT: GET_INDEX")
		if index < 0 or index >= self.table_length(): 
			print("ERROR: Index out of range.")
			return
		return self.table[index]

	# Division Hash - to implement copy lines 35-38 and copy to lines 96-100, and change node to y
	# def insert_hash(self, node):
	## 	print("HT: INSERT_HASH_DIV")
	# 	hashval = node.key % self.max_size
	# 	if self.table[hashval] == 0:
	# 		self.table[hashval] = Linked_List()
	# 	self.table[hashval].list_insert(node)
	# 	self.resize()

	# Multiplication Hash - to implement copy lines 44-48 and copy to lines 96-99, and change node to y
	def insert_hash(self, node):
		# print("HT: INSERT_HASH_MUL")
		A = random.uniform(0, 1)
		hashval = math.floor(self.max_size * ((node.key*A) % 1))
		if self.table[hashval] == 0: 
			self.table[hashval] = Linked_List()
		self.table[hashval].list_insert(node)
		self.resize()

	def delete_key(self, key):
		# print("HT: DELETE_KEY")
		temp = self.search_key(key) 
		if temp == None: print("Key does not exist")
		else: temp.delete_node(key)

	# Print full hash table with keys and values
	def print_table(self):
		# print("HT: PRINT_TABLE")
		for x in self.table:
			if x != 0: x.print_list()
		return

	# Find number of slots in the table that are taken
	def table_length(self):
		# print("HT: TABLE_LENGTH")
		count = 0
		for x in self.table:
			if x != 0:
				count += 1
		return count

	# Resize table according to current size
	def resize(self):
		# print("HT: RESIZE")
		length = self.table_length()
		table_copy = self.table
		if length == self.max_size:
			print("Table is full. Resizing to double the original size.")
			self.max_size = 2*self.max_size
			self.table = [0] * self.max_size
		elif length == self.max_size//4:
			print("Table has very few elements in it. Reducing table size by 1/4th.")
			self.max_size = self.max_size
			self.table = [0] * self.max_size
		else: 
			print("Hash table does not need resizing.")
			return

		temp = []
		for x in table_copy :
			if x != 0:
				temp = x.node_list()
				for y in temp: 
					A = random.uniform(0, 1)
					hashval = math.floor(self.max_size * ((y.key*A) % 1))
					if self.table[hashval] == 0: 
						self.table[hashval] = Linked_List()
					self.table[hashval].list_insert(y)
		print("Hash table has been resized.")

hashtable = HashTable()
node0 = Node(1, 4)
node1 = Node(5, 0)
node2 = Node(9, 2)
node3 = Node(2, 6)

hashtable.print_table()
print("Length of table: " + str(hashtable.table_length()))
hashtable.insert_hash(node0)
hashtable.print_table()

hashtable.insert_hash(node1)
hashtable.insert_hash(node2)
hashtable.insert_hash(node3)
hashtable.print_table()

hashtable.delete_key(9)

hashtable.print_table()