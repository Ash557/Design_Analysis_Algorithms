class Linked_List:
	def __init__(self):
		# print("LL: INIT")
		self.head = None

	# Search linked list
	def list_search(self, key):
		# print("LL: LIST_SEARCH")
		temp = self.head
		while temp != None and temp.key != key:
			temp = temp.next
		if temp != None: return str(temp.data)
		else: return None

	# Insert at head as instructed in book
	def list_insert(self, node):
		# print("LL: LIST_INSERT")
		print("Insert Node: " + str(node.key))
		if self.head == None: self.head = node
		else:
			self.head.prev = node
			node.next = self.head
			self.head = node

	# Find and delete specified node
	def delete_node(self, key):
		# print("LL: DELETE_NODE")
		curr = self.head

		while curr:
			if curr.key == key:
				if curr.prev: #if previous node exists
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
				else: 
					self.head = curr.next
					self.head.prev = None
				print("Node with key " + str(key) + " deleted.")
				return
			curr = curr.next
		print("Node with key " + str(key) + " not found")

	def print_list(self):
		# print("LL: PRINT_LIST")
		temp = self.head
		while temp != None:
			print("Key: " + str(temp.key) + "  Value: " + str(temp.data))
			temp = temp.next
		return

	def node_list(self):
		# print("LL: NODE_LIST")
		if self.head == None: return None
		n_list = []
		temp = self.head
		while temp != None:
			n_list.append(temp)
			temp = temp.next
		return n_list