from django.http import HttpRequest
from django.shortcuts import render

from ..settings import MIN_TO_NEW_STREAM
from ._internal import stream_internal


def language(request : HttpRequest):

    return render(
        request,
        'twitchsearch/language.html',
        {}
    )

def stream(request : HttpRequest, language : str):

    data = {
        'stream_data' : stream_internal(language),
        'time_to_update' : MIN_TO_NEW_STREAM
    }

    return render(
        request, 
        'twitchsearch/stream.html', 
        data
    )
