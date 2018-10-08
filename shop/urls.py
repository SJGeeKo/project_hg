from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allPaintings, name='allPaintings'),
    path('<slug:painting_slug>/', views.paintingDetail, name='paintingDetail'),
]