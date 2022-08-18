from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from ..serializers import StreamDataSerializer
from ._internal import stream_internal


@api_view(['GET'])
def stream(request : Request):
    language = request.query_params.get('language')

    stream_data = stream_internal(language)
    serializer = StreamDataSerializer(stream_data)   
    return Response(serializer.data, status=status.HTTP_200_OK)