import random
from datetime import datetime, timedelta

from django.http import Http404

from ..models import StreamData
from ..twitch import filter_low_view_streams, get_streams
from ..settings import MAX_STREAM_SEARCH_COUNT, MIN_TO_NEW_STREAM



def stream_internal(language) -> StreamData:

    ordered_objects = StreamData.objects.all().filter(language=language).order_by("-start_time")

    chosen_stream = _get_new_stream(language) if len(ordered_objects) == 0 else _update_stream(ordered_objects, language)

    return chosen_stream

def _get_new_stream(language):
    
    data = filter_low_view_streams(get_streams(max_streams=MAX_STREAM_SEARCH_COUNT, language=language))

    # Get random one not in database

    # TODO : Sometimes, MAX_STREAM_SEARCH_COUNT is not large enough to find streams under 5 viewers (namely for english languages)
    # Fix that situation
    if len(data) == 0 : raise Http404("No stream found")

    stream = StreamData(
        streamer_name=data[random.randrange(0, len(data))]['user_name'],
        language=language
    )
    stream.save()

    return stream

def _update_stream(ordered_objects, language):
    current_stream = ordered_objects[0]
    stream_start_time = current_stream.start_time
    current_time = datetime.now(tz=stream_start_time.tzinfo)
    delta = current_time - stream_start_time

    if(delta > timedelta(minutes=MIN_TO_NEW_STREAM)):
        current_stream = _get_new_stream(language)

    return current_stream
