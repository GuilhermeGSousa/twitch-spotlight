from django.urls import path
from . import views

app_name = 'twitchsearch'
urlpatterns = [
    path('', views.stream, name='stream'),
    path('<str:language>/', views.stream, name='stream'),

]
