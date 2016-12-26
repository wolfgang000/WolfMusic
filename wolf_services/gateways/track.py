from abc import ABCMeta, abstractmethod
from ..models import Track as DB_Track
from ..entities.track import Track

class TrackBaseRepository(object, metaclass=ABCMeta):
	
	@abstractmethod
	def get(self, id):
		pass

class TrackDjangoOrmRepository(TrackBaseRepository):
	
	def get(self, id):
		db_track = None
		try:
			db_track = DB_Track.objects.get(pk=id)
		except DB_Track.DoesNotExist:
			return None

		return self.mapper_db_to_entity(db_track)
	
	def add(self, track):
		db_track = self.mapper_entity_to_db(track)
		db_track.save()
		track.id = db_track.pk
		return track

	def update(self, track):
		pass 
	
	def delete(self, track):
		pass

	def mapper_db_to_entity(self, db_track):
		track = Track(
				id = db_track.id, 
				title = db_track.title,
				img = None,
				autor = None,
				album = None,
				file = None,
				track_number = db_track.track_number,
			)
		return track
	
	def mapper_entity_to_db(self, track):
		db_track = DB_Track(title=track.title, track_number = track.track_number)
		return db_track