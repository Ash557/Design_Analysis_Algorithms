class stack_class:
	def __init__(self, max_size):
		self.max_size = max_size-1
		self.top = -1
		self.stack = [None]*max_size

	# Prints the stack
	def print_stack(self):
		print("Print Stack: \t" + str(self.stack))

	# Check if the stack is empty
	def stack_empty(self):
		if self.top == 0: return True
		else: return False

	# Push element to stack - as long as the stack is not at the max size
	def push(self, x):
		print("Push Element: " + str(x))
		if self.top >= self.max_size: 
			print("ERROR: Overflow")
			return
		self.top += 1
		self.stack[self.top] = x

	# Does not remove the element, just moves the self.top as instructed in the book
	def pop(self):
		if self.stack_empty(): 
			print("ERROR: underflow")
			return -1
		else:
			self.top = self.top - 1
			return self.stack[self.top+1]


# Example - stack of size 5
s = stack_class(5)

# Check for if the stack is empty
print("Stack Empty? " + str(s.stack_empty()))

# Push ints to the stack
s.push(4)
s.push(2)
s.push(7)

# Print stack
s.print_stack()

# Check for if the stack is empty
print("Stack Empty? " + str(s.stack_empty()))

#Pop element
print("Pop element: " + str(s.pop()))

# Print stack
s.print_stack()

# Push until you hit the max size
s.push(8)
s.push(2)
s.push(1)
s.push(9)

# Print stack
s.print_stack()

#Pop elements until it is empty
print("Pop element: " + str(s.pop()))
print("Pop element: " + str(s.pop()))
print("Pop element: " + str(s.pop()))
print("Pop element: " + str(s.pop()))
print("Pop element: " + str(s.pop()))
print("Pop element: " + str(s.pop()))

# Print stack
s.print_stack()