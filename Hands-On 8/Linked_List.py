'''
	Based entirely off Chapter 10 Requirements. This is not a full implementation of linked list.
	The only functions in Chapter 10 are list search, list insert and list delete.
'''

class Node:
	def __init__(self, key):
		self.key = key
		self.next = None
		print("Create Node: " + str(self.key))

class Linked_List:
	def __init__(self):
		self.head = None

	# Search singly linked list
	def list_search(self, key):
		temp = self.head
		while temp != None and temp.key != key:
			temp = temp.next
		print("Node found: " + str(temp))

	# Insert at head as instructed in book
	def list_insert(self, node):
		print("Insert Node: " + str(node.key))
		node.next = self.head
		self.head = node

	# Find and delete specified node
	def delete_node(self, node):
		curr = self.head
		prev = None

		while curr:
			if curr.key == node.key:
				if prev: prev.next = curr.next
				else: self.head = curr.next
				return
			prev = curr
			curr = curr.next

# Example
LL = Linked_List()

# Create Data
node0 = Node(3)
node1 = Node(6)
node2 = Node(1)
node3 = Node(5)

# Insert Data
LL.list_insert(node0)
LL.list_insert(node1)
LL.list_insert(node2)
LL.list_insert(node3)

# Search list
LL.list_search(6)

# Delete node
LL.delete_node(node1)