# Name:
# Date:

import random

class HeapPriorityQueue():
	
	def __init__(self):
		self.queue = ["dummy"]  # we do not use index 0 for easy index calulation
		self.current = 1        # to make this object iterable

	def next(self):            # define what __next__ does
		if self.current >=len(self.queue):
			self.current = 1     # to restart iteration later
			raise StopIteration
	 
		out = self.queue[self.current]
		self.current += 1
	
		return out

	def __iter__(self):
		return self

	__next__ = next

	def isEmpty(self):
		return len(self.queue) == 1    # b/c index 0 is dummy

	def swap(self, a, b):
		self.queue[a], self.queue[b] = self.queue[b], self.queue[a]

	# Add a value to the heap_pq
	def push(self, value):
		self.queue.append(value)
		self.heapUp(len(self.queue) - 1)

	# helper method for push      
	def heapUp(self, k):
		while k > 1:
			parent = k // 2
			if self.queue[parent] <= self.queue[k]:
				break
			self.swap(parent, k)
			k = parent
					
	# helper method for reheap and pop
	def heapDown(self, k, size):
		while 2 * k < size:
			l = 2 * k
			r = l + 1
			smaller = l
			if r < size and self.queue[r] < self.queue[l]:
				smaller = r
			if self.queue[k] <= self.queue[smaller]:
				break
			self.swap(k, smaller)
			k = smaller
	
	# make the queue as a min-heap            
	def reheap(self):
		for k in range((len(self.queue) - 1) // 2, 0, -1):
			self.heapDown(k, len(self.queue))
	
	# remove the min value (root of the heap)
	# return the removed value            
	def pop(self):
		min = self.queue[1]
		last = self.queue.pop()
		if not self.isEmpty():
			self.queue[1] = last
			self.heapDown(1, len(self.queue))
		return min
		
	# remove a value at the given index (assume index 0 is the root)
	# return the removed value   
	def remove(self, index):
		q_i = index + 1
		removed = self.queue[q_i]
		last = self.queue.pop()
		if q_i < len(self.queue):
			self.queue[q_i] = last
			parent = q_i // 2
			if q_i > 1 and self.queue[q_i] < self.queue[parent]:
				self.heapUp(q_i)
			else:
				self.heapDown(q_i, len(self.queue))
		return removed
	
  

# This method is for testing. Do not change it.
def isHeap(heap, k):
	l, r = 2*k, 2*k+1
	if l == len(heap): return True
	elif len(heap) == r and heap[k] > heap[l]: return False
	elif r < len(heap): 
		if (heap[k] > heap[l] or heap[k] > heap[r]): return False
		else: return isHeap(heap, l) and isHeap(heap, r)
	return True
	 
# This method is for testing. Do not change it.
def main():
		  
	pq = HeapPriorityQueue()    # create a HeapPriorityQueue object
	
	print ("Check if dummy 0 is still dummy:", pq.queue[0])
	
	# assign random integers into the pq
	for i in range(20):
		t = random.randint(10, 99)
		print (t, end=" ")
		pq.push(t)
	
	print ()
	
	# print the pq which is a min-heap
	for x in pq:
		print (x, end=" ")
	print()
	
	# remove test
	print ("Index 4 is removed:", pq.remove(4))
	
	# check if pq is a min-heap
	for x in pq:
		print (x, end=" ")
	print("\nIs a min-heap?", isHeap(pq.queue, 1))
	
	temp = []
	while not pq.isEmpty():
		temp.append(pq.pop())
		print (temp[-1], end=" ")
	
	print ("\nIn ascending order?", temp == sorted(temp))

if __name__ == '__main__':
	main()