from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..serializers import StreamDataSerializer
from ._internal import stream_internal


@api_view(['GET'])
def stream(request, language):
    stream_data = stream_internal(language)
    serializer = StreamDataSerializer(stream_data)   
    return Response(serializer.data, status=status.HTTP_200_OK)