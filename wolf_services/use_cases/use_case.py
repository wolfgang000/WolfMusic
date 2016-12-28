from .. import entities

import io
from mutagen.ogg import OggPage
from mutagen.mp3 import MP3


class UseCases:
	def __init__(self, track_repository):
		self.track_repository = track_repository

	def add_track(self, file, type):
		if type =='.mp3':
			f = io.BytesIO(file)
			tags =  MP3(fileobj=f)
			track = entities.track.Track()
			track.title = tags['TIT2'].text[0]
			track.track_number = int(tags['TRCK'].text[0])
			tags['TALB'].text[0] #Album
			return track
		else:
			raise('Error tipo no soportado')
		
		
	
	
