import imp
from twitchAPI.twitch import Twitch
from .settings import MIN_VIEW_COUNT, TWITCH_SPOTLIGHT_APP_ID, TWITCH_SPOTLIGHT_APP_SECRET, STREAM_LANGUAGE

def get_streams(max_streams = 500, language = STREAM_LANGUAGE):
    twitch = Twitch(TWITCH_SPOTLIGHT_APP_ID, TWITCH_SPOTLIGHT_APP_SECRET)

    response = twitch.get_streams(language=[STREAM_LANGUAGE], first=100)

    while 'cursor' in response['pagination'].keys() and len(response['data']) < max_streams:
        cursor = response['pagination']['cursor']
        first_count = min(100, max_streams - len(response['data']))
        extra_data = twitch.get_streams(language=[language], first=first_count, after=cursor)
        response['data'] += extra_data['data']
        response['pagination'] = extra_data['pagination']

    return response['data']

def filter_low_view_streams(data, min_view_count = MIN_VIEW_COUNT):
    return list(filter(lambda x : x["viewer_count"] <= min_view_count, data))



