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
	def __init__(self, id = None, title=None, img = None, autor = None, album = None, file = None, track_number = None):
		self.__set_id(id)
		self.__set_title(title)
		self.__set_img(img)
		self.__set_autor(autor)
		self.__set_album(album)
		self.__set_file(file)
		self.__set_track_number(track_number)


	def __get_id(self):
		return self.__id
	def __set_id(self, id):
		self.__id = id
	id = property(__get_id, __set_id)

	def __get_title(self):
		return self.__title
	def __set_title(self, title):
		self.__title = title
	title = property(__get_title, __set_title)

	def __get_img(self):
		return self.__img
	def __set_img(self, img):
		self.__img = img
	img = property(__get_img, __set_img)

	def __get_autor(self):
		return self.__autor
	def __set_autor(self, autor):
		self.__autor = autor
	autor = property(__get_autor, __set_autor)

	def __get_album(self):
		return self.__album
	def __set_album(self, album):
		self.__album = album
	album = property(__get_album, __set_album)

	def __get_file(self):
		return self.__file
	def __set_file(self, file):
		self.__file = file
	file = property(__get_file, __set_file)

	def __get_track_number(self):
		return self.__track_number
	def __set_track_number(self, track_number):
		self.__track_number = track_number
	track_number = property(__get_track_number, __set_track_number)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
	
	def __str__(self):
		return str(self.__dict__)