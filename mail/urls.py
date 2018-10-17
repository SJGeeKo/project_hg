from django.urls import path
from . import views

app_name = 'mail'

urlpatterns = [
    path('sendEmail/', views.sendEmail, name='sendEmail'),
    path('<slug:painting_slug>/sendBrochure/', views.sendBrochure, name='send_brochure'),
]