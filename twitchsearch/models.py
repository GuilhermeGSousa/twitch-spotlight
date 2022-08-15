from django.db import models

class StreamData(models.Model):
    url = models.URLField(max_length=200)
    streamer_name = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time', auto_now_add=True)
