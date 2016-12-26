from rest_framework import serializers

class TrackSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=256)
    track_number = serializers.IntegerField()