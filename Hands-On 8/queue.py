class queue_class:
	# Initialize the queue
	def __init__(self, length):
		self.length = length -1
		self.queue = [None]*length
		self.head = 0
		self.tail = 0
		self.queue[self.head] = True # Covering first enqueue case

	# Print the queue
	def print_queue(self):
		print("Queue: " + str(self.queue))

	# Enqueue x, but only if the queue is not full. If the queue is full, return cannot enqueue message
	def enqueue(self, x):
		print("Enqueue: " + str(x))
		if self.tail == self.head and self.queue[self.head] != True: # Check that it is not the very first input case
			print("ERROR: Cannot enqueue " + str(x))
			return
		self.queue[self.tail] = x
		if self.tail == self.length: self.tail = 0
		else: self.tail += 1

	def dequeue(self):
		x = self.queue[self.head]
		if self.head == self.tail and (x == None or x == True):
			print("ERROR: Empty Queue")
			self.queue[self.head] = True
			return
		print("Dequeue: " + str(x))
		self.queue[self.head] = None
		if self.head == self.length: self.head = 0
		else: self.head += 1
		return x

# Example for queue of size 5
Q = queue_class(5)

# Enqueue 3 ints
Q.enqueue(4)
Q.enqueue(2)
Q.enqueue(9)

# Print the queue
Q.print_queue()

# Dequeue an element
Q.dequeue()

# Print the queue
Q.print_queue()

# Enqueue too many ints
Q.enqueue(3)
Q.enqueue(0)
Q.enqueue(2)
Q.enqueue(5)

# Print the queue
Q.print_queue()

# Dequeue until empty
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()

# Print the queue
Q.print_queue()

# Attempt dequeue on empty queue
Q.dequeue()

# Attempt enqueue
Q.enqueue(5)
Q.enqueue(2)
Q.enqueue(3)

# Print the queue
Q.print_queue()