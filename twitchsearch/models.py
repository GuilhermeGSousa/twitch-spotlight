from django.db import models

class StreamData(models.Model):
    streamer_name = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time', auto_now_add=True)
    language = models.CharField(max_length=200, default='en')
