from abc import ABCMeta, abstractmethod

class TrackBaseRepository(object, metaclass=ABCMeta):
	
	@abstractmethod
	def get(self, id):
		pass

	