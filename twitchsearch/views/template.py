from django.shortcuts import render

from ._internal import stream_internal
from ..settings import MIN_TO_NEW_STREAM

def language(request):

    return render(
        request,
        'twitchsearch/language.html',
        {}
    )

def stream(request, language):

    data = {
        'stream_data' : stream_internal(language),
        'time_to_update' : MIN_TO_NEW_STREAM
    }

    return render(
        request, 
        'twitchsearch/stream.html', 
        data
    )