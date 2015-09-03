# author: lance
class CircularQueue:
	"""docstring for CircularQueue"""
	class _Note:
		__slots__ = '_element', '_next'
		def __init__(self.element, next):
			self._element = element
			self._next = next

	def __init__(self):
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		return head._element

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		
