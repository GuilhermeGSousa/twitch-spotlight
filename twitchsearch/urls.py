from django.urls import path
from . import views

app_name = 'twitchsearch'
urlpatterns = [
    path('', views.language, name='language'),
    path('<str:language>/', views.stream, name='stream'),

]
