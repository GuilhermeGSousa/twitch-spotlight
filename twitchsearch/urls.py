from django.urls import path

from .views import rest
from .views import template

app_name = 'twitchsearch'
urlpatterns = [
    path('', template.language, name='language'),
    path('<str:language>/', template.stream, name='stream'),
    path('api/stream/<str:language>/', rest.stream)
]