from rest_framework import serializers
from .models import StreamData

class StreamDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamData
        fields = ['streamer_name', 'start_time', 'language']