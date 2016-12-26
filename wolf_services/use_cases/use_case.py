from .. import entities
import mutagen 


class UseCases:
	def __init__(self, track_repository):
		self.track_repository = track_repository

	def add_track(self, file_path):
		
		fileName, fileExtension = os.path.splitext( file_path)
		if fileExtension.lower().equals('.mp3'):
			tags =  mutagen.File(file_path)
			track = entities.track.Track()
			track.title = tags['TIT2'].text[0]
			track.track_number = tags['TRCK'].text[0]
			tags['TALB'].text[0] #Album

		else:
			raise('Error tipo no soportado')
		
		
	
	
