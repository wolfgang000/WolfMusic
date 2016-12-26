class file:
	def __init__(self):
		self._path = None

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, value):
		self._path = value

	def read(self):
		with open(self._path, 'rb',) as f:
			content = f.read()
		return content

class Track:
	def __init__(self):
		self._id = None
		self._name = None
		self._img = None
		self._autor = None
		self._album = None
		self._file = None
		self._number = None

	