from django.urls import path
from . import views

app_name = 'artist'

urlpatterns = [
    path('<slug:artist_slug>', views.artistDetailView, name='artistDetailView'),
]