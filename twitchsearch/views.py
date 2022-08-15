import random
from datetime import datetime, timedelta

from django.shortcuts import render

from .models import StreamData
from .twitch import filter_low_view_streams, get_streams
from .settings import MIN_TO_NEW_STREAM

def index(request):
    
    ordered_objects = StreamData.objects.order_by("-start_time")

    chosen_stream = _get_new_stream() if len(ordered_objects) == 0 else _update_stream(ordered_objects)
    
    return render(
        request, 
        'twitchsearch/index.html', 
        {
            'stream_data' : chosen_stream,
            'time_to_update' : MIN_TO_NEW_STREAM
        })

def _get_new_stream():
    
    data = filter_low_view_streams(get_streams(max_streams=2000))

    # Get random one not in database
    stream = StreamData(
        streamer_name=data[random.randrange(0, len(data))]['user_name']
    )
    stream.save()

    return stream

def _update_stream(ordered_objects):
    current_stream = ordered_objects[0]
    stream_start_time = current_stream.start_time
    current_time = datetime.now(tz=stream_start_time.tzinfo)
    delta = current_time - stream_start_time
    if(delta > timedelta(minutes=MIN_TO_NEW_STREAM)):
        current_stream = _get_new_stream()

    return current_stream
